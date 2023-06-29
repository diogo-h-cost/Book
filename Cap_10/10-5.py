class televisao:
    def __init__(self, min = 2, max = 14): #Min e Max opcionais
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = televisao(min = 1, max = 22)
print(tv.cmin)
print(tv.cmax, "\n")

tv2 = televisao(min = 5, max = 10)
print(tv2.cmin)
print(tv2.cmax)