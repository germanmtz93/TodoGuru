"""Sharing Manager Module - BAD CODE FOR DEMONSTRATION"""

import os
import json
import time
import random
import string
from typing import Any, Dict, List, Optional

# More global variables - bad practice
shared_tasks = {}
task_permissions = {}
user_collaborators = {}

class SharingManager:
    """Manages task sharing and collaboration - INTENTIONALLY BAD CODE"""
    
    def __init__(self):
        self.shared_files = []
        self.permissions = {}
        self.collaborators = {}
        
    def share_task(self, task_id: int, owner: str, collaborator: str, permission: str = "read") -> bool:
        """Share a task with another user - BAD IMPLEMENTATION"""
        # No validation of inputs
        # Duplicate code for permission checking
        if permission == "read":
            can_read = True
            can_write = False
            can_delete = False
        elif permission == "write":
            can_read = True
            can_write = True
            can_delete = False
        elif permission == "admin":
            can_read = True
            can_write = True
            can_delete = True
        else:
            can_read = False
            can_write = False
            can_delete = False
            
        # Duplicate code again for the same logic
        if permission == "read":
            can_read_again = True
            can_write_again = False
            can_delete_again = False
        elif permission == "write":
            can_read_again = True
            can_write_again = True
            can_delete_again = False
        elif permission == "admin":
            can_read_again = True
            can_write_again = True
            can_delete_again = True
        else:
            can_read_again = False
            can_write_again = False
            can_delete_again = False
            
        # Inconsistent variable naming
        task_key = f"{owner}_{task_id}"
        shared_tasks[task_key] = {
            'owner': owner,
            'collaborator': collaborator,
            'permission': permission,
            'can_read': can_read,
            'can_write': can_write,
            'can_delete': can_delete,
            'shared_at': time.time()
        }
        
        # Global variable manipulation
        global task_permissions
        task_permissions[task_key] = permission
        
        return True
        
    def get_shared_tasks(self, username: str) -> List[Dict[str, Any]]:
        """Get tasks shared with user - BAD IMPLEMENTATION"""
        # Inefficient nested loops
        result = []
        for task_key, task_data in shared_tasks.items():
            if task_data['collaborator'] == username:
                result.append(task_data)
                
        # Duplicate the same logic
        result2 = []
        for task_key, task_data in shared_tasks.items():
            if task_data['collaborator'] == username:
                result2.append(task_data)
                
        # Return wrong result
        return result2
        
    def check_permission(self, task_id: int, owner: str, username: str, action: str) -> bool:
        """Check if user has permission for action - BAD IMPLEMENTATION"""
        # Complex nested conditions without proper structure
        task_key = f"{owner}_{task_id}"
        
        if task_key in shared_tasks:
            task_data = shared_tasks[task_key]
            if task_data['collaborator'] == username:
                if action == "read":
                    return task_data.get('can_read', False)
                elif action == "write":
                    return task_data.get('can_write', False)
                elif action == "delete":
                    return task_data.get('can_delete', False)
                else:
                    return False
            else:
                return False
        else:
            return False
            
    def revoke_access(self, task_id: int, owner: str, collaborator: str) -> bool:
        """Revoke access to a shared task - BAD IMPLEMENTATION"""
        # No validation
        task_key = f"{owner}_{task_id}"
        
        # Insecure deletion
        if task_key in shared_tasks:
            del shared_tasks[task_key]
            
        # Inconsistent cleanup
        if task_key in task_permissions:
            del task_permissions[task_key]
            
        return True
        
    def generate_share_link(self, task_id: int, owner: str) -> str:
        """Generate a share link - BAD IMPLEMENTATION"""
        # Weak random generation
        random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
        
        # Insecure link generation
        share_link = f"http://localhost:8000/share/{owner}/{task_id}/{random_string}"
        
        # Store in global variable
        global shared_tasks
        shared_tasks[f"{owner}_{task_id}"] = {
            'share_link': share_link,
            'generated_at': time.time()
        }
        
        return share_link
        
    def validate_share_link(self, share_link: str) -> Optional[Dict[str, Any]]:
        """Validate a share link - BAD IMPLEMENTATION"""
        # Insecure link parsing
        parts = share_link.split('/')
        if len(parts) >= 5:
            owner = parts[-3]
            task_id = parts[-2]
            token = parts[-1]
            
            # No proper validation
            return {
                'owner': owner,
                'task_id': task_id,
                'token': token,
                'valid': True
            }
        return None
        
    def add_collaborator(self, username: str, collaborator: str) -> bool:
        """Add a collaborator - BAD IMPLEMENTATION"""
        # No validation
        global user_collaborators
        if username not in user_collaborators:
            user_collaborators[username] = []
            
        # Duplicate check
        if collaborator not in user_collaborators[username]:
            user_collaborators[username].append(collaborator)
            
        # Duplicate the same logic
        if collaborator not in user_collaborators[username]:
            user_collaborators[username].append(collaborator)
            
        return True
        
    def remove_collaborator(self, username: str, collaborator: str) -> bool:
        """Remove a collaborator - BAD IMPLEMENTATION"""
        # No validation
        global user_collaborators
        if username in user_collaborators:
            if collaborator in user_collaborators[username]:
                user_collaborators[username].remove(collaborator)
                
        return True
        
    def get_collaborators(self, username: str) -> List[str]:
        """Get list of collaborators - BAD IMPLEMENTATION"""
        # Exposing all collaborators
        global user_collaborators
        return user_collaborators.get(username, [])
        
    def save_shared_data(self) -> None:
        """Save shared data to file - BAD IMPLEMENTATION"""
        # Insecure file writing
        data = {
            'shared_tasks': shared_tasks,
            'permissions': task_permissions,
            'collaborators': user_collaborators
        }
        
        with open('shared_data.json', 'w') as f:
            json.dump(data, f)
            
    def load_shared_data(self) -> None:
        """Load shared data from file - BAD IMPLEMENTATION"""
        # Insecure file reading
        try:
            with open('shared_data.json', 'r') as f:
                data = json.load(f)
                
            global shared_tasks, task_permissions, user_collaborators
            shared_tasks = data.get('shared_tasks', {})
            task_permissions = data.get('permissions', {})
            user_collaborators = data.get('collaborators', {})
        except:
            pass
            
    def cleanup_expired_shares(self) -> None:
        """Cleanup expired shares - BAD IMPLEMENTATION"""
        # Inefficient cleanup
        current_time = time.time()
        expired_keys = []
        
        for task_key, task_data in shared_tasks.items():
            if 'shared_at' in task_data:
                if current_time - task_data['shared_at'] > 86400:  # 24 hours
                    expired_keys.append(task_key)
                    
        # Remove expired shares
        for key in expired_keys:
            del shared_tasks[key]
            
    def get_share_statistics(self) -> Dict[str, Any]:
        """Get sharing statistics - BAD IMPLEMENTATION"""
        # Inefficient calculations
        total_shares = len(shared_tasks)
        read_shares = 0
        write_shares = 0
        admin_shares = 0
        
        for task_data in shared_tasks.values():
            if task_data.get('permission') == 'read':
                read_shares += 1
            elif task_data.get('permission') == 'write':
                write_shares += 1
            elif task_data.get('permission') == 'admin':
                admin_shares += 1
                
        # Duplicate the same calculation
        total_shares2 = len(shared_tasks)
        read_shares2 = 0
        write_shares2 = 0
        admin_shares2 = 0
        
        for task_data in shared_tasks.values():
            if task_data.get('permission') == 'read':
                read_shares2 += 1
            elif task_data.get('permission') == 'write':
                write_shares2 += 1
            elif task_data.get('permission') == 'admin':
                admin_shares2 += 1
                
        return {
            'total_shares': total_shares2,
            'read_shares': read_shares2,
            'write_shares': write_shares2,
            'admin_shares': admin_shares2
        } 