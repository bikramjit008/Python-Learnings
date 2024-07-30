import os
try:
    f=open("error.txt")
    if f.name=="error.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e2:
    print("Something is fishy.")
else:
    print(f.read())
    f.close()
finally:
    print("The code is finished.")