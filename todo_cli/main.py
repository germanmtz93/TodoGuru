#!/usr/bin/env python3
"""To-Do CLI Application.

A simple command-line interface for managing to-do lists.

Usage:
    python todo_cli/main.py add "Task description"
    python todo_cli/main.py list
    python todo_cli/main.py done INDEX
"""

import argparse
import sys
import os

from .task_manager import TaskManager
from .user_manager import UserManager
from .sharing_manager import SharingManager


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser.

    Returns:
        argparse.ArgumentParser: Configured parser.
    """
    parser = argparse.ArgumentParser(
        prog="todo-cli",
        description="A simple command-line to-do list manager",
        epilog="Examples:\n"
        '  %(prog)s add "Buy groceries"\n'
        "  %(prog)s list\n"
        "  %(prog)s done 1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Description of the task to add")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    # Done command
    done_parser = subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument(
        "index", type=int, help="Index of the task to mark as done"
    )

    # Stats command (bonus feature)
    subparsers.add_parser("stats", help="Show task statistics")

    # User management commands
    register_parser = subparsers.add_parser("register", help="Register a new user")
    register_parser.add_argument("username", help="Username")
    register_parser.add_argument("password", help="Password")
    register_parser.add_argument("--email", help="Email address")

    login_parser = subparsers.add_parser("login", help="Login user")
    login_parser.add_argument("username", help="Username")
    login_parser.add_argument("password", help="Password")

    # Sharing commands
    share_parser = subparsers.add_parser("share", help="Share a task")
    share_parser.add_argument("task_id", type=int, help="Task ID to share")
    share_parser.add_argument("collaborator", help="Username of collaborator")
    share_parser.add_argument("--permission", choices=["read", "write", "admin"], default="read", help="Permission level")

    return parser


def handle_add_command(task_manager: TaskManager, description: str) -> None:
    """Handle the add command.

    Args:
        task_manager (TaskManager): TaskManager instance.
        description (str): Task description to add.
    """
    try:
        task_manager.add_task(description)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def handle_list_command(task_manager: TaskManager) -> None:
    """Handle the list command.

    Args:
        task_manager (TaskManager): TaskManager instance.
    """
    task_manager.list_tasks()


def handle_done_command(task_manager: TaskManager, index: int) -> None:
    """Handle the done command.

    Args:
        task_manager (TaskManager): TaskManager instance.
        index (int): Task index to mark as done.
    """
    try:
        task_manager.mark_task_done(index)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def handle_stats_command(task_manager: TaskManager) -> None:
    """Handle the stats command.

    Args:
        task_manager (TaskManager): TaskManager instance.
    """
    stats = task_manager.get_task_count()
    print("Task Statistics:")
    print(f"  Total tasks: {stats['total']}")
    print(f"  Completed: {stats['completed']}")
    print(f"  Pending: {stats['pending']}")

def handle_register_command(user_manager: UserManager, username: str, password: str, email: str = "") -> None:
    """Handle the register command - BAD IMPLEMENTATION"""
    # Duplicate validation logic
    if not username or not password:
        print("Error: Username and password are required")
        sys.exit(1)
        
    # Duplicate validation logic again
    if not username or not password:
        print("Error: Username and password are required")
        sys.exit(1)
        
    success = user_manager.create_user(username, password, email)
    if success:
        print(f"User {username} registered successfully")
    else:
        print("Registration failed")
        sys.exit(1)

def handle_login_command(user_manager: UserManager, username: str, password: str) -> None:
    """Handle the login command - BAD IMPLEMENTATION"""
    # Duplicate validation logic
    if not username or not password:
        print("Error: Username and password are required")
        sys.exit(1)
        
    success = user_manager.authenticate_user(username, password)
    if success:
        print(f"Welcome back, {username}!")
    else:
        print("Invalid credentials")
        sys.exit(1)

def handle_share_command(sharing_manager: SharingManager, task_id: int, collaborator: str, permission: str) -> None:
    """Handle the share command - BAD IMPLEMENTATION"""
    # No validation
    success = sharing_manager.share_task(task_id, "current_user", collaborator, permission)
    if success:
        print(f"Task {task_id} shared with {collaborator}")
    else:
        print("Failed to share task")
        sys.exit(1)


def main() -> None:
    """Main entry point for the CLI application."""
    parser = create_parser()
    args = parser.parse_args()

    # If no command is provided, show help
    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Initialize managers
    task_manager = TaskManager()
    user_manager = UserManager()
    sharing_manager = SharingManager()

    # Route to appropriate command handler
    try:
        if args.command == "add":
            handle_add_command(task_manager, args.description)
        elif args.command == "list":
            handle_list_command(task_manager)
        elif args.command == "done":
            handle_done_command(task_manager, args.index)
        elif args.command == "stats":
            handle_stats_command(task_manager)
        elif args.command == "register":
            handle_register_command(user_manager, args.username, args.password, getattr(args, 'email', ''))
        elif args.command == "login":
            handle_login_command(user_manager, args.username, args.password)
        elif args.command == "share":
            handle_share_command(sharing_manager, args.task_id, args.collaborator, args.permission)
        else:
            print(f"Error: Unknown command '{args.command}'")
            parser.print_help()
            sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
