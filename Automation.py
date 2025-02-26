from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
from datetime import datetime

def job():
    # Execute your script using subprocess
    subprocess.run(['PATH_TO_EXECUTIVE_ORDER_AUTOMATION.PY'])

def within_working_hours():
    current_time = datetime.now().hour
    return 9 <= current_time < 17

scheduler = BlockingScheduler()

# Add a job that runs every hour, but only if within working hours
def schedule_job():
    if within_working_hours():
        job()  # Run the job
    else:
        print("Outside working hours, waiting until next day...")

# Schedule the job every hour
scheduler.add_job(schedule_job, 'interval', hours=1)

# Start the scheduler
scheduler.start()
