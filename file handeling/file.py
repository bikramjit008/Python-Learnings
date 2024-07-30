# import os
# # f=open("newfile.txt","w")
# f=open("newfile.txt","r")
# print(f.read(7))
# print(f.read(5))
# f.close()

# import os
# f=open("newfile2.txt",'w')
# f.write("I am fine ...and you?\n Hope you are well now.")
# f.close()

import os
f=open("newfile2.txt",'r')
print(f.readline())
f.close()

import os
f=open("newfile2.txt",'r')
print(f.readlines())
f.close()

import os
f=open("newfile2.txt")
for line in f:
    {
        print(f.readline())
    }
f.close()
import os
f=open("newfile2.txt")
for line in f:
    {
        print(line)
    }
f.close()

import os
f=open("newfile.txt","w")
f.write("This is the content that is being written.")
f.write("This is the content that is being written.")

f.close()

import os
f=open("newfile.txt","a")
f.write("This will add with the existing file content.")

f.close()

import os
f=open("newfile3.txt","x")
f.write("hello everyone.")
f.close()

import os
os.remove("newfile.txt")

import os
os.mkdir("new")

import os
os.rmdir("./new")