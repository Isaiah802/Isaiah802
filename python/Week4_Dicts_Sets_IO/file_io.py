# File I/O Example
with open("sample.txt", "w") as f:
    f.write("Hello, file!")

with open("sample.txt", "r") as f:
    print(f.read())
