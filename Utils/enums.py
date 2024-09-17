from typing import Final

class Command():
    ADD: Final = 'add'
    COMPLETE: Final = 'complete'
    LIST: Final = 'list'
    REPORT: Final = 'report'
    START: Final = 'start'

class Status():
    NOT_STARTED: Final = 'not started'
    COMPLETE: Final = 'complete'
    NOT_FOUND: Final = 'not found'
