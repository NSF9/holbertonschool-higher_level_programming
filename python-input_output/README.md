# 📘 Python File Handling & JSON

This project teaches the basics of file handling in Python, along with understanding JSON and how to convert between Python data structures and JSON strings.

---

## 🔥 Why Python is Awesome

- Easy to learn and read.
- Supports object-oriented and procedural programming.
- Has powerful built-in libraries.
- Great for file handling, scripting, web, and data processing.

---

## 📂 File Handling in Python

### 📖 How to Open a File

```python
file = open("filename.txt", "r")  # "r" = read
```

### ✍️ How to Write Text in a File

```python
file = open("filename.txt", "w")
file.write("Hello, World!")
file.close()
```

### 📚 How to Read the Full Content of a File

```python
file = open("filename.txt", "r")
print(file.read())
file.close()
```

### 📄 How to Read a File Line by Line

```python
file = open("filename.txt", "r")
for line in file:
    print(line, end="")
file.close()
```

### 🎯 How to Move the Cursor in a File

```python
file = open("filename.txt", "r")
file.seek(5)  # move to the 5th byte
print(file.read())
file.close()
```

---

## 🔐 File Safety & Best Practice

### ✅ How to Make Sure a File is Closed After Using It

```python
file = open("filename.txt", "r")
# some operations
file.close()
```

### 🧠 What is `with` Statement (Context Manager)

The `with` statement ensures the file is automatically closed:

```python
with open("filename.txt", "r") as file:
    print(file.read())
# No need to call file.close()
```

---

## 🌐 JSON (JavaScript Object Notation)

### ❓ What is JSON?

- A lightweight data-interchange format.
- Human-readable and easy to parse.
- Commonly used in APIs.

```json
{
  "name": "Ali",
  "age": 25
}
```

---

## 🔄 Serialization & Deserialization

### 📤 What is Serialization?

Convert Python objects to JSON strings.

```python
import json

data = {"name": "Nora", "city": "Riyadh"}
json_str = json.dumps(data)
```

### 📥 What is Deserialization?

Convert JSON strings to Python objects.

```python
json_str = '{"name": "Nora", "city": "Riyadh"}'
data = json.loads(json_str)
```

---

## 🔁 Convert Between Python & JSON

### 🧪 Python ➜ JSON

```python
import json

data = {"id": 1, "valid": True}
json_data = json.dumps(data)
print(json_data)
```

### 🧬 JSON ➜ Python

```python
import json

json_str = '{"id": 1, "valid": true}'
data = json.loads(json_str)
print(data["id"])
```

---

## 🧭 Accessing Command Line Arguments

```python
import sys

print("Script name:", sys.argv[0])
print("Arguments passed:", sys.argv[1:])
```

### ✅ Example

```bash
$ python script.py arg1 arg2
```

---

## 📎 Summary

| Feature                        | Covered ✅ |
|-------------------------------|-----------|
| Why Python is awesome         | ✅        |
| Open/Write/Read a file        | ✅        |
| Read line by line             | ✅        |
| Move file cursor              | ✅        |
| File safety (`with` usage)    | ✅        |
| JSON basics                   | ✅        |
| Serialization & Deserialization | ✅      |
| Command line arguments        | ✅        |

---

## 🧑‍💻 Author

> Created with ❤️ by Nawaf / Abu Saleh
