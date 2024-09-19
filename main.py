import argparse

from Utils.enums import Command, Status
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

    # Start task
    start_parser = subparsers.add_parser("start",
                                            help="start a task")
    start_parser.add_argument("title", help="Task title")

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
        if task:
            print(f"Task '{task.title}' added successfully.")
        else:
            print(f"We have a task with the title of '{args.title}'. Please change the title if you want to add a "
                  f"different task")



    elif args.command == Command.COMPLETE:
        status=manager.complete_task(args.title)
        if status == Status.COMPLETE:
            print(f"Task '{args.title}' marked as completed.")
        elif status == Status.NOT_FOUND:
            print(f"Task '{args.title}' not found.")
        else:
            print(f"Task '{args.title}' not started yet")


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

    elif args.command == Command.START:
        manager.start_task(args.title)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
