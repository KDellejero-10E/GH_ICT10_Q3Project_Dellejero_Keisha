from pyscript import Element

def check_team():
    section = Element("section").value

    if section == "Ruby":
        team = "Yellow Tigers"
        img = "yellow.png"

    elif section == "Sapphire":
        team = "Blue Sharks"
        img = "blue.png"

    elif section == "Emerald":
        team = "Green Eagles"
        img = "green.png"

    else:
        team = "Red Dragons"
        img = "red.png"

    Element("result").element.innerHTML = f"You are part of the {team}"
    Element("team_img").element.setAttribute("src", img)