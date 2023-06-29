class televisao:
    def __init__(self, min, max):
        self.ligada = False
        self.canal = 2
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
        else:
            self.canal = self.cmax #Se passar do Min volta para o maximo
    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1
        else:
            self.canal = self.cmin #Se passar do Max volta para o minimo

tv = televisao(2, 10)

tv.muda_canal_para_baixo()
print(tv.canal)

tv.muda_canal_para_cima()
print(tv.canal)