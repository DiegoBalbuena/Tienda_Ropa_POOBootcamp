# Tienda de Ropa - Proyecto POO

Este proyecto es una aplicación de compra de ropa desarrollada en Python utilizando Programación Orientada a Objetos (POO). El sistema permite a los usuarios seleccionar diferentes ítems de ropa y procesar compras, aplicando los conceptos fundamentales de POO.

## Descripción del Proyecto

El programa permite a los usuarios seleccionar productos de categorías como camisas, pantalones y zapatos. Utiliza clases para representar los productos y la tienda, implementando los cuatro pilares de la POO: encapsulamiento, herencia, polimorfismo y abstracción.

### Objetivos

- Aplicar los cuatro pilares de la Programación Orientada a Objetos (POO).
- Practicar el uso de constructores, métodos, objetos y clases.
- Implementar un sistema básico de compra de ropa.
- Fomentar la reutilización de código y la escalabilidad.
- Comprender la relación entre clases padre e hijo y la sobrescritura de métodos.

## Estructura del Proyecto

El proyecto contiene las siguientes clases:

- `Producto`: Clase base que representa un producto general.
- `Ropa`: Clase que hereda de `Producto` y añade características específicas de la ropa.
- `Camisa`, `Pantalon`, `Zapato`: Clases específicas que heredan de `Ropa` y añaden atributos particulares.
- `Tienda`: Clase que maneja los productos disponibles y las compras.
- `Carrito`: Clase que almacena los productos seleccionados.

## Ejemplo de Uso
Al ejecutar el programa, se mostrarán los productos disponibles en la tienda. El usuario puede agregar productos al carrito y ver un resumen de la compra, incluyendo el total a pagar.

## Interacción con el Usuario
El sistema permite seleccionar uno o más productos de un menú, almacenarlos en un carrito y mostrar un resumen al finalizar la compra.

## Requisitos
Python 3.x
No se requieren librerías externas.
