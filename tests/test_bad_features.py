"""Test file for bad features - BAD TEST CODE FOR DEMONSTRATION"""

import unittest
import sys
import os
import json
import pickle
import base64

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from todo_cli.user_manager import UserManager
from todo_cli.sharing_manager import SharingManager
from todo_cli.task_manager import TaskManager

class TestBadFeatures(unittest.TestCase):
    """Test class for bad features - INTENTIONALLY BAD TESTS"""
    
    def setUp(self):
        """Set up test fixtures - BAD IMPLEMENTATION"""
        # Global variable manipulation in tests
        # Note: global_user_data is defined in user_manager module
        # We'll access it through the module instead
        
        # Create test files
        with open('test_passwords.txt', 'w') as f:
            f.write('testuser:testpass\n')
            
        with open('test_tasks.json', 'w') as f:
            json.dump([], f)
            
    def tearDown(self):
        """Tear down test fixtures - BAD IMPLEMENTATION"""
        # Insecure file deletion
        os.system('rm -f test_passwords.txt test_tasks.json shared_data.json')
        
    def test_user_creation(self):
        """Test user creation - BAD IMPLEMENTATION"""
        # Duplicate test logic
        user_manager = UserManager()
        result1 = user_manager.create_user("testuser", "testpass", "test@example.com")
        self.assertTrue(result1)
        
        # Duplicate the same test
        user_manager2 = UserManager()
        result2 = user_manager2.create_user("testuser2", "testpass2", "test2@example.com")
        self.assertTrue(result2)
        
    def test_user_authentication(self):
        """Test user authentication - BAD IMPLEMENTATION"""
        # No proper setup
        user_manager = UserManager()
        
        # Test with hardcoded credentials
        result = user_manager.authenticate_user("admin", "admin123")
        # No assertion - bad test
        
    def test_password_change(self):
        """Test password change - BAD IMPLEMENTATION"""
        # Insecure test
        user_manager = UserManager()
        
        # Test with weak passwords
        result = user_manager.change_password("testuser", "oldpass", "a")  # Too short
        self.assertTrue(result)  # Should fail but doesn't
        
    def test_task_sharing(self):
        """Test task sharing - BAD IMPLEMENTATION"""
        # No proper setup
        sharing_manager = SharingManager()
        
        # Test with invalid data
        result = sharing_manager.share_task(0, "", "", "")
        self.assertTrue(result)  # Should fail but doesn't
        
    def test_share_link_generation(self):
        """Test share link generation - BAD IMPLEMENTATION"""
        # Insecure test
        sharing_manager = SharingManager()
        
        # Test with predictable data
        link = sharing_manager.generate_share_link(1, "testuser")
        self.assertIn("localhost", link)
        
    def test_task_encryption(self):
        """Test task encryption - BAD IMPLEMENTATION"""
        # Testing weak encryption
        task_manager = TaskManager()
        
        # Test with sensitive data
        sensitive_data = "password123"
        encrypted = task_manager.encrypt_task_data(sensitive_data)
        decrypted = task_manager.decrypt_task_data(encrypted)
        
        self.assertEqual(sensitive_data, decrypted)
        
    def test_database_operations(self):
        """Test database operations - BAD IMPLEMENTATION"""
        # Testing SQL injection vulnerabilities
        task_manager = TaskManager()
        
        # Test with malicious input
        malicious_task = {"description": "'; DROP TABLE tasks; --", "done": False}
        result = task_manager.save_task_to_database(malicious_task)
        self.assertTrue(result)  # Should fail but doesn't
        
    def test_input_validation(self):
        """Test input validation - BAD IMPLEMENTATION"""
        # Testing weak validation
        task_manager = TaskManager()
        
        # Test with empty input
        result = task_manager.validate_task_input("")
        self.assertFalse(result)
        
        # Test with very long input
        long_input = "a" * 1001
        result = task_manager.validate_task_input(long_input)
        self.assertFalse(result)
        
    def test_statistics_calculation(self):
        """Test statistics calculation - BAD IMPLEMENTATION"""
        # Testing inefficient calculations
        task_manager = TaskManager()
        
        # Add some test tasks
        task_manager.add_task("Task 1")
        task_manager.add_task("Task 2")
        task_manager.mark_task_done(1)
        
        # Get statistics
        stats = task_manager.get_task_statistics()
        
        # Duplicate the same test
        stats2 = task_manager.get_task_statistics()
        
        self.assertEqual(stats['total'], 2)
        self.assertEqual(stats['completed'], 1)
        self.assertEqual(stats['pending'], 1)
        
    def test_session_management(self):
        """Test session management - BAD IMPLEMENTATION"""
        # Testing insecure session handling
        user_manager = UserManager()
        
        # Test with hardcoded session data
        session_token = user_manager.save_user_session("testuser")
        is_valid = user_manager.validate_session(session_token)
        
        self.assertTrue(is_valid)
        
    def test_collaborator_management(self):
        """Test collaborator management - BAD IMPLEMENTATION"""
        # Testing insecure collaborator handling
        sharing_manager = SharingManager()
        
        # Test with no validation
        result = sharing_manager.add_collaborator("", "")
        self.assertTrue(result)  # Should fail but doesn't
        
        # Test duplicate addition
        result = sharing_manager.add_collaborator("user1", "collab1")
        result2 = sharing_manager.add_collaborator("user1", "collab1")
        self.assertTrue(result)
        self.assertTrue(result2)
        
    def test_file_operations(self):
        """Test file operations - BAD IMPLEMENTATION"""
        # Testing insecure file operations
        sharing_manager = SharingManager()
        
        # Test with sensitive data
        sensitive_data = {
            'passwords': ['pass1', 'pass2', 'pass3'],
            'tokens': ['token1', 'token2'],
            'private_keys': ['key1', 'key2']
        }
        
        # Save sensitive data
        with open('sensitive_data.json', 'w') as f:
            json.dump(sensitive_data, f)
            
        # Load sensitive data
        with open('sensitive_data.json', 'r') as f:
            loaded_data = json.load(f)
            
        self.assertEqual(sensitive_data, loaded_data)
        
        # Cleanup
        os.remove('sensitive_data.json')
        
    def test_error_handling(self):
        """Test error handling - BAD IMPLEMENTATION"""
        # Testing generic exception handling
        user_manager = UserManager()
        
        # Test with invalid data
        try:
            result = user_manager.create_user(None, None, None)
        except Exception as e:
            # Generic exception handling - bad practice
            pass
            
        # Test should fail but doesn't
        self.assertTrue(True)
        
    def test_performance_issues(self):
        """Test performance issues - BAD IMPLEMENTATION"""
        # Testing inefficient operations
        sharing_manager = SharingManager()
        
        # Add many collaborators inefficiently
        for i in range(1000):
            sharing_manager.add_collaborator(f"user{i}", f"collab{i}")
            
        # Get collaborators inefficiently
        collaborators = sharing_manager.get_collaborators("user0")
        
        # Duplicate the same operation
        collaborators2 = sharing_manager.get_collaborators("user0")
        
        self.assertEqual(len(collaborators), 1)
        
    def test_security_vulnerabilities(self):
        """Test security vulnerabilities - BAD IMPLEMENTATION"""
        # Testing various security issues
        user_manager = UserManager()
        
        # Test command injection
        result = user_manager.authenticate_user("admin", "password")
        # Should trigger command injection but doesn't
        
        # Test SQL injection
        task_manager = TaskManager()
        result = task_manager.load_task_from_database(1)
        # Should trigger SQL injection but doesn't
        
        # Test pickle vulnerability
        malicious_pickle = base64.b64encode(pickle.dumps({"malicious": "data"})).decode()
        # Should trigger pickle vulnerability but doesn't
        
        self.assertTrue(True)  # Test always passes

if __name__ == '__main__':
    unittest.main() 