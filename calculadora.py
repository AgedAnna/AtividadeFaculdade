import math
x = float(input("Digite um número:\n"))
y = float(input("Digite um número:\n"))

escolha = input("Escolha A para soma, B para subtração, C para multiplicação, D para divisão, \n"
"E para divisão pelo resto, F para elevar e G para calcular a raiz:\n")

som = x+y
sub = x-y
div = x/y
mul = x*x
ele = x**y
resto = x%y
raiz = math.sqrt(y)

if escolha in "Aa":
    print(som)
elif escolha in "Bb":
    print(sub)
elif escolha in "Cc":
    print(mul)
elif escolha in "Dd":
    print(div)
elif escolha in "Ee":
    print(resto)
elif escolha in "Ff":
    print(ele)
elif escolha in "Gg":
    print(raiz)
else:
    print("Digite um valor válido")