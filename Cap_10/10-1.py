class televisao:
    def __int__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 40
        self.marca = "Samsung"

tv_sala = televisao()
tv_sala.tamanho = 43
tv_sala.marca = "Mancer"

print(f"TV SALA\n"
      f"Tamanho = {tv_sala.tamanho}\n"
      f"Marca = {tv_sala.marca}\n")

tv_coz = televisao()
tv_coz.tamanho = 60
tv_coz.marca = "Aoc"

print(f"TV COZINHA\n"
      f"Tamanho = {tv_coz.tamanho}\n"
      f"Marca = {tv_coz.marca}")