import webbrowser
import time

x = 1

print("This program started at" +time.ctime())

while x < 5:
    time.sleep(5)
    webbrowser.open("http://ny.eater.com/")
    x = x + 1

