import sys

name = "owoalex"

print("You said your name was  " + name)

if (sys.version_info[0] == 2):
    name_given = str(raw_input("Is that your name? Type it here for me!\n"))
else:
    name_given = str(input("Is that your name? Type it here for me!\n"))

if name_given == name:
    print("Stop beeing a weeb you weeb")
else:
    print("Ok, you're free to go")
