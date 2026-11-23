# FILE HANDLING IN PYTHON (FULL DETAILS)

# Why caution is needed:
# Opening a file uses system resources. If a file isn't closed properly,
# it can cause memory leaks, lock the file, or corrupt/lose unsaved data.

# METHOD 1: Manual open() with try...finally
# 'w' mode = Write mode (creates a new file, or OVERWRITES it if it already exists)
file = open('yutube.txt', 'w')

try:
    # Write text into the file
    file.write("altumiya")
finally:
    # 'finally' ALWAYS runs—even if an error occurs inside the 'try' block.
    # This guarantees the file is closed safely.
    file.close()

# Printing 'file' shows the file object metadata, NOT the text inside the file
print(file)  # <_io.TextIOWrapper name='yutube.txt' mode='w' encoding='UTF-8'>
print(file.closed)  # True (confirms the file is safely closed)
#name='yutube.txt': the file’s name
#mode='w': it was opened for writing; this mode creates the file or replaces its contents
#encoding='UTF-8': text is encoded as UTF-8 when written

# METHOD 2: Using 'with' (Context Manager) — RECOMMENDED
# The 'with' statement automatically closes the file as soon as the block ends,
# even if an error happens. No need to manually write try/finally or file.close().

with open('yutube.txt', 'w') as file:
    file.write("altumiya")

# Outside the 'with' block, the file is already closed automatically
print(file.closed)  # True

# COMMON FILE MODES (Bonus Reference)

# 1. 'a' (Append mode): Adds new text to the end without erasing existing content
with open('yutube.txt', 'a') as file:
    file.write("\nAdding a second line!")

# 2. 'r' (Read mode): Opens the file to read its contents (raises FileNotFoundError if missing)
with open('yutube.txt', 'r') as file:
    content = file.read()
    print(content)
    # Output:
    # altumiya
    # Adding a second line!