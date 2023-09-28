numero=int(input("digite um número "))

while numero==0:
    numero=int(input("número inválido, digite novamente: "))

if numero > 0:
    print(f"{numero} é positivo")
else:
    print(f"{numero} é negativo")