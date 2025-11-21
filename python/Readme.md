# Python Challenges – Level 1

This document contains **Level 1 Python challenges** along with their **documented answers**. These exercises introduce basic concepts such as input handling, string manipulation, arithmetic operations, loops, and conditionals.

You can run the solutions by opening the `level_1.py` file and **uncommenting the function call** for the challenge you want to test.

---

## 📘 Challenge List & Answers

Below are the Level 1 challenges and the corresponding solution functions defined in `level_1.py`.

### **1. Print "Hello, Hacker!" to the console.**

**Answer:** Implemented in `ans_1()`

```python
def ans_1():
    print("hello Hacker")
    return
```

---

### **2. Ask the user for their name and print "Welcome, [name]!"**

**Answer:** Implemented in `ans_2()`

```python
def ans_2():
    name = input("enter your name")
    print(f'Welcome, {name} ')
    return
```

---

### **3. Convert "1337" (string) to an integer and add 10.**

**Answer:** Implemented in `ans_3()`

```python
def ans_3():
    string = "1337"
    number = int(string) + 10
    print(number)
    return
```

---

### **4. Ask for two numbers and print sum, difference, product, and quotient.**

**Answer:** Implemented in `ans_4()`

```python
def ans_4():
    first = int(input("enter first number"))
    second = int(input("eneter second number"))
    print(f'''
          Sum: {first+second}
          difference: {abs((first-second))}
          Product: {first * second}
          quotient: {first // second}    
          ''')
    return
```

---

### **5. Reverse the string "rekcah_repus" without using built-in functions.**

**Answer:** Implemented in `ans_5()`

```python
def ans_5():
    def reverse(string):
        reverse = ""
        for i in range(len(string)-1, -1, -1):
            reverse += string[i]
        return reverse

    string = "rekcah_repus"
    print(reverse(string))
    return
```

---

### **6. Check if a number is even or odd.**

**Answer:** Implemented in `ans_6()`

```python
def ans_6():
    def isodd(number):
        if number % 2 == 0:
            return False
        else:
            return True

    number = int(input("enter number:"))
    if isodd(number):
        print("number is odd")
    else:
        print("number is even")
    return
```

---

### **7. Create a boolean variable and print it.**

**Answer:** Implemented in `ans_7()`

```python
def ans_7():
    store = True
    print(store)
    return
```

---

### **8. Convert the binary string "100101" to a decimal number.**

⚠️ **Note:** The implementation in `ans_8()` uses `float()`, which does *not* convert binary. You may update it later.

**Answer (from file):**

```python
def ans_8():
    string = "100101"
    dec = float(string)
    print(dec)
    return
```

---

### **9. Print "H4ck3r" with alternating uppercase and lowercase letters.**

**Answer:** Implemented in `ans_9()`

```python
def ans_9():
    string = "H4ck3r"
    new=""
    for i in range(0, len(string)-1, 2):
        new += string[i].lower()
        new += string[i+1].upper()
    print(new)
    return
```

---

### **10. Replace all vowels in "P@ssw0rd" with "*".**

**Answer (using lowercase version):**

```python
def ans_10():
    string = "password"
    new = string
    for i in range(0, len(string), 1):
        if string[i] in "aeiou":
            print(string[i])
            new = new.replace(string[i], "*", -1)

    print(new)
    return
```

---

## ▶️ Running a Specific Answer

Inside `level_1.py`, the bottom section controls which answer runs:

```python
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
```

Simply **uncomment** the function you want to test.

---
# Python Challenges – Level 2

Level 2 focuses on **control flow, loops, logical operators, validation, and simple algorithms**. This README documents each challenge and its corresponding solution found in the `level_2.py` file.

To run a solution, open `level_2.py` and **uncomment** the function call in the `main()` section.

---

## 📘 Challenge List & Answers

Below are the Level 2 challenges and the functions that solve them.

---

### **1. Ask for a password and allow access only if it matches "s3cr3t".**

**Answer:** Implemented in `ans_1()`

```python
def ans_1():
    password = input("enter the password: ")
    if(password == "s3cr3t"):
        print("correct")
    else:
        print("incorrect")
        ans_1()
    return
```

---

### **2. Print all numbers from 1 to 100 except numbers divisible by 4.**

**Answer:** Implemented in `ans_2()`

```python
def ans_2():
    for i in range(1, 101, 1):
        if i % 4 != 0:
            print("i \n")
    return
```

---

### **3. Print every 4‑digit PIN (0000–9999).**

**Answer:** Implemented in `ans_3()`

```python
def ans_3():
    for i in range(0, 10000, 1):
        if i < 10:
            print(f'000{str(i)}')
        elif i < 100:
            print(f'00{str(i)}')
        elif i < 1000:
            print(f'0{str(i)}')
        else:
            print(i)
    return
```

---

### **4. Check if a given year is a leap year.**

**Answer:** Implemented in `ans_4()`

```python
def ans_4():
    year = int(input("enter year: "))
    if year % 4 == 0 and year % 100 != 0:
        print("leap year")
    else:
        print("not leap year")
    return
```

---

### **5. Find all prime numbers between 1 and 100.**

**Answer:** Implemented in `ans_5()`

```python
def ans_5():
    number = int(input("enter number: "))
    prime = []
    notprime = []
    for i in range(2, number+1, 1):
        if not i in notprime:
            prime.append(i)
            product = 0
            inc = i
            while product < (number + 1):
                product = inc * i
                print(product)
                notprime.append(product)
                inc += 1
    print(prime)            
```

---

### **6. Simulate a login system that locks after 3 failed attempts.**

**Answer:** Implemented in `ans_6()`

```python
def ans_6():
    def retry(tries):
        password = input("enter the password: ")
        if(password == "s3cr3t"):
            print("correct")
        else:
            print("incorrect")
            if tries > 1:
                tries -= 1
                retry(tries)
        return
    retry(3)
    print("used up three attempts")
    return
```

---

### **7. Create a number guessing game (0–10).**

**Answer:** Implemented in `ans_7()`

```python
import random

def ans_7():
    ran = random.randrange(0, 11, 1)
    guess = int(input("guess a number between 0 and 10: "))
    if ran == guess:
        print("correct")
        return
    print("incorrect")
    return
```

---

### **8. Print numbers 1–100 with FizzBuzz rules.**

**Answer:** Implemented in `ans_8()`

```python
def ans_8():
    for i in range(1, 101, 1):
        word = str(i)
        if i % 3 == 0:
            word = "fizz"
        if i % 5 == 0:
            if word == "fizz":
                word = "fizzbuzz"
            else:
                word = "buzz"
        print(word)
```

---

### **9. Continuously ask for a password until the correct one is entered.**

**Answer:** Implemented in `ans_9()`

```python
def ans_9():
    def retry():
        password = input("enter the password: ")
        if(password == "s3cr3t"):
            print("correct")
        else:
            print("incorrect retry")
            retry()
        return
    retry()
    return
```

---

### **10. Check if a string is a palindrome.**

**Answer:** Implemented in `ans_10()`

```python
def ans_10():
    def reverse(string):
        reverse = ""
        for i in range(len(string)-1, -1, -1):
            reverse += string[i]
        return reverse

    string = input("enter the palindrome string: ")
    if string == reverse(string):
        print("palindrome")
    else:
        print("not a palindrome")
    return
```

---

## ▶️ Running a Specific Challenge

In the `main()` function of `level_2.py`, uncomment the function you want to run:

```python
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
```

# Python Challenges – Level 3

Level 3 introduces **Lists, Tuples, Dictionaries, Iteration, and Lookups**. These challenges focus on data structures and how to manipulate and search through them.

All solutions are located in the `level_3.py` file.

To run any challenge, simply **uncomment** the corresponding function call in the `main()` section of that file.

---

## 📘 Challenge List & Answers

Below are the Level 3 exercises and their associated solutions.

---

### **1. Create a list of 10 hacker tools.**

**Answer:** Implemented in `ans_1()`

```python
def ans_1():
    list = [
        "Nmap",
        "Wireshark",
        "Metasploit Framework",
        "Aircrack-ng",
        "John the Ripper",
        "Hydra",
        "Burp Suite",
        "Nikto",
        "sqlmap",
        "Hashcat"
    ]
    return list
```

---

### **2. Print the 3rd item in the list.**

**Answer:** Implemented in `ans_2()`

```python
def ans_2():
    print(ans_1()[2])
    return
```

---

### **3. Create a dictionary of HTTP status codes.**

**Answer:** Implemented in `ans_3()`

```python
def ans_3():
    status_codes = {
        200: "OK",
        201: "Created",
        204: "No Content",
        301: "Moved Permanently",
        302: "Found",
        304: "Not Modified",
        400: "Bad Request",
        401: "Unauthorized",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        408: "Request Timeout",
        409: "Conflict",
        429: "Too Many Requests",
        500: "Internal Server Error",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout"
    }
    return status_codes
```

---

### **4. Count how many times each letter appears in a string.**

**Answer:** Implemented in `ans_4()`

```python
def ans_4():
    string = input("enter string: ")
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    return
```

---

### **5. Sort a list of random numbers without using `.sort()`.**

**Answer:** Bubble sort in `ans_5()`

```python
def ans_5():
    def bubble_sort(numbers):
        n = len(numbers)
        for i in range(0, n-1):
            swapped = False
            for j in range(0, n-i-1):
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    swapped = True
            if not swapped:
                break
        return array

    array = [3, 34, 5, 56, 78, 2, 12, 24]
    print(bubble_sort(array))
    return
```

---

### **6. Store ports and services in a dictionary and allow user queries.**

**Answer:** Implemented in `ans_6()`

```python
def ans_6():
    search = True
    ports = {
        20: "FTP (Data Transfer)",
        21: "FTP (Control)",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS"
    }
    while search:
        port = int(input("please enter the port number: "))
        if port in ports:
            print(ports[port])
        else:
            print("port doesnt exist")
        res = input("Search again [Y/n]: ")
        if res == 'n':
            search = False
    return
```

---

### **7. Function to remove duplicates from a list.**

**Answer:** Implemented in `ans_7()`

```python
def ans_7():
    array = [3, 34, 5, 56, 5, 3, 78, 2, 12, 56, 56, 24]
    new = []
    store = {}
    for i in array:
        if not i in store:
            new.append(i)
            store[i] = 1
    print(new)
    return
```

---

### **8. Convert a list into a comma-separated string.**

**Answer:** Implemented in `ans_8()`

```python
def ans_8():
    list = [1, 'apple', 3.14, 'banana']
    res = ', '.join(str(a) for a in list)
    print(res)
```

---

### **9. Find the longest word in a list.**

**Answer:** Implemented in `ans_9()`

```python
def ans_9():
    list = ['adljflasdoijew', 1, 'apple', 3.14, 'banana']
    max = 0
    word = ""
    for i in list:
        if len(str(i)) > max:
            max = len(str(i))
            word = i
    print(word)
    return
```

---

### **10. Print the password for a given username from a dictionary.**

**Answer:** Implemented in `ans_10()`

```python
def ans_10():
    search = True
    users = {
        "alice": "pass123",
        "bob": "secure456",
        "charlie": "mypwd789",
        "diana": "letmein01",
        "eve": "qwerty99",
        "frank": "hello2025",
        "grace": "python321",
        "heidi": "testpass77",
        "ivan": "code654",
        "judy": "sample111"
    }
    while search:
        user = input("please enter the username: ")
        if user in users:
            print(users[user])
        else:
            print("user doesnt exist")
        res = input("Search again [Y/n]: ")
        if res == 'n':
            search = False
```

---

## ▶️ Running a Specific Challenge

Uncomment the desired function call inside:

```python
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
```

---

