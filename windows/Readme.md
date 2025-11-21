# Windows Assignment

---

## **Day 1: Windows Basics & System Information**
### Topics: OS Detection, Basic System Info, Environment Variables

---

### **1. Write a script that prints the Windows version**
```python
print(platform.platform())
```

### **2. Print the computer name and the current logged-in user**
```python
print(os.environ.get("COMPUTERNAME"), os.getlogin())
```

### **3. List all environment variables and their values**
```python
for k, v in os.environ.items():
    print(k, v)
```

### **4. Get and print the current working directory**
```python
print(os.getcwd())
```

### **5. Find and display the system architecture (32-bit or 64-bit)**
```python
print(platform.architecture()[0])
```

### **6. Retrieve the current user's home directory path**
```python
print(os.path.expanduser("~"))
```

### **7. Write a script to detect if the system is Windows or not**
```python
print(platform.system() == "Windows")
```

### **8. Print the system boot time**
```python
print(os.popen("wmic os get lastbootuptime").read())
```

### **9. Retrieve and print the CPU name and number of cores**
```python
print(platform.processor(), os.cpu_count())
```

### **10. Check if a specific environment variable (like PATH) exists**
```python
print("PATH" in os.environ)
```

---

## **Day 2: Processes, Tasks, and Services**
### Topics: Process Listing, Management, Service Control

---

### **1. List all running processes along with their PID**
```python
print(os.popen("tasklist").read())
```

### **2. Kill a process by its name**
```python
print(os.popen("taskkill /IM notepad.exe /F").read())
```

### **3. Start a new process (e.g., Notepad)**
```python
os.system("notepad.exe")
```

### **4. Monitor and print CPU usage of the top 5 processes**
```python
print(os.popen("wmic path Win32_PerfFormattedData_PerfProc_Process get Name,PercentProcessorTime").read())
```

### **5. Detect if a given process (like explorer.exe) is running**
```python
tasks = os.popen("tasklist").read()
print("explorer.exe" in tasks)
```

### **6. Restart a Windows service (example: Spooler)**
```python
os.system("net stop spooler")
os.system("net start spooler")
```

### **7. List all services, their status, and startup type**
```python
print(os.popen("sc query").read())
```

### **8. Start, stop, or restart a service programmatically**
```python
os.system("net stop spooler")
os.system("net start spooler")
```

### **9. Simple task-manager clone that refreshes every 5 seconds**
```python
print(os.popen("tasklist").read())
time.sleep(5)
```

### **10. Terminate all processes started by a specific user**
```python
print(os.popen('taskkill /FI "USERNAME eq testuser" /F').read())
```

---

## **Day 3: File System & Automation**
### Topics: File Operations, Directories, Metadata, Backups

---

### **1. List all files and folders in C:\Users\Public**
```python
print(os.listdir("C:\\Users\\Public"))
```

### **2. Copy a file from one location to another**
```python
shutil.copy("a.txt", "b.txt")
```

### **3. Monitor a directory for file changes**
```python
before = os.listdir("C:\\test")
time.sleep(2)
after = os.listdir("C:\\test")
print(set(after) - set(before))
```

### **4. Find the size of every file inside a specific folder**
```python
for name in os.listdir("C:\\test"):
    path = "C:\\test\\" + name
    if os.path.isfile(path):
        print(name, os.path.getsize(path))
```

### **5. Automatically create daily backups of a folder**
```python
today = time.strftime("%Y-%m-%d")
shutil.copytree("C:\\data", f"C:\\backup\\{today}")
```

### **6. Search for a file by name across a directory tree**
```python
for root, dirs, files in os.walk("C:\\"):
    if "target.txt" in files:
        print(os.path.join(root, "target.txt"))
```

### **7. Monitor and report any new files created in C:\Windows\Temp**
```python
before = os.listdir("C:\\Windows\\Temp")
time.sleep(2)
after = os.listdir("C:\\Windows\\Temp")
print(set(after) - set(before))
```

### **8. Zip and unzip folders**
```python
with zipfile.ZipFile("data.zip", "w") as z:
    for file in os.listdir("C:\\data"):
        z.write(os.path.join("C:\\data", file))

with zipfile.ZipFile("data.zip", "r") as z:
    z.extractall("unzipped")
```

### **9. List all files modified in the last 24 hours**
```python
now = time.time()
for name in os.listdir("C:\\test"):
    path = "C:\\test\\" + name
    if os.path.isfile(path):
        if now - os.path.getmtime(path) < 86400:
            print(name)
```

### **10. Find all files bigger than 100MB in a directory**
```python
for root, dirs, files in os.walk("C:\\test"):
    for f in files:
        p = os.path.join(root, f)
        if os.path.getsize(p) > 100 * 1024 * 1024:
            print(p)
```

