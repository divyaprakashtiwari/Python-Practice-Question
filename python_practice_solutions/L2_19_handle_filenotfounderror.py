# Level 2 - Q19: Handle FileNotFoundError
# Handle FileNotFoundError while opening a file.

try:
    with open("data.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: file not found")
