# 1 . Please pull the  `task_manager_with_json_db` branch

# My Assumptions
- As this is a small app for personal task management, I decided not to use a database. Instead, I am persisting the data in a file named `db.json`, as I didn’t want to use a sledgehammer to crack a nut.
- After reviewing the entire codebase, I opted for a TDD approach, maintaining the same test cases for this version.
- Since the add command adds tasks with a title and description, the title should be unique. 
- There is no command for starting a task, so I suggest introducing a new command called `start`. 
- To generate the report, which requires the average time to complete tasks, I propose adding `start_time` and `end_time` fields. Initially, both will be set to None. When a task is started using its title, the `start_time` will be updated accordingly





# Task Management System

This is a simple command-line (CLI) task management system implemented in Python.

## Functional Requirements

The application should allow users to do the following:

1. Add a new task
2. Complete a task
3. List all tasks (with an option to show only incomplete tasks)
4. Generate a report of task statistics, which should include:
   - Total number of tasks
   - Number of completed tasks
   - Number of pending tasks
   - Average time taken to complete a task (*business for this is not clear*)
5. The application must persist user data across sessions, ensuring that all information remains intact and accessible upon returning, without resetting or losing any previously entered tasks

## Setup

1. Ensure you have Python 3.7 or higher installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Install Poetry if you don't have it installed:
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
5. Install dependencies
    ```
    poetry install
    ```
6.  Running the application
    ```
    poetry run python main.py
    ```

## Running Tests

To run all the unit tests, use the following command:

```
python -m unittest discover tests
```

## Your Task

**Ensure and validate with tests that the app meets the required functionality** and addresses any bugs. Enhance performance and do optimisations to the best of your knowledge, while refactoring the code for better readability and maintainability. Feel free to make necessary assumptions where applicable.

## Submission

Once you are done, please:

1. Push your code to a **public** GitHub repository with at least **read** access
2. Reply to our email with the repository link to complete your submission within the deadline

Good luck!

# my plan






## Add task
- [X] Since task title is the unique identifier for the cli application.
  - [X] we can keep title unique in the database(lets go this path assuming it's a cli for personal use).
    - [ ] we can do it in database level making the title column unique.
    - [X] we can do an extra query to check if the task exist in the database. 
  - [ ] Or we can keep consider this as a daily tasker and if the previously entered task is completed we will let user input task with same title.
    - if we consider this path:
      - The title column should not be marked as unique.
      - An additional query will be required to check if an incomplete task with the same title already exists in the database.
        - If no such task exists, add the new task.
        - If an incomplete task is found, notify the user.
- [ ] need database table to persist.

## What's missing 
- [X] there no way to start need a command for that.
- [X] if user start a task current date will be inserted in start_time field
- [X] if user end a task current date will be inserted in end_time field
