# Level 2 - Q5: Remove Empty Strings
# Remove empty strings and strings containing only spaces from a list using list comprehension.

words = ["hello", "", "world", "   ", "python", ""]
cleaned = [w for w in words if w.strip() != ""]
print(cleaned)
