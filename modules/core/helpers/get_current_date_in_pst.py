from datetime import datetime

import pytz


def get_current_date_in_pst() -> datetime:
    current_date = datetime.now()
    pst_tz = pytz.timezone("America/Los_Angeles")

    return current_date.astimezone(pst_tz)
