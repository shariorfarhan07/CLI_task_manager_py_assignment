from datetime import datetime

print(datetime.fromisoformat('2023-09-19T11:53:15.315107')-datetime.fromisoformat('2024-09-18T11:53:15.315107'))

def time_for_completing_task(task):
    return  datetime.fromisoformat(task.end_time)-datetime.fromisoformat(task.start_time)