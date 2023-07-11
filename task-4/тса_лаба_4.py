
import random


def fermat_test(n):
    # Проверяем случай с n = 2 или 3
    if n <= 3:
        return True if n > 1 else False


    # Выбираем случайное число a меньше n
    a = random.randint(2, n - 2)


    # Проверяем условие a^(n-1) mod n == 1
    if pow(a, n - 1, n) != 1:
        return False

    return True

def is_prime(binary_number):
    # Преобразуем бинарное число в десятичное
    decimal_number = int(binary_number, 2)

    # Проверяем простоту числа с помощью теста Ферма
    if fermat_test(decimal_number):
       return "Бинарное число " + binary_number + " является простым."
    else:
       return "Бинарное число " + binary_number + " не является простым."



binary_number = input("Введите бинарное число для проверки на простоту: ")

print(is_prime(binary_number))

print()

print('Проверим простые числа')
test_prime = ['11', '10001', '110101', '11010011', '111110011', '1111010111']
for x in test_prime:
    print(is_prime(x))

print()

print('Проверим составные числа')
test_composite = ['110', '11011', '1001011', '10011100', '1000110000', '1101111000']
for x in test_composite:
    print(is_prime(x))
