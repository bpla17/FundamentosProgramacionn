# DÍA 1, 2 Y 3 - BUNNY SNEAKER STORE

import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from datetime import datetime

# Inventario Inicial incluye 10 productos
inventario = [
    {"id": "001", "modelo": "Air Jordan 1",        "marca": "Nike",      "precio": 3500.00, "talla": "9",   "stock": 3,  "descripcion": "clásico atemporal"},
    {"id": "002", "modelo": "Nike Air Max 90",      "marca": "Nike",      "precio": 2800.00, "talla": "10",  "stock": 2,  "descripcion": "Diseño Moderno"},
    {"id": "003", "modelo": "Yeezy 350",           "marca": "Adidas",    "precio": 3000.00, "talla": "8.5", "stock": 5,  "descripcion": "Colorway popular"},
    {"id": "004", "modelo": "Nike Dunk Low",       "marca": "Nike",      "precio": 2500.00, "talla": "10.5","stock": 4,  "descripcion": "Comodidad premium"},
    {"id": "005", "modelo": "Adidas Ultraboost 22","marca": "Adidas",    "precio": 3800.00, "talla": "9",   "stock": 6,  "descripcion": "Retro futurista"},
    {"id": "006", "modelo": "Puma RS-X",           "marca": "Puma",      "precio": 2800.00, "talla": "11",  "stock": 2,  "descripcion": "Lujo made in USA"},
    {"id": "007", "modelo": "New Balance 990v5",   "marca": "New Balance","precio": 3900.00,"talla": "10",  "stock": 1,  "descripcion": "Icono de los 90"},
    {"id": "008", "modelo": "Jordan Retro 11",     "marca": "Nike",      "precio": 3100.00, "talla": "8",   "stock": 8,  "descripcion": "Clásico minimalista"},
    {"id": "009", "modelo": "Adidas Stan Smith",   "marca": "Adidas",    "precio": 2100.00, "talla": "9.5", "stock": 7,  "descripcion": "Leyenda al aire"},
    {"id": "010", "modelo": "Salomon XT-6",        "marca": "Salomon",   "precio": 4500.00, "talla": "10",  "stock": 3,  "descripcion": "Trail running premium"}
]

historial_ventas = []
STOCK_MINIMO = 3
boton_activo = None

# -------------------
# Funciones auxiliares
# -------------------
def validar_numero_positivo(valor, nombre_campo):
    """Validar que el valor sea un número positivo."""
    try:
        num = float(valor)
        if num <= 0:
            messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' debe ser mayor a 0.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' debe ser un número válido.")
        return None

def generar_nuevo_id():
    """Genera un nuevo ID consecutivo basado en el ID numérico más alto actual."""
    if not inventario:
        return "001"
    max_id = 0
    for item in inventario:
        try:
            num_id = int(item['id'])
            if num_id > max_id:
                max_id = num_id
        except ValueError:
            continue
    return str(max_id + 1).zfill(3)

# -------------------
# FUNCIONES PRINCIPALES
# -------------------
def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida con estadísticas rápidas"""
    global boton_activo
    texto.delete(1.0, tk.END)
    activar_boton(btn_home)

    total_modelos = len(inventario)
    total_pares = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(
        1 for v in historial_ventas
        if datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M").date() == datetime.now().date()
    )
    productos_stock_bajo = sum(1 for t in inventario if 0 < t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "      /\\_/\\  \n     (  o . o ) \n      >   ^  <  \n\n")
    texto.insert(tk.END, "--------------------------------------------------------\n\n")
    texto.insert(tk.END, "  🐰 Bienvenido a Bunny Sneaker Store 🐰\n\n")
    texto.insert(tk.END, "--------------------------------------------------------\n\n")

    texto.insert(tk.END, "RESUMEN RAPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"Modelos únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total de Pares en Stock: {total_pares}\n")
    texto.insert(tk.END, f"Ventas Registradas (Hoy): {ventas_hoy}\n")

    if productos_stock_bajo > 0:
        texto.insert(tk.END, f"¡ALERTA DE STOCK BAJO!: {productos_stock_bajo} productos necesitan reabastecimiento.\n", "alerta")
    else:
        texto.insert(tk.END, "¡Inventario en buen estado!\n")

    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")

def mostrar_inventario():
    """Muestra el listado completo del inventario."""
    texto.delete(1.0, tk.END)
    activar_boton(btn1)
    texto.insert(tk.END, "\n--- INVENTARIO COMPLETO ---\n\n")

    if not inventario:
        texto.insert(tk.END, "\n X No hay tenis en el inventario\n")
        return

    texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<25} | {'PRECIO':<12} | {'TALLA':<6} | {'MARCA':<12} | {'STOCK':<6}\n")
    texto.insert(tk.END, "-" * 80 + "\n")

    for tenis in inventario:
        linea = (f"{tenis['id']:<4} | {tenis['modelo']:<25} | ${tenis['precio']:<10,.2f} | {tenis['talla']:<6} | {tenis['marca']:<12} | {tenis['stock']:<6}")
        texto.insert(tk.END, linea)

        if tenis['stock'] > 0 and tenis['stock'] <= STOCK_MINIMO:
            texto.insert(tk.END, " → STOCK BAJO", "alerta")
        elif tenis['stock'] == 0:
            texto.insert(tk.END, " → AGOTADO", "agotado")

        texto.insert(tk.END, "\n")

def agregar_tenis():
    """Agrega un nuevo producto al inventario."""
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    modelo = simpledialog.askstring("Agregar Tenis", "1. Nombre del modelo (Obligatorio):", parent=ventana)
    if not modelo:
        return

    marca = simpledialog.askstring("Agregar Tenis", "2. Marca/Categoría (Obligatorio):", parent=ventana)
    if not marca:
        return

    precio_str = simpledialog.askstring("Agregar Tenis", "3. Precio unitario (Obligatorio):", parent=ventana)
    if not precio_str:
        return
    precio_validado = validar_numero_positivo(precio_str, "Precio")
    if precio_validado is None:
        return

    talla = simpledialog.askstring("Agregar Tenis", "4. Talla (Obligatorio):", parent=ventana)
    if not talla:
        return

    stock_str = simpledialog.askstring("Agregar Tenis", "5. Cantidad inicial (Stock) (Obligatorio):", parent=ventana)
    if not stock_str:
        return
    stock_validado = validar_numero_positivo(stock_str, "Cantidad inicial")
    if stock_validado is None:
        return

    descripcion = simpledialog.askstring("Agregar Tenis", "6. Descripción adicional (Opcional):", parent=ventana)

    nuevo_tenis = {
        "id": new_id,
        "modelo": modelo,
        "marca": marca,
        "precio": float(precio_validado),
        "talla": talla,
        "stock": int(stock_validado),
        "descripcion": descripcion if descripcion else "sin descripción"
    }

    inventario.append(nuevo_tenis)
    messagebox.showinfo("Éxito", f"'{modelo}' agregado con ID {new_id} al inventario.")
    mostrar_inventario()

def buscar_tenis():
    """Busca un producto en el inventario por ID, Modelo, Marca o Talla"""
    activar_boton(btn4)

    if not inventario:
        messagebox.showwarning("Sin inventario", "No hay productos disponibles para buscar", parent=ventana)
        return

    criterio_busqueda = simpledialog.askstring("Buscar Tenis", "Busca por: ID, Modelo, Marca o Talla:", parent=ventana)
    if not criterio_busqueda:
        return

    criterio = criterio_busqueda.lower()
    resultados = []

    for tenis in inventario:
        if (criterio in tenis['id'].lower()
            or criterio in tenis['modelo'].lower()
            or criterio in tenis['marca'].lower()
            or criterio in tenis['talla'].lower()):
            resultados.append(tenis)

    texto.delete(1.0, tk.END)
    texto.insert(tk.END, f"=== RESULTADOS DE BÚSQUEDA: '{criterio_busqueda}' ===\n\n")

    if not resultados:
        texto.insert(tk.END, "X No se encontraron resultados\n")
        return

    texto.insert(tk.END, f"Se encontraron {len(resultados)} producto(s):\n\n")
    texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<25} | {'PRECIO':<12} | {'TALLA':<6} | {'MARCA':<12} | {'STOCK':<6}\n")
    texto.insert(tk.END, "-" * 80 + "\n")

    for tenis in resultados:
        linea = f"{tenis['id']:<4} | {tenis['modelo']:<25} | ${tenis['precio']:<10,.2f} | {tenis['talla']:<6} | {tenis['marca']:<12} | {tenis['stock']:<6}"
        texto.insert(tk.END, linea)
        if tenis['stock'] > 0 and tenis['stock'] <= STOCK_MINIMO:
            texto.insert(tk.END, " → STOCK BAJO", "alerta")
        elif tenis['stock'] == 0:
            texto.insert(tk.END, " → AGOTADO", "agotado")
        texto.insert(tk.END, "\n")

def vender_tenis():
    """Registra una venta de productos y actualiza el inventario."""
    activar_boton(btn3)

    if not inventario:
        messagebox.showwarning("Sin inventario", "No hay productos disponibles para vender", parent=ventana)
        return

    opciones = "\n".join([f"{i+1}. ID:{t['id']} - {t['modelo']} ({t['marca']}) - Stock: {t['stock']}" for i, t in enumerate(inventario)])
    try:
        seleccion = simpledialog.askinteger("Vender Tenis", f"Selecciona el NÚMERO del producto a vender:\n\n{opciones}", parent=ventana)
    except Exception:
        seleccion = None

    if seleccion is None or seleccion < 1 or seleccion > len(inventario):
        if seleccion is not None:
            messagebox.showerror("Error", "Selección inválida o cancelada.")
        return

    tenis_a_vender = inventario[seleccion - 1]

    if tenis_a_vender['stock'] <= 0:
        messagebox.showwarning("Sin stock", "Este modelo está agotado.", parent=ventana)
        return

    # pedir cantidad como entero
    try:
        cantidad = simpledialog.askinteger("Vender Tenis", f"¿Cuántas unidades de '{tenis_a_vender['modelo']}' quieres vender?", parent=ventana, minvalue=1)
    except Exception:
        cantidad = None

    if cantidad is None:
        return

    if cantidad <= 0:
        messagebox.showerror("Error de venta", "La cantidad debe ser mayor que 0.", parent=ventana)
        return

    if cantidad > tenis_a_vender['stock']:
        messagebox.showerror("Error de venta", f"Solo hay {tenis_a_vender['stock']} unidades disponibles. No se puede vender {cantidad}", parent=ventana)
        return

    monto_total = cantidad * tenis_a_vender['precio']
    tenis_a_vender['stock'] -= cantidad

    registro_venta = {
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "id_producto": tenis_a_vender['id'],
        "modelo": tenis_a_vender['modelo'],
        "cantidad": cantidad,
        "precio_unitario": tenis_a_vender['precio'],
        "total": monto_total
    }

    historial_ventas.append(registro_venta)

    messagebox.showinfo("Venta Registrada", f"Se vendieron {cantidad} unidades de '{tenis_a_vender['modelo']}'\nMonto total: ${monto_total:,.2f}")
    mostrar_resumen_venta(registro_venta)

def mostrar_resumen_venta(venta):
    """Muestra el resumen detallado de la venta realizada."""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "=VENTA REGISTRADA =\n\n")

    texto.insert(tk.END, "DETALLES DE LA VENTA:\n", "titulo")
    texto.insert(tk.END, f"Fecha y Hora: {venta['fecha']}\n")
    texto.insert(tk.END, f"Producto ID: {venta['id_producto']}\n")
    texto.insert(tk.END, f"Nombre: {venta['modelo']}\n")
    texto.insert(tk.END, f"Cantidad: {venta['cantidad']} unidades\n")
    texto.insert(tk.END, f"Precio Unitario: ${venta['precio_unitario']:,.2f}\n")
    texto.insert(tk.END, f"TOTAL: ${venta['total']:,.2f}\n", "total")
    texto.insert(tk.END, "\n¡La venta ha sido registrada exitosamente!\n")

# -------------------
# UI: botones y eventos
# -------------------
def activar_boton(boton):
    """Actualiza el color del botón activo."""
    global boton_activo
    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg="#000000")
    if boton:
        boton.config(bg="#ff4500")
        boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg="#333333")

def on_leave(e, boton):
    if boton != boton_activo:
        boton.config(bg="#000000")

# -------------------
# INTERFAZ GRAFICA
# -------------------
ventana = tk.Tk()
ventana.title("₍ᐢ. .ᐢ₎ Bunny Sneaker Store ₍ᐢ. .ᐢ₎ ")
ventana.geometry("1200x800")
ventana.configure(bg="#f5f5f5")

boton_activo = None

titulo = tk.Label(ventana, text="₍ᐢ. .ᐢ₎ BUNNY SNEAKER STORE ₍ᐢ. .ᐢ₎",
                  font=("Helvetica", 32, "bold"), bg="#f5f5f5", fg="#000000")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS",
                     font=("Helvetica", 12), bg="#f5f5f5", fg="#666666")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)

btn_style = {"font": ("Albert Sans", 11, "bold"), "bg": "#000000", "fg": "white",
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)

btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn1.grid(row=0, column=1, padx=8)

btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_tenis, **btn_style)
btn2.grid(row=0, column=2, padx=8)

btn3 = tk.Button(frame_botones, text="VENDER", command=vender_tenis, **btn_style)
btn3.grid(row=0, column=3, padx=8)

btn4 = tk.Button(frame_botones, text="BUSCAR", command=buscar_tenis, **btn_style)
btn4.grid(row=0, column=4, padx=8)

for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

texto = scrolledtext.ScrolledText(ventana,
                                  font=("Open Sans", 11),
                                  bg="#ffffff", fg="#000000",
                                  height=18,
                                  padx=20, pady=20,
                                  relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground="#000000")
texto.tag_config("alerta", background="#ffe5e5", foreground="#ff4500", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", background="#fddede", foreground="#cc0000", font=("Open Sans", 11, "bold"))
texto.tag_config("total", font=("Open Sans", 11, "bold"), foreground="#008000")

footer = tk.Label(ventana, text="© 2025 Bunny Sneaker Store | Día 1, 2 y 3 - Completo",
                  font=("Helvetica", 10), bg="#f5f5f5", fg="#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()