from src.logica.OperacionesBasicas import OperacionesBasicas

if __name__ == '__main__':
    operaciones = OperacionesBasicas()
    try:
        sumando1 = operaciones.ingresoParametro(input("Primer sumando: "))
        sumando2 = operaciones.ingresoParametro(input("Segundo sumando: "))
        print(f"{sumando1:.2f} + {sumando2:.2f} = {operaciones.suma(sumando1,sumando2):.2f}")
    except ValueError:
        print("Error: Sumando1 y sumando2 deben ser int o float")

    try:
        dividendo = float(input("Primer dividendo: "))
        divisor = float(input("Segundo divisor: "))
        print(f"{dividendo:.2f} + {divisor:.2f} = {operaciones.division(dividendo,divisor):.2f}")
    except ValueError:
        print("Error: Dividendo y divisor deben ser int o float")