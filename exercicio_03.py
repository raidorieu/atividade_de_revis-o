idade=int(input("quantos anos você tem? "))
ano=int(input("em que ano estamos? "))
mes=int(input("em que mês estamos? "))
mesnascimento=int(input("em que mês você nasceu? "))

if mesnascimento>=mes:
    anonascimento=(ano-idade)-1
    print(anonascimento)
elif mesnascimento==mes:
    anonascimento = ano - idade
    print(anonascimento)
else:
    anonascimento=(ano-idade)
    print(anonascimento)
