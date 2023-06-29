from datetime import datetime

from pytz import timezone  # type:ignore


def kst_now() -> datetime:
    return datetime.now(timezone("Asia/Seoul"))
