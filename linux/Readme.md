# Linux Challenges — Commands & Solutions

This file contains **all Linux challenge questions and their corresponding commands**, organized by day.

---

## ✅ Day 1: System Basics

### 1. Display the Linux distribution name and version

```
cat /etc/*-release
lsb_release -a
```

### 2. Print the current username and its user ID (UID)

```
echo $USER
echo $UID
```

### 3. Show the system's hostname and local IP address

```
hostip=$(hostname -I)
hostname1=$(hostname)
echo "hostname: $hostname1  Ip: $hostip"
```

### 4. List all environment variables

```
env
```

### 5. Detect whether the current system is running Linux

```
uname -a
```

### 6. Display the system uptime in readable format

```
uptime -p
```

### 7. Show the CPU model and number of cores

```
lscpu
```

### 8. Display total and available RAM (human readable)

```
free -m
```

### 9. Determine whether the system is 32-bit or 64-bit

```
uname -m
```

### 10. Monitor CPU and memory usage live

```
top
```

---

## ✅ Day 2: Files & Permissions

### 1. Create a file and write "Hello Linux" into it

```
echo "hello linux" >> ./idk.txt
```

### 2. Check the size of a file in bytes

```
stat -c %s ./level_1.sh
```

### 3. List all files (including hidden) with permissions and sizes

```
ls -l -a
```

### 4. Make a script executable

```
chmod 777 ./test.txt
```

### 5. Recursively change owner of all files in a directory

```
sudo chown -R test:test ./test/
```

### 6. Find all files larger than 100MB

```
find / -type f -size +100M
```

### 7. Create a symbolic link to a file

```
ln -s ./test/filler.txt symlink.txt
```

### 8. Display owner and permissions of a file

```
ls -l test.txt
```

### 9. Compare two text files

```
diff --brief <(sort ./test/filler1.txt) <(sort ./test/filler2.txt)
```

### 10. Show disk usage of each subdirectory in /home

```
du -h /home
```

---

## ✅ Day 3: Processes & Services

### 1. List all running processes

```
sudo ps -ef
```

### 2. Find PID of a running service (e.g., nginx)

```
pgrep nginx
```

### 3. Kill a process by name

```
pkill nginx
```

### 4. Display memory usage of a specific process

```
ps aux | grep sshd
```

### 5. Show top five processes by CPU

```
ps aux --sort=-%cpu | head -5
```

### 6. Start a systemd service

```
sudo systemctl start ssh
```

### 7. Check if a service is enabled on boot

```
systemctl is-enabled ssh
```

### 8. Restart a specific service

```
sudo systemctl restart ssh
```

### 9. View logs for a service

```
journalctl -u ssh
```

### 10. Monitor live process activity

```
top
```
****
