#Nombre: Mariano Diaz
#Aplicacion API-REST

import requests

# API de productos de DummyJSON

BASE_URL= "https://dummyjson.com/products"

def mostrar_respuesta(respuesta):
    #Mostrar el codigo HTTP y los datos recibidos
    print("Codigo HTTP", respuesta.status_code)

    if respuesta.text:
        print("Respuesta JSON:")
        print(respuesta.json())
    else:
        print("la respuesta no tiene datos")


try:
    # =============================
    # 1. GET: CONSULTAR UN PRODUCTO
    # =============================

    print("\n GET --- Consultar un producto ---")
    
    respuesta = requests.get(
        f"{BASE_URL}/19",
        timeout=10
    )

    respuesta.raise_for_status()
    producto = respuesta.json()

    print("Producto", producto["title"] )
    print("Precio", producto["price"])
    print("Categoria", producto["category"])


    # ===========================
    # 2. METODO POST
    # ============================
    
    print("\n POST --- Crear un producto ---")
    
    nuevo_producto = {
        "title": "Teclado mecanico gamer",
        "price": "90000",
        "description": "Teclado gamer para juegos",
        "category": "electronics"
    }

    respuesta = requests.post(
        f"{BASE_URL}/add",
        json=nuevo_producto,
        timeout=10
    )
    
    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)
    
except requests.exceptions.Timeout:
    print("Error: se agoto el tiempo de espera")
    
    # ===========================
    # 2. METODO PUT
    # ============================
    
    print("\n PUT --- Actualizar un producto ---")
    
    producto_actualizado = {
        "title": "Notebook para desarrollar",
        "price": 590000,
        "description": "Notebook para programar",
        "category": "laptops"
    }
    
    respuesta = requests.put(
        f"{BASE_URL}/1",
        json=producto_actualizado,
        timeout=10
    )
    
    respuesta.raise_for_status()
    mostrar_respuesta(respuesta)
    
except requests.exceptions.Timeout:
    print("Error: se agoto el tiempo de espera")