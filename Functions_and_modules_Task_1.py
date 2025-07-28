n=int(input('Enter a number: '))
def factorial(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        return 'Not defined'
    else:
        return n*factorial(n-1)
ans=factorial(n)
print('Factorial of ' +str(n)+' is: ' +str(ans))