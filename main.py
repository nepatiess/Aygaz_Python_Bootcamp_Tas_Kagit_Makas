import random
import time

def tas_kagit_makas_Zeynep_Koz():
    time.sleep(2)
    print("----------------------------------------------------------------------------------")
    print("Doğa, her zaman dengeyi kurar. İnsanlık, bu dengeyi bozmadan yaşamasını öğrenmeli.")
    print("----------------------------------------------------------------------------------")
    time.sleep(2)
    print("Hoş geldiniz! Bu oyun, Buz, Ateş ve Su unsurlarını kullanarak oynanır.")
    print("Kurallar:")
    print("Buz: Suyu dondurur, ama Ateş tarafından eritilir.")
    print("Ateş: Buzu eritir, ama Su tarafından söndürülür.")
    print("Su: Ateşi söndürür, ama Buz tarafından dondurulur.")
    print("----------------------------------------------------------------------------------")
    time.sleep(2)
    print("İlk iki turu kazanan oyunu kazanır.")
    print("Oyundan çıkmak için 'Çıkış' yazın.")

    elements = ["buz", "ateş", "su"]
    rounds_played = 0
    player_wins = 0
    computer_wins = 0

    while True:
        rounds_played = 0
        player_wins = 0
        computer_wins = 0

        while player_wins < 2 and computer_wins < 2:
            time.sleep(2)
            print("----------------------------------------------------------------------------------")
            print(f"Tur {rounds_played + 1}:")
            player_choice = input("Seçiminizi yapın (buz, ateş, su): ").lower()

            if player_choice == "çıkış":
                print("Oyundan çıktınız. Teşekkürler!")
                return

            if player_choice not in elements:
                print("Geçersiz seçenek. Lütfen buz, ateş veya su seçin.")
                continue

            computer_choice = random.choice(elements)
            print(f"Bilgisayarın seçimi: {computer_choice}")

            if player_choice == computer_choice:
                print("Beraberlik!")
            elif (player_choice == "buz" and computer_choice == "su") or \
                 (player_choice == "su" and computer_choice == "ateş") or \
                 (player_choice == "ateş" and computer_choice == "buz"):
                print("Bu turu kazandınız!")
                player_wins += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                computer_wins += 1

            rounds_played += 1
            print(f"Durum: Siz {player_wins}, Bilgisayar {computer_wins}\n")

        if player_wins == 2:
            time.sleep(2)
            print("----------------------------------------------------------------------------------")
            print("Tebrikler! Oyunu kazandınız!")
        else:
            print("Maalesef, oyunu bilgisayar kazandı.")

        play_again = input("Başka bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        if play_again != "evet":
            print("Oyundan çıktınız. Teşekkürler!")
            break

        computer_play_again = random.choice(["evet", "hayır"])
        time.sleep(2)
        print("----------------------------------------------------------------------------------")
        print(f"Bilgisayar {'oyuna devam etmek istiyor.' if computer_play_again == 'evet' else 'oyuna devam etmek istemiyor.'}")

        if computer_play_again != "evet":
            print("Bilgisayar devam etmek istemediği için oyun sona erdi. Teşekkürler!")
            break

tas_kagit_makas_Zeynep_Koz()