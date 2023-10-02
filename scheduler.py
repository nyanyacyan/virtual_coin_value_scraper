from apscheduler.schedulers.blocking import BlockingScheduler
import main

def run_task():
    main.my_task()

scheduler = BlockingScheduler()
scheduler.add_job(run_task, 'cron', hour=6, minute=0) # 6時に実行
scheduler.start()
