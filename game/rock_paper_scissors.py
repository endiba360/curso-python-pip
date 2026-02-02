import random
import time

options = ["piedra", "papel", "tijeras"]

def get_play_from_user():
    while True:
        play = input("\nElige piedra, papel o tijeras (o 'salir'): ").lower().strip()
        
        if play == 'salir':
            return 'salir'
        
        if play in options:
            return play
        
        print("❌ Error: Esa no es una opcion valida. Intentalo de nuevo.")
        
def determine_the_winner(user, pc):
    if user == pc:
        return "Empate"
    
    victories = {
        "piedra": "tijeras",
        "papel": "piedra",
        "tijeras": "papel"
    }
    
    if victories[user] == pc:
        return "Ganaste"
    else:
        return "Perdiste"
    
def play():
    while True:
        user = get_play_from_user()
        
        if user == 'salir':
            print("¡Gracias por jugar!")
            break
        
        pc = random.choice(options)
        print("\nPiedra... papel... o...")
        time.sleep(1)
        print(f"¡{pc.upper()}! 🤖")
        
        result = determine_the_winner(user, pc)
        
        if result == "Empate":
            print("\n💚 ¡Es un empate!")
            break
        elif result == "Ganaste":
            print("\n🎉 ¡Felicidades! Le ganaste a la Maquina.")
            break
        else:
            print("\n🤖 La Computadora gana esta vez.")
            break

def play_tournament():
    user_points = 0
    pc_points = 0
    goal = 2
    
    print(f"\n🏆 ¡Torneo al mejor de 3! El primero en ganar {goal} rondas gana.")
    
    while user_points < goal and pc_points < goal:
        print(f"\n--- Marcador: Tu {user_points} | PC {pc_points} ---")
        user = get_play_from_user()
        
        if user == 'salir':
            print("¡Gracias por jugar!")
            break
        
        pc = random.choice(options)
        print("Lanzando...")
        time.sleep(1)
        print(f"La PC lanzó: {pc}")
        
        result = determine_the_winner(user, pc)
        
        if result == "Ganaste":
            user_points += 1
            print(f"Resultado: {result}")
        elif result == "Perdiste":
            pc_points +=1
            print(f"Resultado: {result}")
        elif result == "Empate":
            print(f"Resultado: {result}")
            
    if user_points == goal:
        print("\n👑 ¡ERES EL CAMPEÓN DEL TORNEO!")
    elif pc_points == goal:
        print("\n💀 La máquina ha dominado el mundo... perdiste el torneo.")

def main_menu():
    while True:
        print("\n🐍--- Bienvenido a piedra_papel_o_tijera.py ---🐍")
        print("1. Juego Rapido (Una sola ronda)")
        print("2. Torneo (Al mejor de 3)")
        print("3. Salir")
        
        option = input("\nSelecciona una opcion (1, 2 o 3): ").strip()
        if option == "1":
            play()
        elif option == "2":
            play_tournament()
        elif option == "3":
            print("¡Gracias por jugar! Adios.")
            break
        else:
            print("❌ Error: Esa no es una opcion valida. Intentalo de nuevo.")
        

if __name__=='__main__':
    main_menu()
