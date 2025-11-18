import os
import time

def ans_1():
    print(os.popen("tasklist").read())

def ans_2():
    print(os.popen("taskkill /IM notepad.exe /F").read())

def ans_3():
    os.system("notepad.exe")

def ans_4():
    print(os.popen("wmic path Win32_PerfFormattedData_PerfProc_Process get Name,PercentProcessorTime").read())

def ans_5():
    tasks = os.popen("tasklist").read()
    print("explorer.exe" in tasks)

def ans_6():
    os.system("net stop spooler")
    os.system("net start spooler")

def ans_7():
    print(os.popen("sc query").read())

def ans_8():
    os.system("net stop spooler")
    os.system("net start spooler")

def ans_9():
    print(os.popen("tasklist").read())
    time.sleep(5)

def ans_10():
    print(os.popen('taskkill /FI "USERNAME eq testuser" /F').read())

def main():
    ans_1()
    ans_2()
    ans_3()
    ans_4()
    ans_5()
    ans_6()
    ans_7()
    ans_8()
    ans_9()
    ans_10()

main()
