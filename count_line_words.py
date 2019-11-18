#program to count no. of lines , words and characters in a txt file.
import sys
import os
print("Enter file name:")
fname=input()
if os.path.isfile(fname):
    f=open(fname,'r')
else:
    print(fname+ " File does not exist")
    sys.exit()
cl=cc=cw=0
for line in f:
    print(line)
    print("The words are\n")
    words=line.split()
    print(words)
    cl=cl+1
    cw=cw+len(words)
    cc=cc+len(line)
print(" No. of lines: ",cl)
print("no. of words:",cw)
print("No. of characters :",cc)
# print full file data
f.seek(0,0)
str=f.read()
print(str)
f1=open("text2.txt","a")
f1.write(str)
f.close()
f1.close()
