filmes = {
    "Drama": ["Cidadão Kane", "O Poderoso Chefão"],
    "Comédia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
    "Policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
    "Guerra": ["Rambo", "Platoon", "Tora!Tora!Tora"]
}

with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
    <!DOCTYPE html>
    <html lang="pt=BR">
    <head>
    <meta charset="utf-8">
    <title>Filmes</title>
    </head>
    <body>
    """)
    for c, v in filmes.items():
        pagina.write(f"<h1>{c}</h1>\n")
        for e in v:
            pagina.write(f"<p>{e}</p>\n")
    pagina.write("</body></html>")