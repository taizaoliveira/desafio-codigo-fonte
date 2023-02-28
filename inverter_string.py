string = input("Digite uma string: ")  # recebe a string do usuário

# inverte os caracteres da string usando um loop for
string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("A string invertida é:", string_invertida)
