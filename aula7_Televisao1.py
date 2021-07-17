class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumetar_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

print("---------------------------------")

televisao = Televisao()
print("Televisão está desligada: {}".format(televisao.ligada))
televisao.power()
print("Televisão está ligada: {}".format(televisao.ligada))
televisao.power()
print("Televisão está ligada: {}".format(televisao.ligada))

print("---------------------------------")

print("Canal : {}".format(televisao.canal))
televisao.power()
print("Televisão está ligada: {}".format(televisao.ligada))
televisao.aumetar_canal()
televisao.aumetar_canal()
print("Canal: {}".format(televisao.canal))
televisao.diminui_canal()
print("Canal: {}".format(televisao.canal))