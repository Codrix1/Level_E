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

If you'd like formatting changes, examples, or want Level 2 prepared next, just let me know!
