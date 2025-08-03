"""
Task Manager Module

Handles task operations including loading, saving, adding, listing,
and marking tasks as done.
"""

import json
import os
from typing import Any, Dict, List


class TaskManager:
    """Manages to-do tasks with persistent storage."""

    def __init__(self, data_file: str = "tasks.json"):
        """
        Initialize TaskManager with specified data file.

        Args:
            data_file (str): Path to the JSON file for storing tasks
        """
        self.data_file = data_file
        self.tasks = self._load_tasks()

    def _load_tasks(self) -> List[Dict[str, Any]]:
        """
        Load tasks from the JSON file.

        Returns:
            List[Dict[str, Any]]: List of task dictionaries
        """
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    # Ensure backward compatibility
                    if isinstance(data, list):
                        return data
                    return []
            return []
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load tasks from {self.data_file}: {e}")
            return []

    def _save_tasks(self) -> None:
        """Save tasks to the JSON file."""
        try:
            with open(self.data_file, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=2, ensure_ascii=False)
        except IOError as e:
            print(f"Error: Could not save tasks to {self.data_file}: {e}")
            raise

    def add_task(self, description: str) -> None:
        """
        Add a new task to the to-do list.

        Args:
            description (str): Description of the task to add

        Raises:
            ValueError: If description is empty or only whitespace
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        task = {"description": description.strip(), "done": False}
        self.tasks.append(task)
        self._save_tasks()
        print(f"Task added: {description.strip()}")

    def list_tasks(self) -> None:
        """List all tasks with their completion status."""
        if not self.tasks:
            print("No tasks found. Add some tasks to get started!")
            return

        print("Your to-do list:")
        for index, task in enumerate(self.tasks, 1):
            status_icon = "✔️" if task["done"] else "❌"
            print(f"{index}. [{status_icon}] {task['description']}")

    def mark_task_done(self, task_index: int) -> None:
        """
        Mark a task as done by its index.

        Args:
            task_index (int): 1-based index of the task to mark as done

        Raises:
            ValueError: If task_index is invalid
        """
        if not self.tasks:
            raise ValueError("No tasks available to mark as done")

        if task_index < 1 or task_index > len(self.tasks):
            raise ValueError(
                f"Invalid task index. Please choose a number between 1 and "
                f"{len(self.tasks)}"
            )

        # Convert to 0-based index
        array_index = task_index - 1

        if self.tasks[array_index]["done"]:
            print(f"Task {task_index} is already marked as done")
            return

        self.tasks[array_index]["done"] = True
        self._save_tasks()
        print(
            f"Task {task_index} marked as done: "
            f"{self.tasks[array_index]['description']}"
        )

    def get_task_count(self) -> Dict[str, int]:
        """
        Get count of total, completed, and pending tasks.

        Returns:
            Dict[str, int]: Dictionary with counts
        """
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task["done"])
        pending = total - completed

        return {"total": total, "completed": completed, "pending": pending}

    def remove_task(self, task_index: int) -> None:
        """
        Remove a task by its index.

        Args:
            task_index (int): 1-based index of the task to remove

        Raises:
            ValueError: If task_index is invalid
        """
        if not self.tasks:
            raise ValueError("No tasks available to remove")

        if task_index < 1 or task_index > len(self.tasks):
            raise ValueError(
                f"Invalid task index. Please choose a number between 1 and "
                f"{len(self.tasks)}"
            )

        # Convert to 0-based index
        array_index = task_index - 1
        removed_task = self.tasks.pop(array_index)
        self._save_tasks()
        print(f"Task {task_index} removed: {removed_task['description']}")
