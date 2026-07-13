def add():
    sum1=a+b
    print(sum1)
def sub():
    if a>b:
        diff=a-b
        print(diff)
    else:
        diff=b-a
        print(diff)

def mul():
    pro=a*b
    print(pro)

def div():
    if b==0:
        print("cannot divide by zero")
    else:
        div=a/b
        print(div)


print("Welcome to the basic calculator here you can add/sub/mul/div two numbers")

a=int(input("Enter your number:"))
b=int(input("Enter your number:"))
op=input("do you wish to add,sub,mul or div:")
if op=="add":
    add()
elif op=="sub":
    sub()
elif op=="mul":
    mul()
elif op=="div":
    div()
else:
    print("Invalid operation")
    
