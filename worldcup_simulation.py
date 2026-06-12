# World Cup 2026 Winner Simulation

winner = "Argentina"

while True:
    country = input("Enter country (or exit): ")

    if country == "exit":
        break

    if country == "":
        continue

    if country == "Uganda":
        pass

    if country == winner:
        print("Winner found:", winner)
        break
    else:
        print("Try again!")