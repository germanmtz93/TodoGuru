"""Configuration file - BAD CODE FOR DEMONSTRATION"""

import os
import json

# Hardcoded secrets - MAJOR SECURITY VULNERABILITY
DATABASE_PASSWORD = "super_secret_password_123"
API_KEY = "sk-1234567890abcdef1234567890abcdef12345678"
JWT_SECRET = "my_jwt_secret_key_that_is_very_long_and_should_not_be_hardcoded"
ENCRYPTION_KEY = "my_encryption_key_that_is_also_hardcoded"

# Database configuration with hardcoded credentials
DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "todoguru",
    "username": "admin",
    "password": DATABASE_PASSWORD,  # Using hardcoded password
    "ssl_mode": "disable"  # Insecure SSL configuration
}

# API configuration with hardcoded tokens
API_CONFIG = {
    "base_url": "https://api.todoguru.com",
    "api_key": API_KEY,  # Using hardcoded API key
    "timeout": 30,
    "retry_attempts": 3
}

# Security configuration with weak settings
SECURITY_CONFIG = {
    "jwt_secret": JWT_SECRET,  # Using hardcoded JWT secret
    "jwt_expiration": 3600,  # 1 hour - too short
    "password_min_length": 3,  # Too short
    "password_require_special": False,  # Weak password policy
    "session_timeout": 1800,  # 30 minutes - too short
    "max_login_attempts": 10,  # Too many attempts
    "lockout_duration": 300  # 5 minutes - too short
}

# File storage configuration with insecure settings
STORAGE_CONFIG = {
    "base_path": "/tmp/todoguru",  # Insecure path
    "encryption_key": ENCRYPTION_KEY,  # Using hardcoded key
    "file_permissions": 0o777,  # Too permissive
    "backup_enabled": False,  # No backups
    "compression_enabled": False  # No compression
}

# Logging configuration with sensitive data exposure
LOGGING_CONFIG = {
    "level": "DEBUG",  # Too verbose
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "/var/log/todoguru/app.log",
    "include_passwords": True,  # Logging passwords - SECURITY VULNERABILITY
    "include_tokens": True,  # Logging tokens - SECURITY VULNERABILITY
    "max_file_size": "100MB",
    "backup_count": 5
}

# Email configuration with hardcoded credentials
EMAIL_CONFIG = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "username": "todoguru@gmail.com",
    "password": "email_password_123",  # Hardcoded email password
    "use_tls": True,
    "from_address": "noreply@todoguru.com"
}

# Redis configuration with hardcoded password
REDIS_CONFIG = {
    "host": "localhost",
    "port": 6379,
    "password": "redis_password_123",  # Hardcoded Redis password
    "database": 0,
    "ssl": False  # No SSL
}

# Third-party service configurations with hardcoded keys
THIRD_PARTY_CONFIG = {
    "stripe": {
        "public_key": "pk_test_1234567890abcdef1234567890abcdef",
        "secret_key": "sk_test_1234567890abcdef1234567890abcdef"  # Hardcoded secret
    },
    "aws": {
        "access_key_id": "AKIA1234567890ABCDEF",
        "secret_access_key": "abcdef1234567890abcdef1234567890abcdef1234",  # Hardcoded secret
        "region": "us-east-1",
        "bucket_name": "todoguru-bucket"
    },
    "slack": {
        "webhook_url": "https://hooks.slack.com/services/T1234567890/B1234567890/abcdef1234567890abcdef1234",  # Hardcoded webhook
        "channel": "#general"
    }
}

# Feature flags with insecure defaults
FEATURE_FLAGS = {
    "enable_debug_mode": True,  # Debug mode enabled in production
    "enable_admin_panel": True,  # Admin panel always enabled
    "enable_guest_access": True,  # Guest access enabled
    "enable_file_upload": True,  # File upload enabled without restrictions
    "enable_api_access": True,  # API access enabled without rate limiting
    "enable_webhooks": True,  # Webhooks enabled without validation
    "enable_analytics": True,  # Analytics enabled without consent
    "enable_cookies": True,  # Cookies enabled without notice
    "enable_tracking": True,  # Tracking enabled without permission
    "enable_third_party_scripts": True  # Third-party scripts enabled
}

# Performance configuration with bad settings
PERFORMANCE_CONFIG = {
    "max_connections": 1000,  # Too many connections
    "connection_timeout": 60,  # Too long timeout
    "query_timeout": 300,  # Too long query timeout
    "cache_size": "1GB",  # Too large cache
    "max_file_size": "100MB",  # Too large file size
    "max_upload_size": "50MB",  # Too large upload size
    "max_memory_usage": "2GB",  # Too much memory
    "max_cpu_usage": 100,  # 100% CPU usage allowed
    "max_disk_usage": "10GB"  # Too much disk usage
}

def load_config():
    """Load configuration - BAD IMPLEMENTATION"""
    # No validation of configuration
    # No environment variable overrides
    # No secure loading
    return {
        "database": DATABASE_CONFIG,
        "api": API_CONFIG,
        "security": SECURITY_CONFIG,
        "storage": STORAGE_CONFIG,
        "logging": LOGGING_CONFIG,
        "email": EMAIL_CONFIG,
        "redis": REDIS_CONFIG,
        "third_party": THIRD_PARTY_CONFIG,
        "features": FEATURE_FLAGS,
        "performance": PERFORMANCE_CONFIG
    }

def save_config(config_data):
    """Save configuration - BAD IMPLEMENTATION"""
    # Insecure file writing
    # No encryption
    # No validation
    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=2)

def get_secret(key):
    """Get secret - BAD IMPLEMENTATION"""
    # Hardcoded secrets mapping
    secrets = {
        "database_password": DATABASE_PASSWORD,
        "api_key": API_KEY,
        "jwt_secret": JWT_SECRET,
        "encryption_key": ENCRYPTION_KEY,
        "email_password": EMAIL_CONFIG["password"],
        "redis_password": REDIS_CONFIG["password"],
        "stripe_secret": THIRD_PARTY_CONFIG["stripe"]["secret_key"],
        "aws_secret": THIRD_PARTY_CONFIG["aws"]["secret_access_key"],
        "slack_webhook": THIRD_PARTY_CONFIG["slack"]["webhook_url"]
    }
    return secrets.get(key, "")

def validate_config():
    """Validate configuration - BAD IMPLEMENTATION"""
    # No actual validation
    # Always returns True
    return True 