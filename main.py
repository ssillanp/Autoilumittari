# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tripdata import car, trip

def menu():
    print("Valitse auto [A, B tai C] ")
    carn = input("->: ")
    print("Anna matkan pituus (km): ")
    dist = int(input("->: "))
    print("Anna keskinopeus (km/h): ")
    speed = int(input("->: "))
    return carn, dist, speed

def main():
    carn, dist, speed = menu()
    trp = trip(dist, speed, car(carn))
    h, m, s = trp.trip_duration()
    print(f"Nopeudella {speed} km/h, {dist} km matka kestää {h} tuntia {m} minuuttia ja {s} sekuntia")
    print(f"Autolla {carn} tällä matkalla polttoainetta kuluu {trp.trip_consumption()} litraa")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
