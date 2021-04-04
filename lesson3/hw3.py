def main(n):
    return n

def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1       
    else:
        return fibonacci(n-1) + fibonacci(n-2)      

if __name__ == '__main__':    
    n = int(input('Enter number: '))
    print(fibonacci(n))