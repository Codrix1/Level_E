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


# 🔐 Day 2 — Symmetric Encryption & Block Modes

**File:** `level2.py`
**Topics:** AES, DES, Block Modes (ECB, CBC, CTR)

---



## 📘 Exercises & Solutions

### 1 AES-CBC Encrypt & Decrypt

Encrypts and decrypts a message using AES-CBC.

```python
data = b"secret"
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

# Decrypt
cipher2 = AES.new(key, AES.MODE_CBC, cipher.iv)
plaintext = unpad(cipher2.decrypt(ciphertext), AES.block_size)
```

---

### 2 AES-ECB Encrypt & Decrypt

Encrypts and decrypts a message using AES-ECB.

```python
cipher = AES.new(key, AES.MODE_ECB)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

# Decrypt
cipher2 = AES.new(key, AES.MODE_ECB)
plaintext = unpad(cipher2.decrypt(ciphertext), AES.block_size)
```

---

### 3 Generate Random AES Key

Generates a 128-bit random AES key.

```python
key = os.urandom(16)  # 16 bytes = 128-bit key
```

---

### 4 PKCS7 Pad & Unpad

Pads and unpads plaintext for AES block size.

```python
padder = padding.PKCS7(algorithms.AES.block_size).padder()
padded_data = padder.update(data) + padder.finalize()

unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
original = unpadder.update(padded_data) + unpadder.finalize()
```

---

### 5 Encrypt a File with AES

Encrypts a file and writes ciphertext to disk.

```python
cipher, iv = encrypt(file_bytes, key, True)  # CBC mode
with open('encrypted.txt', 'wb') as f:
    f.write(cipher)
with open('iv.txt', 'wb') as f:
    f.write(iv)
```

---

### 6 Decrypt AES-Encrypted File

Reads ciphertext + IV and decrypts back to plaintext.

```python
with open('encrypted.txt','rb') as f: cipher = f.read()
with open('iv.txt','rb') as f: iv = f.read()
decrypted = decrypt(cipher, key, True, iv)
```

---

### 7 DES Encryption (ECB)

Encrypts string with DES in ECB mode.

```python
key = b"8bytekey"
plaintext = b"Hello DES!"
ciphertext = des_encrypt_ecb(plaintext, key)
```

---

### 8 AES-ECB vs AES-CBC Comparison

Encrypt same plaintext in ECB and CBC to see difference in output.

```python
# ECB repeats patterns, CBC uses IV so ciphertext differs even for same plaintext
```

---

### 9 Mini AES Encryption Tool

User-provided key and plaintext saved to a file.

```python
plaintext = input("Text: ").encode()
key_input = input("AES key (16/24/32 bytes): ")
ciphertext, iv = encrypt(plaintext, key, mode_cbc)
with open('encrypted_output.bin','wb') as f:
    if iv: f.write(iv + ciphertext)
    else: f.write(ciphertext)
```



