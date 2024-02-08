print("Witaj w programie do obsługi ładowarki paczek!")

while True:
    total_packages = 0
    total_weight = 0
    total_empty_weight = 0
    max_empty_weight = 0
    max_empty_package = 0

    nmb_elements = int(input("\nPodaj liczbę elementów to wysłania: "))
    if nmb_elements <= 0:
        print("\nPodaj liczbę większą od 0.")
        continue  

    current_package_weight = 0
    current_element = 1
    current_package_number = 1

    while current_element <= nmb_elements:
        weight = float(input(f"\nPodaj wagę elementu {current_element} (od 1 do 10 kg): "))
        if 1 <= weight <= 10:
            if current_package_weight + weight <= 20:
                current_package_weight += weight
            else:
                total_packages += 1
                total_weight += current_package_weight    
                empty_space = 20 - current_package_weight
                total_empty_weight += empty_space
                if empty_space > max_empty_weight:
                    max_empty_weight = empty_space
                    max_empty_package = current_package_number
                current_package_weight = weight
                current_package_number += 1
            current_element += 1
        else:
            print("\nNieprawidłowa waga. Waga elementu musi być z przedziału od 1 do 10 kg.")
    
    if current_package_weight > 0:
        total_packages += 1
        total_weight += current_package_weight
        empty_space = 20 - current_package_weight
        total_empty_weight += empty_space
        if empty_space > max_empty_weight:
            max_empty_weight = empty_space
            max_empty_package = current_package_number
    
    print("\nPodsumowanie:")
    print(f"Liczba wysłanych paczek: {total_packages}")
    print(f"Liczba wysłanych kilogramów: {total_weight}")
    print(f"Suma 'pustych' kilogramów: {total_empty_weight}")
    print(f"Najwięcej 'pustych' kilogramów miała paczka numer {max_empty_package}: {max_empty_weight} kg")