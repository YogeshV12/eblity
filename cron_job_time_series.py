import schedule
import time
import datetime
import os

def job():
    print("I'm working...")
    os.system('python time_series_report.py')
    os.system('python insert_time_series_data.py')
    os.system('python alert_from_time_series_data.py')
job()
schedule.every(30).minutes.do(job)
while True:
    schedule.run_pending()


