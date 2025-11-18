import os
import shutil
import time
import zipfile

def ans_1():
    print(os.listdir("C:\\Users\\Public"))

def ans_2():
    shutil.copy("a.txt", "b.txt")

def ans_3():
    before = os.listdir("C:\\test")
    time.sleep(2)
    after = os.listdir("C:\\test")
    print(set(after) - set(before))

def ans_4():
    for name in os.listdir("C:\\test"):
        path = "C:\\test\\" + name
        if os.path.isfile(path):
            print(name, os.path.getsize(path))

def ans_5():
    today = time.strftime("%Y-%m-%d")
    shutil.copytree("C:\\data", f"C:\\backup\\{today}")

def ans_6():
    for root, dirs, files in os.walk("C:\\"):
        if "target.txt" in files:
            print(os.path.join(root, "target.txt"))

def ans_7():
    before = os.listdir("C:\\Windows\\Temp")
    time.sleep(2)
    after = os.listdir("C:\\Windows\\Temp")
    print(set(after) - set(before))

def ans_8():
    with zipfile.ZipFile("data.zip", "w") as z:
        for file in os.listdir("C:\\data"):
            z.write(os.path.join("C:\\data", file))
    with zipfile.ZipFile("data.zip", "r") as z:
        z.extractall("unzipped")

def ans_9():
    now = time.time()
    for name in os.listdir("C:\\test"):
        path = "C:\\test\\" + name
        if os.path.isfile(path):
            if now - os.path.getmtime(path) < 86400:
                print(name)

def ans_10():
    for root, dirs, files in os.walk("C:\\test"):
        for f in files:
            p = os.path.join(root, f)
            if os.path.getsize(p) > 100 * 1024 * 1024:
                print(p)

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
