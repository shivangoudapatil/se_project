import os

#validating based on extension
def validateProgramType(fileName):
    ext = os.path.splitext(fileName)[-1].lower()
    if(ext==".c"):
        #print("Valid File Type")
        return True
    else:
        #print("Not a valid file type")
        return False


x = validateProgramType("hello.c")
x1=validateProgramType("prog1.c")
y = validateProgramType("hi.cpp")
y1 = validateProgramType("prog2c.py")

assert(x==True)
assert(y==False)
