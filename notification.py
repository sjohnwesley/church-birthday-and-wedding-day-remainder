from plyer import notification
from datetime import datetime, timedelta
from database.db import get_birthdays, get_weddings


def show_weekly_notifications():

    today = datetime.now()

    # Friday = 4, Saturday = 5
    if today.weekday() not in [4, 5]:
        return

    days_since_sunday = (today.weekday() + 1) % 7

    this_week_start = (
        today - timedelta(days=days_since_sunday)
    ).replace(
        hour=0,
        minute=0,
        second=0,
        microsecond=0
    )

    next_week_start = (
        this_week_start + timedelta(days=7)
    )

    next_week_end = (
        next_week_start + timedelta(days=6)
    )

    message = ""

    # Birthdays
    for _, name, birthday in get_birthdays():
        try:
            date = datetime.strptime(
                birthday,
                "%d/%m/%Y"
            )

            event_date = date.replace(
                year=next_week_start.year
            )

            if (
                next_week_start.date()
                <= event_date.date()
                <= next_week_end.date()
            ):
                message += (
                    f"🎂 {name} - "
                    f"{event_date.strftime('%d %b')}\n"
                )
        except:
            pass

    # Weddings
    for _, husband, wife, anniversary in get_weddings():
        try:
            date = datetime.strptime(
                anniversary,
                "%d/%m/%Y"
            )

            event_date = date.replace(
                year=next_week_start.year
            )

            if (
                next_week_start.date()
                <= event_date.date()
                <= next_week_end.date()
            ):
                message += (
                    f"💍 {husband} & {wife} - "
                    f"{event_date.strftime('%d %b')}\n"
                )
        except:
            pass

    if message != "":
        notification.notify(
            title="Upcoming Week Reminders",
            message=message,
            timeout=15
        )