num = int(input("Digite um número: "))

# Inicializa os valores dos dois primeiros números da sequência de Fibonacci
a, b = 0, 1

# Enquanto o valor atual da sequência de Fibonacci for menor ou igual ao número informado pelo usuário
while b <= num:
    # Se o valor atual da sequência de Fibonacci for igual ao número informado pelo usuário, exibe uma mensagem
    if b == num:
        print(num, "pertence à sequência de Fibonacci!")
        break
    # Atualiza os valores dos números da sequência de Fibonacci
    a, b = b, a + b
else:
    # Se o número informado pelo usuário não pertencer à sequência de Fibonacci, exibe uma mensagem
    print(num, "não pertence à sequência de Fibonacci.")
