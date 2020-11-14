#from win10toast import ToastNotifier
from win10toast_persist import ToastNotifier
from apscheduler.schedulers.blocking import BlockingScheduler

#Path to icon
image = "img\\water.ico"


#Define toaster
toaster = ToastNotifier()

#Let user know the program has started
toaster.show_toast("Drink Reminder Started!","You will get a reminder every 30 minutes.",image, None)

def reminder():
    toaster.show_toast("Drink some water!","Your body will be thankful",image,None)

#Setup Scheduler
scheduler = BlockingScheduler()
scheduler.add_job(reminder, 'interval', minutes=30)
scheduler.start()