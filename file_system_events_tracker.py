import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/hrugg/OneDrive/Escritorio/Programación/Byju's Future School/Python/Proyecto 102-103"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("[" + event.src_path + "] ha sido creado hace unos segundos")
    def on_deleted(self, event):
        print("[" + event.src_path + "] ha sido eliminado hace unos segundos")
    def on_modified(self, event):
        print("[" + event.src_path + "] ha sido modificado hace unos segundos")
    def on_moved(self, event):
        print("[" +event.src_path + "] ha sido movido hace unos segundos")

eventHandler = FileEventHandler()

observer = Observer(from_dir)

observer.schedule(eventHandler, from_dir, recursive = True)

observer.start()


try:
    while (True):
        time.sleep(2)
        print("ejecutando...")
except KeyboardInterrupt:
    print("Se ha terminado la operación de monitoreo")
    observer.stop()