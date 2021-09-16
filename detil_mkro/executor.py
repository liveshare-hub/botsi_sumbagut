from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor

from detil_mkro.pushNotif import sendNotif

def mulai():

    # jobstores = {
    #     'mongo':{'type':'mongodb'},
    #     'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    # }

    # executors = {
    #     'default': {
    #         'type': 'threadpool','max_workers':20},
    #         'processpool': ProcessPoolExecutor(max_workers=5)
        
    # }

    # job_defaults = {
    #     'coalesce': False,
    #     'max_instances':3
    # }

    scheduler = BackgroundScheduler()

    #days_of_week = 'mon-fri'
    scheduler.add_job(sendNotif, 'cron', day_of_week='mon-fri', hour='7')

    print(scheduler.print_jobs())
    
    print('Scheduling is running')
    scheduler.start()