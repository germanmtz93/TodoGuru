"""
Unit tests for the TaskManager class.
"""

import unittest
import tempfile
import os
import json
from unittest.mock import patch, mock_open
from todo_cli.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """Test cases for TaskManager class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        # Initialize with empty JSON array to avoid parsing errors
        self.temp_file.write('[]')
        self.temp_file.close()
        self.task_manager = TaskManager(self.temp_file.name)
    
    def tearDown(self):
        """Clean up after each test method."""
        # Remove the temporary file
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_init_with_existing_file(self):
        """Test TaskManager initialization with existing file."""
        # Write test data to file
        test_tasks = [
            {"description": "Test task 1", "done": False},
            {"description": "Test task 2", "done": True}
        ]
        with open(self.temp_file.name, 'w') as f:
            json.dump(test_tasks, f)
        
        # Initialize TaskManager
        tm = TaskManager(self.temp_file.name)
        self.assertEqual(len(tm.tasks), 2)
        self.assertEqual(tm.tasks[0]["description"], "Test task 1")
        self.assertFalse(tm.tasks[0]["done"])
        self.assertTrue(tm.tasks[1]["done"])
    
    def test_init_with_nonexistent_file(self):
        """Test TaskManager initialization with non-existent file."""
        non_existent_file = "non_existent_file.json"
        tm = TaskManager(non_existent_file)
        self.assertEqual(len(tm.tasks), 0)
    
    def test_init_with_corrupted_file(self):
        """Test TaskManager initialization with corrupted JSON file."""
        # Write invalid JSON to file
        with open(self.temp_file.name, 'w') as f:
            f.write("invalid json content")
        
        with patch('builtins.print') as mock_print:
            tm = TaskManager(self.temp_file.name)
            self.assertEqual(len(tm.tasks), 0)
            mock_print.assert_called()
    
    def test_add_task_success(self):
        """Test successful task addition."""
        with patch('builtins.print') as mock_print:
            self.task_manager.add_task("Test task")
            mock_print.assert_called_with("Task added: Test task")
        
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0]["description"], "Test task")
        self.assertFalse(self.task_manager.tasks[0]["done"])
    
    def test_add_task_empty_description(self):
        """Test task addition with empty description."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.add_task("")
        self.assertIn("Task description cannot be empty", str(context.exception))
        
        with self.assertRaises(ValueError):
            self.task_manager.add_task("   ")  # Only whitespace
    
    def test_add_task_strips_whitespace(self):
        """Test that task addition strips leading/trailing whitespace."""
        with patch('builtins.print'):
            self.task_manager.add_task("  Test task  ")
        
        self.assertEqual(self.task_manager.tasks[0]["description"], "Test task")
    
    def test_list_tasks_empty(self):
        """Test listing tasks when no tasks exist."""
        with patch('builtins.print') as mock_print:
            self.task_manager.list_tasks()
            mock_print.assert_called_with("No tasks found. Add some tasks to get started!")
    
    def test_list_tasks_with_tasks(self):
        """Test listing tasks when tasks exist."""
        # Add test tasks
        self.task_manager.tasks = [
            {"description": "Task 1", "done": False},
            {"description": "Task 2", "done": True}
        ]
        
        with patch('builtins.print') as mock_print:
            self.task_manager.list_tasks()
            
            # Check that print was called with expected output
            calls = mock_print.call_args_list
            self.assertEqual(calls[0][0][0], "Your to-do list:")
            self.assertIn("1. [❌] Task 1", calls[1][0][0])
            self.assertIn("2. [✔️] Task 2", calls[2][0][0])
    
    def test_mark_task_done_success(self):
        """Test successfully marking a task as done."""
        # Add a test task
        self.task_manager.tasks = [{"description": "Test task", "done": False}]
        
        with patch('builtins.print') as mock_print:
            self.task_manager.mark_task_done(1)
            mock_print.assert_called_with("Task 1 marked as done: Test task")
        
        self.assertTrue(self.task_manager.tasks[0]["done"])
    
    def test_mark_task_done_already_done(self):
        """Test marking an already completed task as done."""
        # Add a completed test task
        self.task_manager.tasks = [{"description": "Test task", "done": True}]
        
        with patch('builtins.print') as mock_print:
            self.task_manager.mark_task_done(1)
            mock_print.assert_called_with("Task 1 is already marked as done")
    
    def test_mark_task_done_invalid_index(self):
        """Test marking task as done with invalid index."""
        self.task_manager.tasks = [{"description": "Test task", "done": False}]
        
        with self.assertRaises(ValueError) as context:
            self.task_manager.mark_task_done(0)  # Invalid: too low
        self.assertIn("Invalid task index", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            self.task_manager.mark_task_done(2)  # Invalid: too high
        self.assertIn("Invalid task index", str(context.exception))
    
    def test_mark_task_done_empty_list(self):
        """Test marking task as done when no tasks exist."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.mark_task_done(1)
        self.assertIn("No tasks available to mark as done", str(context.exception))
    
    def test_get_task_count(self):
        """Test getting task count statistics."""
        # Test empty list
        stats = self.task_manager.get_task_count()
        self.assertEqual(stats["total"], 0)
        self.assertEqual(stats["completed"], 0)
        self.assertEqual(stats["pending"], 0)
        
        # Add test tasks
        self.task_manager.tasks = [
            {"description": "Task 1", "done": False},
            {"description": "Task 2", "done": True},
            {"description": "Task 3", "done": False}
        ]
        
        stats = self.task_manager.get_task_count()
        self.assertEqual(stats["total"], 3)
        self.assertEqual(stats["completed"], 1)
        self.assertEqual(stats["pending"], 2)
    
    def test_remove_task_success(self):
        """Test successfully removing a task."""
        self.task_manager.tasks = [
            {"description": "Task 1", "done": False},
            {"description": "Task 2", "done": True}
        ]
        
        with patch('builtins.print') as mock_print:
            self.task_manager.remove_task(1)
            mock_print.assert_called_with("Task 1 removed: Task 1")
        
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0]["description"], "Task 2")
    
    def test_remove_task_invalid_index(self):
        """Test removing task with invalid index."""
        self.task_manager.tasks = [{"description": "Test task", "done": False}]
        
        with self.assertRaises(ValueError) as context:
            self.task_manager.remove_task(0)  # Invalid: too low
        self.assertIn("Invalid task index", str(context.exception))
        
        with self.assertRaises(ValueError) as context:
            self.task_manager.remove_task(2)  # Invalid: too high
        self.assertIn("Invalid task index", str(context.exception))
    
    def test_remove_task_empty_list(self):
        """Test removing task when no tasks exist."""
        with self.assertRaises(ValueError) as context:
            self.task_manager.remove_task(1)
        self.assertIn("No tasks available to remove", str(context.exception))
    
    def test_persistence(self):
        """Test that tasks are properly saved and loaded."""
        # Add a task
        with patch('builtins.print'):
            self.task_manager.add_task("Persistent task")
        
        # Create a new TaskManager instance with the same file
        new_tm = TaskManager(self.temp_file.name)
        
        # Verify the task was loaded
        self.assertEqual(len(new_tm.tasks), 1)
        self.assertEqual(new_tm.tasks[0]["description"], "Persistent task")
        self.assertFalse(new_tm.tasks[0]["done"])
    
    @patch('builtins.open', mock_open())
    def test_save_tasks_io_error(self):
        """Test handling of IO errors during save."""
        with patch('builtins.open', side_effect=IOError("Permission denied")):
            with self.assertRaises(IOError):
                self.task_manager._save_tasks()


if __name__ == '__main__':
    unittest.main()
