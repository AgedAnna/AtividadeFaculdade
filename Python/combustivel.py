litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (E-etanol ou G-gasolina): ")

if tipo in "Ee":
    if litros <= 20:
        valor = litros * 3.24 * 0.97
    else:
        valor = litros * 3.24 * 0.95
elif tipo in "Gg":
    if litros <= 20:
        valor = litros * 4.02 * 0.96
    else:
        valor = litros * 4.02 * 0.94
else:
    print("Tipo de combustível inválido.")
    exit()  # encerra o programa em caso de tipo inválido
print(f"Valor a ser pago: R$ {valor:.2f}")
