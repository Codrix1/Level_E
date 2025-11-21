import os
import platform

def ans_1():
    print(platform.platform())

def ans_2():
    print(os.environ.get("COMPUTERNAME"), os.getlogin())

def ans_3():
    for k, v in os.environ.items():
        print(k, v)

def ans_4():
    print(os.getcwd())

def ans_5():
    print(platform.architecture()[0])

def ans_6():
    print(os.path.expanduser("~"))

def ans_7():
    print(platform.system() == "Windows")

def ans_8():
    print(os.popen("wmic os get lastbootuptime").read())

def ans_9():
    print(platform.processor(), os.cpu_count())

def ans_10():
    print("PATH" in os.environ)

def main():
    ans_1()
    # ans_2()
    # ans_3()
    # ans_4()
    # ans_5()
    # ans_6()
    # ans_7()
    # ans_8()
    # ans_9()
    # ans_10()

main()
