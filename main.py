numid = int(input("Digite seu id:\n"))
n1 = float(input("Digite sua 1° nota:\n"))
n2 = float(input("Digite sua 1° nota:\n"))
n3 = float(input("Digite sua 1° nota:\n"))
media = float(input("Digite sua média dos exercicios:\n"))

ma = (n1 + (2 * n2) + (3 * n3) + media) / 7.0
print(numid)
print("Sua notas foram:", n1, n2, n3)
print("Essa foi sua média nos exercicios:", media)
print("Essa foi sua média de aproveitamento:", ma)

if ma >= 9 and ma <= 10:
    print("A, aprovado")
elif ma >= 7.5 and ma <= 9:
    print("B, aprovado")
elif ma >= 6 and ma <= 7.5:
    print("C, aprovado")
elif ma >= 4 and ma <= 6:
    print("D, REPROVADO")
else:
    print("E, REPROVADO")
