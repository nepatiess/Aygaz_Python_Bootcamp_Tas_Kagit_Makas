import random
import time

def rock_paper_scissors_Zeynep_Koz():
    time.sleep(2)
    print("----------------------------------------------------------------------------------")
    print("Nature always finds balance. Humanity must learn to live without disturbing this balance.")
    print("----------------------------------------------------------------------------------")
    time.sleep(2)
    print("Welcome! This game is played using the elements of Ice, Fire, and Water.")
    print("Rules:")
    print("Ice: Freezes Water, but is melted by Fire.")
    print("Fire: Melts Ice, but is extinguished by Water.")
    print("Water: Extinguishes Fire, but is frozen by Ice.")
    print("----------------------------------------------------------------------------------")
    time.sleep(2)
    print("The first to win two rounds wins the game.")
    print("Type 'Exit' to leave the game.")

    elements = ["ice", "fire", "water"]
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
            print(f"Round {rounds_played + 1}:")
            player_choice = input("Make your choice (ice, fire, water): ").lower()

            if player_choice == "exit":
                print("You have exited the game. Thank you!")
                return

            if player_choice not in elements:
                print("Invalid choice. Please choose ice, fire, or water.")
                continue

            computer_choice = random.choice(elements)
            print(f"Computer's choice: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (player_choice == "ice" and computer_choice == "water") or \
                 (player_choice == "water" and computer_choice == "fire") or \
                 (player_choice == "fire" and computer_choice == "ice"):
                print("You won this round!")
                player_wins += 1
            else:
                print("The computer won this round!")
                computer_wins += 1

            rounds_played += 1
            print(f"Score: You {player_wins}, Computer {computer_wins}\n")

        if player_wins == 2:
            time.sleep(2)
            print("----------------------------------------------------------------------------------")
            print("Congratulations! You won the game!")
        else:
            print("Unfortunately, the computer won the game.")

        play_again = input("Would you like to play another game? (yes/no): ").lower()
        if play_again != "yes":
            print("You have exited the game. Thank you!")
            break

        computer_play_again = random.choice(["yes", "no"])
        time.sleep(2)
        print("----------------------------------------------------------------------------------")
        print(f"The computer {'wants to continue playing.' if computer_play_again == 'yes' else 'does not want to continue playing.'}")

        if computer_play_again != "yes":
            print("The computer doesn't want to continue, so the game has ended. Thank you!")
            break
            
tas_kagit_makas_Zeynep_Koz()
