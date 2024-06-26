from datetime import datetime, timezone
import time

while True:
    current_utc_time = datetime.now(timezone.utc)
    print("Current UTC time:", current_utc_time)
    time.sleep(.1)  # Sleep for 10 seconds
