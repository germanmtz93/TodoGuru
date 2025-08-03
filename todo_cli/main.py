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

from .task_manager import TaskManager


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


def main() -> None:
    """Main entry point for the CLI application."""
    parser = create_parser()
    args = parser.parse_args()

    # If no command is provided, show help
    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Initialize task manager
    task_manager = TaskManager()

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
