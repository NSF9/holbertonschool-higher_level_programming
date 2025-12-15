# Python OOP Inheritance - Concepts Overview

This document covers the essential concepts related to class inheritance in Python, including superclasses, subclasses, attributes, built-in functions like `isinstance()` and `super()`, and more.

---

## 🔹 What is a Superclass / Base Class / Parent Class?

A **superclass** (also called **base class** or **parent class**) is the class that provides **attributes and methods** to another class.  
It’s the class that is inherited from.

```python
class Animal:
    def speak(self):
        print("Animal speaks")
