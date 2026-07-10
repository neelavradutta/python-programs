import sys

# Check if arguments are passed
if len(sys.argv) != 3:
    print("Usage: python program.py source.txt destination.txt")
    sys.exit()

source_file = sys.argv[1]
dest_file = sys.argv[2]

# Step 1: Create source file and write 5 lines
with open(source_file, 'w') as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: This is a file handling program\n")
    f.write("Line 3: Written in Python\n")
    f.write("Line 4: Copying file content\n")
    f.write("Line 5: End of file\n")

# Step 2: Copy content to destination file
with open(source_file, 'r') as src, open(dest_file, 'w') as dst:
    content = src.read()
    dst.write(content)

# Step 3: Display destination file content
print("\nContent of destination file:\n")
with open(dest_file, 'r') as f:
    print(f.read())