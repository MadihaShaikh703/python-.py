print(" 251A018 , 10/2/26 ")
n=int(input("Enter a number : "))
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
          return"prime"
    else  :
         return"Not prime"
print(is_prime(n))
