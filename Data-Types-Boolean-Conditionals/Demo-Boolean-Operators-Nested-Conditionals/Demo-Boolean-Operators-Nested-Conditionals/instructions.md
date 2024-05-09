## **Boolean Operators and Conditionals**
### **Boolean Operators:**
- `and`: Both conditions must be True
- `or`: At least one condition must be True
- `not`: Reverses the boolean value

### **Examples:**

#### **Example 1:**
```python
age = int(input("What is your age? "))
if age < 12 or age >= 65:
    print("You can enter for free")
elif 12 <= age <= 18:
    print("You need to pay $8")
else:
    print("You need to pay $16")
```

#### **Example 2: Nested Conditionals:**
```python
print("Welcome to Universal Studios Singapore 2.0!")
height = int(input("Please enter your height (cm): "))
if height > 120:
    age = int(input("What is your age? "))
    if age > 18:
        print("Please pay $12")
    else:
        print("Please pay $5")
else:
    print("Sorry, you are below the height limit and cannot be admitted into this ride")
```

#### **Example 3: Multiple Ifs:**
```python
num = 10
if num == 10:
  print("yes")
if num == 10:
  print("yes")
if num == 10:
  print("yes")
```

### **Notes:**
- In the first example, we use the `or` operator, so if the user is either younger than 12 or older than 65, they can enter for free.
- In the second example, a nested conditional is used to check another condition if the first condition is True.
- The third example demonstrates multiple `if` statements, which are independent of each other.
