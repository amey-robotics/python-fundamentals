# Q1: What is a string? | A: A sequence of characters enclosed in quotes
name = "Rahul"

# Q2: Create a string variable named city | A:
city = "Pune"

# Q3: Print a string | Output: Rahul
name = "Rahul"; print(name)

# Q4: Find length of a string | Output: 6
text = "Python"; print(len(text))

# Q5: Print first character | Output: P
text = "Python"; print(text[0])

# Q6: Print last character | Output: n
text = "Python"; print(text[-1])

# Q7: Concatenate two strings | Output: Hello World
first = "Hello"; second = "World"; print(first + " " + second)

# Q8: Convert to uppercase | Output: PYTHON
text = "Python"; print(text.upper())

# Q9: Convert to lowercase | Output: python
text = "PYTHON"; print(text.lower())

# Q10: Remove spaces | Output: Python
text = "  Python  "; print(text.strip())

# Q11: Replace text | Output: Java Programming
text = "Python Programming"; print(text.replace("Python", "Java"))

# Q12: Split string into list | Output: ['Python', 'Programming']
text = "Python Programming"; print(text.split())

# Q13: Check if character exists | Output: True
text = "Python"; print("P" in text)

# Q14: Check if character does not exist | Output: False
text = "Python"; print("z" in text)

# Q15: Print using f-string | Output: My name is Rahul and I am 20 years old.
name = "Rahul"; age = 20; print(f"My name is {name} and I am {age} years old.")

# Q16: Slice a string | Output: yth
text = "Python"; print(text[1:4])

# Q17: Reverse a string | Output: nohtyP
text = "Python"; print(text[::-1])

# Q18: Capitalize first letter | Output: Python
text = "python"; print(text.capitalize())

# Q19: Count occurrences of a character | Output: 3
text = "banana"; print(text.count("a"))

# Q20: Find index of a character | Output: 2
text = "Python"; print(text.find("t"))

# Q21: Repeat a string | Output: PythonPythonPython
text = "Python"; print(text * 3)

# Q22: Check string starts with a word | Output: True
text = "Python Programming"; print(text.startswith("Python"))

# Q23: Check string ends with a word | Output: True
text = "Python Programming"; print(text.endswith("Programming"))

# Q24: Convert string to title case | Output: Python Programming
text = "python programming"; print(text.title())

# Q25: Check if all characters are alphabetic | Output: True
text = "Python"; print(text.isalpha())

# Q26: Check if all characters are digits | Output: True
text = "12345"; print(text.isdigit())

# Q27: Check if all characters are alphanumeric | Output: True
text = "Python123"; print(text.isalnum())

# Q28: Join strings | Output: Python Java C++
languages = ["Python", "Java", "C++"]; print(" ".join(languages))

# Q29: Convert string to list of characters | Output: ['P', 'y', 't', 'h', 'o', 'n']
text = "Python"; print(list(text))

# Q30: Get substring from index 2 to end | Output: thon
text = "Python"; print(text[2:])