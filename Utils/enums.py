from enum import Enum
from typing import Final


class Command(Enum):
    ADD: Final = "add"
    COMPLETE: Final = "complete"
    LIST: Final = "list"
    REPORT: Final = "report"
