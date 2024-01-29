# Greeting program using timestamp
import os
import time
timeStamp = time.strftime('%H:%M:%S')
print(type(timeStamp))
timeStampH = int(time.strftime("%H"))
print(timeStampH)
if 1 < timeStampH < 12:
    print(timeStampH)
    print("Good Morning ! Programmer")
elif 12 < timeStampH <= 16:
    print("Good afternoon ! Programmer")
elif 17 <= timeStampH <= 22:
    print("Good evening ! Programmer")
else:
    print("Good night ! Programmer.")

os.system("python --version")