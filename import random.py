import random

options = ("piedra", "papel", "tijera")
rounds = 1
computer_wins = 0
user_wins = 0
user2_wins = 0

print("""
      [🤖 Bienvenido al juego de Piedra, Papel o tijera para 3 personas🙋🙋]
                  >>> Ingresa una opcion <<<
      """)

while rounds < 4:
    print("***" * 10)
    print("ROUND", rounds)
    print("***" * 10)

    print(f"""
🤖 computer_wins: {computer_wins})
🙋 user_wins: {user_wins})
🙋 user2_wins: {user2_wins})
    """)

    user_option = input(">>>User:piedra, papel o tijera => ").lower()
    user2_option = input(">>>User2:piedra, papel o tijera => ").lower()

    while user_option not in options or user2_option not in options or user_option and user2_option not in options:
        print("Esas opciones son invalida")
        user_option = input(">>>User: piedra, papel o tijera => ").lower()
        user_option2 = input(">>>User2: piedra, papel o tijera => ").lower()
        break
    
    computer_option = random.choice(options)

    print("User option = ", user_option)
    print("User2 option = ", user2_option)
    print("Computer option = ", computer_option)

    if user_option == computer_option == user2_option:
        print("Empate!\n")

    elif user_option == "piedra" and user2_option == "piedra" or user_option == "piedra" and computer_option == "piedra" or user2_option == "piedra" and computer_option == "piedra":

        if computer_option == "papel":
            print("Perdiste!\n")
            computer_wins += 1
        elif user2_option == "papel":
            print("Ganaste!\n")
            user2_wins += 1
        elif user_option == "papel":
            print("ganaste!\n")
            user_wins += 1
        else:
            print("---" * 10)
            print("Nadie gana!\n")

    elif user_option == "papel" and user2_option == "papel" or user_option == "papel" and computer_option == "papel" or user2_option == "papel" and computer_option == "papel":

        if computer_option == "piedra":
            print("📄 Empate de parte de dos usuarios y perdida de uno!🪨")
            print("---" * 10)
            print("¡Nadie gana!\n")
        elif computer_option== "tijera":
            print("✂️ Tijera gana a papel!📄\n")
            computer_wins += 1
        elif user2_option == "tijera":
            print("✂️ Tijera gana a papel!📄\n")
            user2_wins += 1
        elif user_option == "tijera":
            print("✂️ Tijera gana a papel!📄\n")
            user_wins += 1

    elif user_option == "tijera" and user2_option == "tijera" or user_option == "tijera" and computer_option == "tijera" or user2_option == "tijera" and computer_option == "tijera":
        if computer_option == "papel":
            print("✂️ Empate de parte de dos usuarios y perdida de uno!📄\n")
            print("---" * 10)
            print("¡Nadie gana!\n")
            
        elif computer_option == "piedra":
            print("🪨 Piedra gana a tijera!✂️\n")
            computer_wins += 1
        elif user2_option == "piedra":
            print("🪨 Piedra gana a tijera!✂️\n")
            user2_wins += 1
        elif user_option == "piedra":
            print("🪨 Piedra gana a tijera!✂️\n")
            user_wins += 1
    else:
        print("---" * 10)
        print("Nadie gana.")    

    rounds += 1

if user2_wins < user_wins > computer_wins:
    print(f"""
🤖 computer_wins: {computer_wins})
🙋 user_wins: {user_wins})
🙋 user2_wins: {user2_wins})
    """)
    print("🎖El ganador es User🎖")
    print(f"Puntaje: {user_wins}")
    

elif user2_wins < computer_wins > user_wins:
    print(f"""
🤖 computer_wins: {computer_wins})
🙋 user_wins: {user_wins})
🙋 user2_wins: {user2_wins})
    """)
    print("🎖El ganador es Computer🎖")
    print(f"Puntaje: {computer_wins}")
    
elif computer_wins < user2_wins > user_wins:
    print(f"""
🤖 computer_wins: {computer_wins})
🙋 user_wins: {user_wins})
🙋 user2_wins: {user2_wins})
    """)
    print("🎖El ganador es Computer🎖")
    print(f"Puntaje: {user2_option}")
    
else:
    print("Empate")
    print(f"""
🤖 computer_wins: {computer_wins})
🙋 user_wins: {user_wins})
🙋 user2_wins: {user2_wins})
    """)