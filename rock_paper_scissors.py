import random

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
    print("--- Bienvenido a piedra_papel_o_tijera.py ---")
    
    while True:
        user = get_play_from_user()
        
        if user == 'salir':
            print("¡Gracias por jugar!")
            break
        
        pc = random.choice(options)
        print(f"La computadora eligio: {pc}")
        
        result = determine_the_winner(user, pc)
        
        if result == "Empate":
            print("💚 ¡Es un empate!")
        elif result == "Ganaste":
            print("🎉 ¡Felicidades! Le ganaste a la Maquina.")
        else:
            print("🤖 La Computadora gana esta vez.")

def play_tournament():
    user_points = 0
    pc_points = 0
    goal = 2
    
    print(f"\n🏆 ¡Torneo al mejor de 3! El primero en ganar {goal} rondas gana.")
    
    while user_points < goal and pc_points < goal:
        user = get_play_from_user()
        
        if user == 'salir':
            print("Gracias por jugar!")
            break
        
        pc = random.choice(options)
        print(f"La computadora eligio: {pc}")
        
        result = determine_the_winner(user, pc)
        
        if result == "Ganaste":
            user_points += 1
            print(f"✅ Punto para ti. Marcador: Tu {user_points} | PC {pc_points}")
        elif result == "Perdiste":
            pc_points +=1
            print(f"🤖 Punto para la PC. Marcador: Tu {user_points} | PC {pc_points}")
        else:
            print(f"🤝 Empate técnico. El marcador sigue igual.")
            
    if user_points == goal:
        print("\n👑 ¡ERES EL CAMPEÓN DEL TORNEO!")
    elif pc_points == goal:
        print("\n💀 La máquina ha dominado el mundo... perdiste el torneo.")

if __name__=='__main__':
    play_tournament()
