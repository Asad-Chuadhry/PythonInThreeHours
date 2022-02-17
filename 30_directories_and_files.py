from pathlib import Path
# Absolute path
# c:\program Files\Microsoft
# /usr/local/bin
# Relative Path
current_path = Path()
print(current_path.absolute())
a_package_dir_path = Path("a_package")
print(a_package_dir_path)
email_path = Path("emails")
print(email_path.exists())
new_email_path = Path("new emails")
# new_email_path.mkdir() to create a directory
# new_email_path.rmdir() to delete a directory

# search for a file or directory in a directory
for file in current_path.glob("*"):
    # for file in current_path.glob("*.py"): to search only .py file
    print(file)
