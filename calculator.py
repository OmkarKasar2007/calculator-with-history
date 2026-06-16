def add(a,b):
 return a+b
def sub(a,b):
 return a-b
def mul(a,b):
 return a*b
def div(a,b):
 if b==0:
  print("Cannot divide by zero")
  return None
 else:
   return a/b
history=[]
while True :
 print("\nCALCULATOR\n")
 print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Show History\n6.Exit\n7.Clear History")
 choice=int(input("Enter your choice: "))
 if choice==1:
  x=int(input("Enter first number: "))
  y=int(input("Enter second number: "))
  print("Addition of",x,"and",y,"is",add(x,y))
  history.append(f"{x} + {y} = {add(x,y)}")
 elif choice==2:
  x=int(input("Enter first number: "))
  y=int(input("Enter second number: "))
  print("Subtraction of",x,"and",y,"is",sub(x,y))
  history.append(f"{x} - {y} = {sub(x,y)}")
 elif choice==3:
  x=int(input("Enter first number: "))
  y=int(input("Enter second number: "))
  print("Multiplication of",x,"and",y,"is",mul(x,y))
  history.append(f"{x} * {y} = {mul(x,y)}")
 elif choice==4:
  x=int(input("Enter first number: "))
  y=int(input("Enter second number: "))
  print("Division of",x,"and",y,"is",div(x,y))
  history.append(f"{x} / {y} = {div(x,y)}")
 elif choice==5:
  print("HISTORY")
  for i in history:
   print(i)
 elif choice==6:
  break
 elif choice==7:
  history.clear()
  print("History cleared")
 else:
  print("Invalid choice")
