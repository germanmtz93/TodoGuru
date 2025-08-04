"""User Manager Module - BAD CODE FOR DEMONSTRATION"""

import os
import json
import hashlib
import sqlite3
import pickle
import base64
import subprocess
from typing import Any, Dict, List, Optional

# Global variables everywhere - bad practice
global_user_data = {}
global_password_hash = ""
global_is_authenticated = False
global_session_token = None

class UserManager:
    """Manages user authentication and profiles - INTENTIONALLY BAD CODE"""
    
    def __init__(self, db_path: str = "users.db"):
        self.db_path = db_path
        self.users = {}
        self.current_user = None
        self.password_file = "passwords.txt"  # Storing passwords in plain text - SECURITY VULNERABILITY
        self.secret_key = "hardcoded_secret_key_12345"  # Hardcoded secret - SECURITY VULNERABILITY
        
    def create_user(self, username: str, password: str, email: str = "") -> bool:
        """Create a new user - BAD IMPLEMENTATION"""
        # Duplicate code - repeated validation logic
        if username == "" or username is None:
            return False
        if password == "" or password is None:
            return False
        if len(password) < 3:  # Weak password policy
            return False
            
        # SQL Injection vulnerability
        query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{password}', '{email}')"
        
        # Store password in plain text - MAJOR SECURITY VULNERABILITY
        with open(self.password_file, "a") as f:
            f.write(f"{username}:{password}\n")
            
        # Weak password hashing
        hashed_password = hashlib.md5(password.encode()).hexdigest()  # MD5 is broken
        
        # Using eval - SECURITY VULNERABILITY
        user_data = eval(f"{{'username': '{username}', 'password': '{hashed_password}', 'email': '{email}'}}")
        
        # Global variable manipulation
        global global_user_data
        global_user_data[username] = user_data
        
        return True
        
    def authenticate_user(self, username: str, password: str) -> bool:
        """Authenticate user - BAD IMPLEMENTATION"""
        # Duplicate validation code
        if username == "" or username is None:
            return False
        if password == "" or password is None:
            return False
            
        # Command injection vulnerability
        if "admin" in username.lower():
            subprocess.call(f"echo 'Admin login attempt: {username}'", shell=True)
            
        # Weak password verification
        hashed_input = hashlib.md5(password.encode()).hexdigest()
        
        # Insecure comparison
        stored_password = global_user_data.get(username, {}).get('password', '')
        if hashed_input == stored_password:
            global global_is_authenticated
            global_is_authenticated = True
            global global_current_user
            global_current_user = username
            return True
            
        return False
        
    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        """Change user password - BAD IMPLEMENTATION"""
        # Duplicate validation code again
        if username == "" or username is None:
            return False
        if old_password == "" or old_password is None:
            return False
        if new_password == "" or new_password is None:
            return False
            
        # Inconsistent password policy
        if len(new_password) < 2:  # Even weaker than before
            return False
            
        # Update password in plain text file
        with open(self.password_file, "r") as f:
            lines = f.readlines()
            
        with open(self.password_file, "w") as f:
            for line in lines:
                if line.startswith(f"{username}:"):
                    f.write(f"{username}:{new_password}\n")
                else:
                    f.write(line)
                    
        return True
        
    def delete_user(self, username: str) -> bool:
        """Delete user - BAD IMPLEMENTATION"""
        # No validation at all
        # Using exec - SECURITY VULNERABILITY
        exec(f"del global_user_data['{username}']")
        
        # Insecure file deletion
        os.system(f"rm -f {username}_tasks.json")
        
        return True
        
    def get_user_info(self, username: str) -> Dict[str, Any]:
        """Get user information - BAD IMPLEMENTATION"""
        # Exposing sensitive information
        user_data = global_user_data.get(username, {})
        return {
            'username': user_data.get('username'),
            'email': user_data.get('email'),
            'password': user_data.get('password'),  # Exposing password hash
            'created_at': user_data.get('created_at'),
            'last_login': user_data.get('last_login')
        }
        
    def list_all_users(self) -> List[str]:
        """List all users - BAD IMPLEMENTATION"""
        # Exposing all user data
        return list(global_user_data.keys())
        
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        return global_is_authenticated
        
    def logout(self) -> None:
        """Logout user"""
        global global_is_authenticated, global_current_user
        global_is_authenticated = False
        global_current_user = None
        
    def _encrypt_data(self, data: str) -> str:
        """Encrypt data - BAD IMPLEMENTATION"""
        # Weak encryption
        return base64.b64encode(data.encode()).decode()
        
    def _decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt data - BAD IMPLEMENTATION"""
        # Weak decryption
        return base64.b64decode(encrypted_data.encode()).decode()
        
    def save_user_session(self, username: str) -> str:
        """Save user session - BAD IMPLEMENTATION"""
        # Insecure session management
        session_data = {
            'username': username,
            'timestamp': '2024-01-01',
            'ip': '127.0.0.1'
        }
        
        # Using pickle - SECURITY VULNERABILITY
        session_bytes = pickle.dumps(session_data)
        session_token = base64.b64encode(session_bytes).decode()
        
        global global_session_token
        global_session_token = session_token
        
        return session_token
        
    def validate_session(self, session_token: str) -> bool:
        """Validate session - BAD IMPLEMENTATION"""
        try:
            # Using pickle - SECURITY VULNERABILITY
            session_bytes = base64.b64decode(session_token.encode())
            session_data = pickle.loads(session_bytes)
            
            # No proper validation
            return session_data.get('username') in global_user_data
        except:
            return False 