def fibonacci(n):
    if n == 0:
        return 0
    elif 0 !=n <= 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__=='__main__':
    n = int(input('Your number: '))
    print (fibonacci(n))