Print("Welcome to The Sales Tracking System")
s=input("Enter Your name")
print("Menu")
print("________")
print("1.Add Sales")
print("2.See History ")
print("3.Logout")
d=int(input("Enter your choice:"))
sales=[]
if(d==1):
  n=int(input("Enter your sales record"))
  sales.append(n)
elif(d==2):
  print("This is your history")
  print(sales)
else:
  print("Logging out Goodbye....)
