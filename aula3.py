print("######################")
a = int(input("Digite primeiro valor: "))
b = int(input("Digite segundo valor: "))

if a > b:
    print("Maior número é: {}". format(a))
elif b > a:
    print("Maior é: {}".format(b))
else:
    print("Os valores são iguais: {}".format(b))

print("Fim")
print("######################")

print("----------------------")

num = int(input("Digite um número: "))
res = num % 2

if res == 0:
    print("Número {} é par".format(num))
elif res != 0 or res == 1:
    print("Número {} é impar".format(num))

print("----------------------")

print("@@@@@@@@@@@@@@@@@@@@@@")

av1 = int(input("Insira nota da avaliação 1: "))
av2 = int(input("Insira nota da avaliação 2: "))
av3 = int(input("Insira nota da avaliação 3: "))

media = (av1 + av2 + av3)/3

if av1 <= 10 and av2 <= 10 and av3 <= 10:
    print("Média é: {0:.1f}".format(media))
else:
    print("Inserido valor inválido!")
print("@@@@@@@@@@@@@@@@@@@@@@")