from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def get_time(timezone: str) -> str:
    """Returns current time in timezone."""
    try:
        timezone = ZoneInfo(timezone)
        now = datetime.now(timezone)
        return now.strftime('%Y-%m-%d %H:%M:%S')
    except ZoneInfoNotFoundError:
        return "Unknown timezone"
