class televisao:
    def __init__(self, canal, min, max):
        self.ligada = False
        self.canal = canal
        self.cmin = min
        self.cmax = max
    def muda_canal_para_baixo(self):
        if self.canal - 1 >= self.cmin:
            self.canal -= 1
    def muda_canal_para_cima(self): #Self -> Objeto tv
        if self.canal + 1 <= self.cmax:
            self.canal += 1

tv = televisao(5, 1, 99)
#Canal atual / Min / Max

print(tv.canal) #Canal atual