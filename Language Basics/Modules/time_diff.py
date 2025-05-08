from datetime import datetime
from time import sleep

time_now = datetime.now()
sleep(3)
time_then = datetime.now()

diff = time_then-time_now
print(f"diff = {diff}")
print(f"diff (in seconds) = {diff.total_seconds()}")