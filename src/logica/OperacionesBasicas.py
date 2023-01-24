class OperacionesBasicas:
    def suma(self, sumando1, sumando2):
        if not isinstance(sumando1, (int, float)) or not isinstance(sumando2, (int, float)):
            raise Exception("Oops! Los sumandos deben ser int o float.")
        return sumando1 + sumando2

    def division(self, dividendo, divisor):
        return dividendo / divisor