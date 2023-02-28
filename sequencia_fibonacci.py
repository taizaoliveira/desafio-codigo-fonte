num = int(input("Digite um número: "))

a, b = 0, 1

while b <= num:
    if b == num:
        print(num, "pertence à sequência de Fibonacci!")
        break
    a, b = b, a + b
else:
    print(num, "não pertence à sequência de Fibonacci.")
