anos=int(input("quanto anos você tem? "))
mes=int(input("em que mês estamos? "))
dia=int(input("qual é o dia que estamos? "))

print(f"você tem {anos} dias, em dias isto é {anos*365} dias")
print(f"já que estamos no mês {mes}, coloque aí mais {mes*30} dias")
print(f"e já que a gente tá no dia {dia}")
print(f"no total você viveu {(anos*365)+(mes*30)+(dia)}")