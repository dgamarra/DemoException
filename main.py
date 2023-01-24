from src.logica.OperacionesBasicas import OperacionesBasicas

if __name__ == '__main__':
    operaciones = OperacionesBasicas()
    try:
        sumando1 = float(input("Primer sumando: "))
        sumando2 = float(input("Segundo sumando: "))
        print(f"{sumando1:.2f} + {sumando2:.2f} = {operaciones.suma(sumando1,sumando2):.2f}")
    except ValueError:
        print("Error: Sumando1 y sumando2 deben ser int o float")