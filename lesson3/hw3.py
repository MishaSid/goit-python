def main(n):
    if __name__ == '__main__':
        return n

def fibonacci(n):

    if n == 0:
        return 0
    elif n <= 2:
        return 1       
    else:
        return fibonacci(n-1) + fibonacci(n-2)      
    
print(fibonacci(3))