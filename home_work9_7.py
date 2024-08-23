def is_prime(func):
    def wrapper(*args):
        num = sum(args)
        if num <= 1:
            print('Число меньше или равно единице')
        if num == 2:
            print('Простое')
        if num % 2 == 0:
            print('Составное')
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                print('Составное')
            else:
                print('Простое')
        return func(*args)
    return wrapper
@is_prime
def sum_three(a, b, c):
    return sum([a, b, c])


result = sum_three(2, 5, 8)
print(result)