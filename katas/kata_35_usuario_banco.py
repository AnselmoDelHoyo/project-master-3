# Kata 35: Clase UsuarioBanco.
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0 or cantidad > self.saldo:
            raise ValueError("No es posible retirar esa cantidad.")
        self.saldo -= cantidad

    def transferir_dinero(self, destinatario, cantidad):
        self.retirar_dinero(cantidad)
        destinatario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.saldo += cantidad


if __name__ == "__main__":
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    bob.transferir_dinero(alicia, 80)
    alicia.retirar_dinero(50)
    print(alicia.saldo, bob.saldo)
