# 🔐 Day 1 — Encoding & Hashing Basics

**File:** `level1.py`
**Topics:** Base64, Hex, MD5, SHA-1, SHA-256

---

## ▶️ How to Run

Each question is implemented as a function (`ans_1()` → `ans_10()`).

To run a specific question:

1. Open `level1.py`
2. Uncomment the function call in `main()`
3. Run the script:

```bash
python3 level1.py
```

Example:

```python
def main():
    ans_3()  # MD5 File Hash
```

---
### 1 Base64 Encode & Decode

Encodes a string into Base64 and decodes it back.

```python
string = "encode"
encoded = base64.b64encode(string.encode())
decoded = base64.b64decode(encoded).decode()
```

---

### 2 Convert String to Hex

Converts text to its hexadecimal representation.

```python
string = "hello man"
hex_value = string.encode().hex()
```

---

### 3 MD5 Hash of a File

Loads file bytes and prints the MD5 hash.

```python
with open(file_name, 'rb') as f:
    print(hashlib.md5(f.read()).hexdigest())
```

---

### 4 SHA-1 Hash of a String

Creates SHA-1 hash from input string.

```python
hashlib.sha1(string.encode()).hexdigest()
```

---

### 5 Password to SHA-256 Hash

Hashes a user-entered password.

```python
password = input("Password: ")
print(hashlib.sha256(password.encode()).hexdigest())
```

---

### 6 File Integrity Check (SHA-256)

Compares hashes of two files.

```python
if hash1 == hash2:
    print("passed integrity check")
```

---

### 7 Brute-Force MD5 4-Digit PINs

Generates MD5 hashes of all PINs 0000-9999.

```python
pin = str(i).zfill(4)
hashlib.md5(pin.encode()).hexdigest()
```

---

### 8 Base64 Encode a File

Binary-safe encoding of file data.

```python
encoded = base64.b64encode(f.read()).decode()
```

---

### 9 Detect Base64 or Hex

Uses regex + decode validation.

```python
def detect_encoding(s):
    ...
```

---

### 10 Multi-Hash Tool

Prints MD5, SHA-1, and SHA-256 of input text.

```python
for h in [hashlib.sha1, hashlib.sha256, hashlib.md5]:
    print(h(text.encode()).hexdigest())
```

---

