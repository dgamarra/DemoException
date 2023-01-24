class OperacionesBasicas:
    def suma(self, sumando1, sumando2):
        if not isinstance(sumando1, (int, float)) or not isinstance(sumando2, (int, float)):
            raise Exception("Oops! Los sumandos deben ser int o float.")
        return sumando1 + sumando2

    def division(self, dividendo, divisor):
        if not isinstance(dividendo, (int, float)) or not isinstance(divisor, (int, float)):
            raise Exception("Oops! El Divideno y el divisor sumandos deben ser int o float.")

        try:
            return dividendo / divisor
        except ZeroDivisionError:
            print("El divisor no puede ser cero.")
            exit(2)
    def ingresoParametro(self, parametro):
        if not isinstance(parametro, (int, float)):
            try:
                parametro=float(parametro)
            except ValueError:
                print("No se puede convertir a float")
                exit(2)
        return parametro