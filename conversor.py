menu = """
======================================================================================
================Bienvenido al conversor de dólares a cripto things 💎================
======================================================================================


Escoge una criptomoneda por favor.

1 - Ethereums
2 - Bitcoins
3 - Solana

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    dolares = input("¿Cuántos dolares tienes?: ")
    dolares = float(dolares)
    valor_ethereum = 4291.91
    ethereums = dolares / valor_ethereum
    ethereums = round(ethereums, 3)
    ethereums = str(ethereums)
    print("Tienes ETH " + ethereums + " ethereums")
elif opcion == 2:
    dolares = input("¿Cuántos dolares tienes?: ")
    dolares = float(dolares)
    valor_bitcoin = 61511.03
    bitcoins = dolares / valor_bitcoin
    bitcoins = round(bitcoins, 5)
    bitcoins = str(bitcoins)
    print("Tienes BTC " + bitcoins + " bitcoins")
elif opcion == 3:
    dolares = input("¿Cuántos dolares tienes?: ")
    dolares = float(dolares)
    valor_solana = 192.24
    solana = dolares / valor_solana
    solana = round(solana, 2)
    solana = str(solana)
    print("Tienes SOL " + solana + " solanas")
else:
    print("Ingresa una opción correcta por favor")


