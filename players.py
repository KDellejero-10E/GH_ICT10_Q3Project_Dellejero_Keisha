from pyscript import Element

def show_players():
    players = [
        "Escudero", "Estrada", "Tolentino", "Pimentel",
        "Binay", "Cayetano", "Dela Rosa", "Ejercito",
        "Gatchalian", "Go", "Hontiveros", "Lapid",
        "Legarda", "Marcos", "Padilla", "Poe",
        "Revilla", "Tulfo", "Villanueva", "Villar", "Zubiri"
    ]

    output = ""
    for i, name in enumerate(players, 1):
        output += f"{i}) {name}<br>"

    Element("players_list").write(output)