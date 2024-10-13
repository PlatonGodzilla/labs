def is_prime(number):
    for i in range(2, number):
        if number%i == 0:
            return('составное число')
            break
    else:
        return('простое число')
print(is_prime(int(input())))