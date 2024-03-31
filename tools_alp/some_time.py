from crewai_tools import tool
from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


@tool("Check time")
def get_time(timezone: str) -> str:
    """Returns current time in timezone."""
    return _get_time_logic(timezone)


def _get_time_logic(timezone: str) -> str:
    try:
        timezone = ZoneInfo(timezone)
        now = datetime.now(timezone)
        return now.strftime('%Y-%m-%d %H:%M:%S')
    except ZoneInfoNotFoundError:
        return "Unknown timezone"
