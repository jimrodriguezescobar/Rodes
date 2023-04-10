class Fraccion:

    def __init__(self, Numerador, Denominador):
        self.Numerador = Numerador
        self.Denominador = Denominador

    def imprime(self):
        print(self.Numerador, "/", self.Denominador)

    def Multiplicar(self, valor2):
        Numerador = self.Numerador * valor2.Numerador
        Denominador = self.Denominador * valor2.Denominador
        resultado = Fraccion(Numerador, Denominador)
        return resultado


def main():
    valor1 = Fraccion(3, 2)
    valor1.imprime()

    valor2 = Fraccion(7, 4)
    valor2.imprime()

    resultado = valor1.Multiplicar(valor2)
    resultado.imprime()


if __name__ == "__main__":
    main()
