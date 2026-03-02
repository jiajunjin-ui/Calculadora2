class Calculadora:
    def sumar (self, a, b):
        return a + b
    def restar (self, a, b):
        return a - b
    def multiplicar (self, a, b):
        return a * b

    def dividir (self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            return (e)

    def exponencial (self, a, b):
        return a ** b
    def modulo (self, a, b):
        return a % b

if __name__ == '__main__':
    C = Calculadora()
    print(C.sumar(2, 3))
    print(C.multiplicar(2, 3))
    print(C.dividir(2, 3))
    print(C.dividir(2, 0))
    print(C.exponencial(2, 3))
    print(C.modulo(2, 3))

