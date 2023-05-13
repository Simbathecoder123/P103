import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir="C:\\Users\\kavit"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")

    def on_deleted(self, event):
        print(f"Oops someone deleted, {event.src_path}!")

    def on_modified(self, event):
        print(f"Hey someone modified, {event.src_path}!")

    def on_moved(self, event):
        print(f"Wait a sec... someone moved, {event.src_path}!")

event_handler = FileEventHandler()
observer1 = Observer()
observer1.schedule(event_handler, from_dir, recursive=True)
observer1.start
try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stopped..")
    observer1.stop()        
