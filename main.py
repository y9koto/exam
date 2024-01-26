from datetime import datetime
import pytz
import os
import time

alarm_time = "17:48"

while True:

   mykolaiv_time = datetime.now()
   current_time = mykolaiv_time.strftime('%H:%M')

   if current_time == alarm_time:
       print("Будильник сработал в " + current_time)
       print("Будильник отключился. Идет процесс охлаждения...")
