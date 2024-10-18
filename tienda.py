from src import Producto
from src import Ropa
from src import Camisa
from src import Pantalon
from src import Zapato
from src import Tienda
from src import Carrito

def mostrar_menu():
    print("\n--- Menú de Compras ---")
    print("1. Ver productos disponibles")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito")
    print("4. Quitar producto del carrito")
    print("5. Terminar compra")
    print("6. Salir")

def main():
    tienda = Tienda()
    carrito = Carrito()

    # Agregar productos a la tienda (puedes personalizarlos)
    tienda.agregar_producto(Camisa("Camisa Casual", 25.99, "M", "Algodón", "Clásico"))
    tienda.agregar_producto(Pantalon("Pantalón Jeans", 35.50, "L", "Denim", "Normal"))
    tienda.agregar_producto(Zapato("Zapato Deportivo", 50.00, "42", "Sintético", "Deportivo"))

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nProductos disponibles:")
            tienda.mostrar_productos()
        
        elif opcion == "2":
            print("\nSelecciona el producto a agregar al carrito:")
            tienda.mostrar_productos()
            indice = int(input("Ingresa el número del producto a agregar: ")) - 1
            if 0 <= indice < len(tienda._productos):
                carrito.agregar_al_carrito(tienda._productos[indice])
                print(f"Agregado al carrito: {tienda._productos[indice]._nombre}")
            else:
                print("Número de producto no válido.")

        elif opcion == "3":
            print("\nProductos en el carrito:")
            carrito.mostrar_resumen()

        elif opcion == "4":
            print("\nSelecciona el producto a quitar del carrito:")
            carrito.mostrar_resumen()
            indice = int(input("Ingresa el número del producto a quitar: ")) - 1
            if 0 <= indice < len(carrito._productos):
                producto_quitado = carrito._productos.pop(indice)
                print(f"Quitado del carrito: {producto_quitado._nombre}")
            else:
                print("Número de producto no válido.")

        elif opcion == "5":
            print("\nFinalizando la compra...")
            carrito.mostrar_resumen()
            print("¡Gracias por tu compra!")
            break
        
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
