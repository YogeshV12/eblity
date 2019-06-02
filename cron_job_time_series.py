import schedule
import time
import datetime
import os

def job():
    print("I'm working...")
    if os.system('python test_download.py') == 0:
        if os.system('python insert_time_series_data.py') == 0:
            os.system('python alert_from_time_series_data.py')
    print("i'm done")
job()
schedule.every(15).minutes.do(job)
while True:
    schedule.run_pending()


