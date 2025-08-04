# Dual SonarQube Setup Guide

This project is configured to work with both SonarCloud (cloud-based) and local SonarQube server for code quality analysis.

## Configuration Files

### 1. SonarCloud Configuration (`sonar-project.cloud.properties`)
- **Host**: https://sonarcloud.io
- **Project Key**: `germanmtz93_TodoGuru`
- **Organization**: `germanmtz93`
- **Features**: Cloud-based analysis with automatic quality gates

### 2. Local SonarQube Configuration (`sonar-project.local.properties`)
- **Host**: http://localhost:9000
- **Project Key**: `TodoGuru-local`
- **Features**: Self-hosted analysis for internal development

## GitHub Actions Workflows

### 1. SonarCloud Analysis (`sonarcloud-analysis.yml`)
- **Trigger**: Push to main/develop, PRs, manual dispatch
- **Runner**: Ubuntu latest
- **Features**:
  - Automatic test coverage generation
  - SonarCloud integration
  - Quality gate enforcement
  - Coverage report artifacts

### 2. Local SonarQube Analysis (`sonarqube-local-analysis.yml`)
- **Trigger**: Push to main/develop, PRs, manual dispatch
- **Runner**: Self-hosted (requires local SonarQube access)
- **Features**:
  - Local SonarQube server integration
  - Manual scanner installation
  - Quality gate enforcement
  - Coverage report artifacts

## Required Secrets

### For SonarCloud:
- `SONAR_TOKEN`: SonarCloud authentication token
- `GITHUB_TOKEN`: GitHub token (automatically provided)

### For Local SonarQube:
- `SONAR_TOKEN_LOCAL`: Local SonarQube authentication token

### Environment Variables Setup
1. Copy `.env.example` to `.env`: `cp .env.example .env`
2. Fill in your actual tokens in the `.env` file
3. The `.env` file is automatically loaded by the helper scripts

## Setup Instructions

### SonarCloud Setup
1. Create a SonarCloud account at https://sonarcloud.io
2. Create a new organization or join existing one
3. Create a new project in SonarCloud
4. Generate a token in SonarCloud user settings
5. Add the token as `SONAR_TOKEN` secret in GitHub repository settings

### Local SonarQube Setup
1. Ensure your local SonarQube instance is running on port 9000
2. Access SonarQube at http://localhost:9000
3. Create a new project in local SonarQube (if not already created)
4. Generate a token for the project
5. Add the token as `SONAR_TOKEN_LOCAL` secret in GitHub repository settings

### Self-Hosted Runner Setup (for Local Analysis)
1. Set up a self-hosted GitHub Actions runner
2. Ensure the runner has access to your local SonarQube server (port 9000)
3. Configure the runner to run on the `self-hosted` label

## Usage

### Running Analysis Manually
1. **SonarCloud**: Go to Actions → SonarCloud Analysis → Run workflow
2. **Local SonarQube**: Go to Actions → Local SonarQube Analysis → Run workflow

### Automatic Analysis
Both workflows run automatically on:
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop` branches

## Configuration Differences

| Feature | SonarCloud | Local SonarQube |
|---------|------------|-----------------|
| Host URL | https://sonarcloud.io | http://localhost:9000 |
| Project Key | germanmtz93_TodoGuru | TodoGuru-local |
| Runner | Ubuntu latest | Self-hosted |
| Scanner | Built-in action | Manual installation |
| Token Secret | SONAR_TOKEN | SONAR_TOKEN_LOCAL |

## Quality Gates

Both configurations include:
- Code coverage thresholds
- Code duplication detection
- Security hotspots analysis
- Code smells detection
- Technical debt tracking

## Troubleshooting

### SonarCloud Issues
- Verify `SONAR_TOKEN` secret is correctly set
- Check organization and project key match SonarCloud settings
- Ensure repository has proper permissions

### Local SonarQube Issues
- Verify SonarQube server is running and accessible
- Check `SONAR_TOKEN_LOCAL` secret is correctly set
- Ensure self-hosted runner has network access to local SonarQube
- Verify scanner installation and PATH configuration

### Common Issues
- **Coverage not found**: Ensure tests are running and generating coverage.xml
- **Authentication failed**: Verify tokens are valid and have proper permissions
- **Quality gate failed**: Review SonarQube quality gate configuration

## Best Practices

1. **Use both environments**: SonarCloud for CI/CD, Local for development
2. **Regular analysis**: Run analysis on every significant change
3. **Quality gates**: Configure appropriate quality thresholds
4. **Token security**: Rotate tokens regularly and use least privilege
5. **Coverage goals**: Maintain high test coverage for critical code paths 