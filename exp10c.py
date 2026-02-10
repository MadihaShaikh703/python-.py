print(" 251A018 , 10/2/26 ")
n=int(input("Enter a number : "))
if n==1:
    print("Neither prime nor composite.")
else:
   flag=False
   for i in range (2,n):
      if n%i==0:
         flag=True
         break
         flag=False
   if flag==True:
           print("Not prime.")
   else:
           print("Prime.")

