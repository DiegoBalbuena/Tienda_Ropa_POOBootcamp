# Clase base Producto
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def obtener_precio(self):
        return self._precio

    def mostrar_info(self):
        return f'Producto: {self._nombre}, Precio: {self._precio}'


# Clase Ropa que hereda de Producto
class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return f'Ropa: {self._nombre}, Talla: {self._talla}, Tela: {self._tipo_tela}, Precio: {self._precio}'


# Clases derivadas de Ropa
class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_collar):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_collar = tipo_collar

    def mostrar_info(self):
        return f'Camisa: {self._nombre}, Talla: {self._talla}, Tela: {self._tipo_tela}, Collar: {self._tipo_collar}, Precio: {self._precio}'


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_cintura):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_cintura = tipo_cintura

    def mostrar_info(self):
        return f'Pantalón: {self._nombre}, Talla: {self._talla}, Tela: {self._tipo_tela}, Cintura: {self._tipo_cintura}, Precio: {self._precio}'


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_calzado):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_calzado = tipo_calzado

    def mostrar_info(self):
        return f'Zapato: {self._nombre}, Talla: {self._talla}, Tela: {self._tipo_tela}, Tipo: {self._tipo_calzado}, Precio: {self._precio}'


# Clase Tienda
class Tienda:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_productos(self):
        for producto in self._productos:
            print(producto.mostrar_info())


# Clase Carrito
class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_al_carrito(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        return sum([producto.obtener_precio() for producto in self._productos])

    def mostrar_resumen(self):
        for producto in self._productos:
            print(producto.mostrar_info())
        print(f'Total a pagar: {self.calcular_total()}')


# Ejemplo de uso
if __name__ == "__main__":
    tienda = Tienda()
    tienda.agregar_producto(Camisa("Camisa Casual", 25.00, "M", "Algodón", "Clásico"))
    tienda.agregar_producto(Pantalon("Pantalón Jeans", 35.50, "L", "Denim", "Normal"))
    tienda.agregar_producto(Zapato("Zapato Deportivo", 50.00, "42", "Sintético", "Deportivo"))

    print("Productos disponibles en la tienda:")
    tienda.mostrar_productos()

    carrito = Carrito()
    carrito.agregar_al_carrito(tienda._productos[0])  # Agregar Camisa
    carrito.agregar_al_carrito(tienda._productos[1])  # Agregar Pantalón

    print("\nResumen de la compra:")
    carrito.mostrar_resumen()
