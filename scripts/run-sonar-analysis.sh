#!/bin/bash

# SonarQube Analysis Helper Script
# This script helps run SonarQube analysis locally during development

set -e

# Load environment variables from .env file if it exists
if [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
fi

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
SONAR_CLOUD_CONFIG="sonar-project.cloud.properties"
SONAR_LOCAL_CONFIG="sonar-project.local.properties"
SCANNER_VERSION="4.8.0.2856"

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if SonarQube server is running
check_sonarqube_server() {
    print_status "Checking SonarQube server status..."
    
    if curl -s http://localhost:9000/api/system/status > /dev/null 2>&1; then
        print_success "SonarQube server is running"
        return 0
    else
        print_error "SonarQube server is not running at http://localhost:9000"
        print_warning "Please ensure your local SonarQube instance is running on port 9000"
        return 1
    fi
}

# Function to install SonarQube scanner
install_scanner() {
    print_status "Installing SonarQube scanner..."
    
    if command -v sonar-scanner > /dev/null 2>&1; then
        print_success "SonarQube scanner is already installed"
        return 0
    fi
    
    # Download and install scanner
    SCANNER_DIR="/tmp/sonar-scanner"
    mkdir -p $SCANNER_DIR
    cd $SCANNER_DIR
    
    print_status "Downloading SonarQube scanner..."
    wget -q "https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SCANNER_VERSION}-linux.zip"
    
    print_status "Extracting scanner..."
    unzip -q "sonar-scanner-cli-${SCANNER_VERSION}-linux.zip"
    
    # Add to PATH for this session
    export PATH="$SCANNER_DIR/sonar-scanner-${SCANNER_VERSION}-linux/bin:$PATH"
    
    print_success "SonarQube scanner installed temporarily"
    print_warning "For permanent installation, add to your PATH: $SCANNER_DIR/sonar-scanner-${SCANNER_VERSION}-linux/bin"
}

# Function to run tests and generate coverage
run_tests() {
    print_status "Running tests with coverage..."
    
    # Install test dependencies
    pip install pytest pytest-cov
    
    # Run tests
    pytest --cov=todo_cli --cov-report=xml --cov-report=term-missing tests/
    
    if [ $? -eq 0 ]; then
        print_success "Tests completed successfully"
    else
        print_error "Tests failed"
        exit 1
    fi
}

# Function to run SonarCloud analysis
run_sonarcloud_analysis() {
    print_status "Running SonarCloud analysis..."
    
    if [ -z "$SONAR_TOKEN" ]; then
        print_error "SONAR_TOKEN environment variable is not set"
        print_warning "Set it with: export SONAR_TOKEN=your_sonarcloud_token"
        return 1
    fi
    
    # Use SonarCloud configuration
    sonar-scanner \
        -Dproject.settings=$SONAR_CLOUD_CONFIG \
        -Dsonar.login=$SONAR_TOKEN
    
    print_success "SonarCloud analysis completed"
}

# Function to run local SonarQube analysis
run_local_analysis() {
    print_status "Running local SonarQube analysis..."
    
    if [ -z "$SONAR_TOKEN_LOCAL" ]; then
        print_error "SONAR_TOKEN_LOCAL environment variable is not set"
        print_warning "Set it with: export SONAR_TOKEN_LOCAL=your_local_sonarqube_token"
        return 1
    fi
    
    # Check if server is running
    check_sonarqube_server || return 1
    
    # Use local SonarQube configuration with local token
    SONAR_TOKEN=$SONAR_TOKEN_LOCAL sonar-scanner \
        -Dproject.settings=$SONAR_LOCAL_CONFIG
    
    print_success "Local SonarQube analysis completed"
}

# Main script logic
main() {
    echo "🔍 SonarQube Analysis Helper"
    echo "============================"
    
    # Check if we're in the project root
    if [ ! -f "pyproject.toml" ]; then
        print_error "Please run this script from the project root directory"
        exit 1
    fi
    
    # Parse command line arguments
    case "${1:-help}" in
        "cloud")
            print_status "Running SonarCloud analysis..."
            install_scanner
            run_tests
            run_sonarcloud_analysis
            ;;
        "local")
            print_status "Running local SonarQube analysis..."
            install_scanner
            run_tests
            run_local_analysis
            ;;
        "test")
            print_status "Running tests only..."
            run_tests
            ;;
        "install")
            print_status "Installing SonarQube scanner..."
            install_scanner
            ;;
        "check")
            print_status "Checking SonarQube server..."
            check_sonarqube_server
            ;;
        "help"|*)
            echo "Usage: $0 [cloud|local|test|install|check|help]"
            echo ""
            echo "Commands:"
            echo "  cloud   - Run SonarCloud analysis (requires SONAR_TOKEN)"
            echo "  local   - Run local SonarQube analysis (requires SONAR_TOKEN_LOCAL)"
            echo "  test    - Run tests with coverage only"
            echo "  install - Install SonarQube scanner"
            echo "  check   - Check if local SonarQube server is running"
            echo "  help    - Show this help message"
            echo ""
            echo "Environment variables:"
            echo "  SONAR_TOKEN       - SonarCloud authentication token"
            echo "  SONAR_TOKEN_LOCAL - Local SonarQube authentication token"
            ;;
    esac
}

# Run main function with all arguments
main "$@" 