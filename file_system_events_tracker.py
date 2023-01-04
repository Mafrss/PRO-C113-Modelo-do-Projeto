import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Classe Gerenciadora de Eventos
class FileEventHandler(FileSystemEventHandler):

    #1_on_created

    #2_on_deleted

    #3_on_modified

    #4_on_moved

        


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileEventHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Inicie o Observer
observer.start()


#5_Escreva uma exceção para keyboardInterrupt

while True:
    time.sleep(2)
    print("executando...")






