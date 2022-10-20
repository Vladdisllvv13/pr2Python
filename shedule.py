import time
from watchdog.observers import Observer
from shedule_class import FileShedule

event_handler = FileShedule()
observer = Observer()
path = f"C:/Users/User/Desktop/pythonPR/pr2/test/"
observer.schedule(event_handler, path=path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except:
    print('Exception')
finally:
    observer.stop()
    observer.join()