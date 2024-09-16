import argparse

from Utils.enums import Command
from storage import Storage
from task_manager import TaskManager


def main():
    storage = Storage()
    manager = TaskManager(storage)

    parser = argparse.ArgumentParser(description="Task Management System")
    subparsers = parser.add_subparsers(dest="command",
                                       help="Available commands")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("description", help="Task description")

    # Complete task
    complete_parser = subparsers.add_parser("complete",
                                            help="Mark a task as completed")
    complete_parser.add_argument("title", help="Task title")

    # List tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--all",
                             action="store_true",
                             help="Include completed tasks")

    # Generate report
    subparsers.add_parser("report", help="Generate a report")

    args = parser.parse_args()

    if args.command == Command.ADD:
        task = manager.add_task(args.title, args.description)
        print(f"Task '{task.title}' added successfully.")
    elif args.command == Command.COMPLETE:
        if manager.complete_task(args.title):
            print(f"Task '{args.title}' marked as completed.")
        else:
            print(f"Task '{args.title}' not found.")
    elif args.command == Command.LIST:
        tasks = manager.list_tasks(include_completed=args.all)
        if tasks:
            for task in tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"{task.title} - {status}")
        else:
            print("No tasks found.")
    elif args.command == Command.REPORT:
        print(manager.generate_report())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
