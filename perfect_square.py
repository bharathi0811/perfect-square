n = int(input("Enter the number: "))
def perfect_square(n):
    m=n
    if n ==1:
        return True
    for i in range(1, n):
        if i * i-m ==0:
            return True
    else:
        return False
print(perfect_square(n))