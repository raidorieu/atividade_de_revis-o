num=int(input("digite um número: "))

while num==10:
    num = int(input("digite um número, menos 10: "))

if num>10:
    print(f"{num} É MAIOR QUE 10")
else:
    print(f"{num} É MENOR QUE 10")