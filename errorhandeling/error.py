# f=open("_text.txt")
#This code will through an error

try:
    f=open("_text.txt")
except Exception:
    print("Sorry, This file doesn't exixt.")


try:
    f=open("text.txt")
    var= novar
except FileNotFoundError:
    print("Sorry, This file doesn't exixt.")


try:
    f=open("text.txt")
    var= novar
except FileNotFoundError:
    print("Sorry, This file doesn't exixt.")
except Exception:
    print("Sorry,Something went wrong.")


try:
    f=open("qtext.txt")#This will catch the 1st error occurs in the code .It will not check the entire code.
    var= novar
except FileNotFoundError as e:
    print(e)
except Exception as e2:
    print(e2)

import os
try:
    f=open("text.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e2:
    print(e2)
else:
    print(f.read())
    f.close()


import os
try:
    f=open("ptext.txt")
except FileNotFoundError as e:
    print(e)
except Exception as e2:
    print(e2)
else:
    print(f.read())
    f.close()
finally:
    print("The code is finished.")


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
