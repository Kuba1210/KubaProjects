from random import randint
twoje_punkty = 0
punkty_komputera = 0
while (twoje_punkty < 5 and punkty_komputera < 5):
    kamien_papier_nozyce = randint(1, 3)
    wybierasz = input("""Kamień, papier, nożyce!
    Kamień: Wybierz "1"
    Papier: Wybierz "2"
    Nożyce: Wybierz "3"
    Twój wybór: """)
    if kamien_papier_nozyce == 1:
        print("Kamil: Kamień!")
    elif kamien_papier_nozyce == 2:
        print("Kamil: Papier!")
    elif kamien_papier_nozyce == 3:
        print("Kamil: Nożyce!")

    if (wybierasz == "1") and (kamien_papier_nozyce == 1):
        print("Oboje daliscie kamien! remis!")
    elif (wybierasz == "2") and (kamien_papier_nozyce == 2):
        print("Oboje daliscie papier! Remis!")
    elif (wybierasz == "3") and (kamien_papier_nozyce == 3):
        print("Oboje daliscie nozyce! Remis!")

    if (wybierasz == "1") and (kamien_papier_nozyce == 3):
        print("Punkt dla Pawła!")
        twoje_punkty += 1
    elif (wybierasz == "1") and (kamien_papier_nozyce == 2):
        print("Punkt dla Kamila!")
        punkty_komputera += 1

    if (wybierasz == "2") and (kamien_papier_nozyce == 1):
        print("Punkt dla Pawła!")
        twoje_punkty += 1
    elif (wybierasz == "2") and (kamien_papier_nozyce == 3):
        print("Punkt dla Kamila!")
        punkty_komputera += 1

    if (wybierasz == "3") and (kamien_papier_nozyce == 1):
        print("Punkt dla Kamila!")
        punkty_komputera += 1
    elif (wybierasz == "3") and (kamien_papier_nozyce == 2):
        print("Punkt dla Pawła!")
        twoje_punkty += 1
    print(f"""Aktualny wynik:
    Punkty Pawła: {twoje_punkty}
    Punkty Kamila: {punkty_komputera}
""")

if twoje_punkty > punkty_komputera:
    print("Paweł wygrał!")
else:
    print("Kamil wygrał!")
