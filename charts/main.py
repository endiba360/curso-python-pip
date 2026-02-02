import matplotlib.pyplot as plt

def main():
    days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
    time_study = [2, 5, 3, 8, 4]

    plt.bar(days, time_study, color='skyblue')

    plt.title("Horas de estudio a la Semana")
    plt.xlabel("Dias")
    plt.ylabel("Horas")

    plt.savefig("chart.png")

    print("Imagen guardada")
    plt.show()

if __name__ == "__main__":
    main()