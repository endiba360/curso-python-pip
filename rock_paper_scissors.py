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
            print("Gracias por jugar!")
            break
        
        pc = random.choice(options)
        print(f"La computadora eligio: {pc}")
        
        result = determine_the_winner(user, pc)
        
        if result == "Empate":
            print("💚 Es un empate!")
        elif result == "Ganaste":
            print("🎉 Felicidades! Le ganaste a la Maquina.")
        else:
            print("🤖 La Computadora gana esta vez.")

if __name__=='__main__':
    play()
