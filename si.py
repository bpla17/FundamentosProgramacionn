#Librerias
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
from tkinter import simpledialog

# Inventario Inicial incluye 10 productos
inventario = [
    {"id": "001", "modelo": "Air Jordan 1",      "marca": "Nike",        "precio": 3500.00, "talla": "9",   "stock": 3, "descripcion": "Clásico atemporal"},
    {"id": "002", "modelo": "Yeezy 350",         "marca": "Adidas",      "precio": 4200.00, "talla": "10", "stock": 2, "descripcion": "Diseño moderno"},
    {"id": "003", "modelo": "Nike Dunk Low",     "marca": "Nike",        "precio": 2800.00, "talla": "8.5", "stock": 5, "descripcion": "Colorway popular"},
    {"id": "004", "modelo": "Adidas Ultraboost 22", "marca": "Adidas",   "precio": 3200.00, "talla": "10.5","stock": 4, "descripcion": "Comodidad premium"},
    {"id": "005", "modelo": "Puma RS-X", "marca": "Puma",        "precio": 2500.00, "talla": "9",   "stock": 6, "descripcion": "Retro futurista"},
    {"id": "006", "modelo": "New Balance 990v6","marca": "New Balance", "precio": 3800.00, "talla": "11",  "stock": 2, "descripcion": "Lujo made in USA"},
    {"id": "007", "modelo": "Jordan Retro 11", "marca": "Nike", "precio": 3900.00, "talla": "10",  "stock": 1, "descripcion": "Icónico de los 90s"},
    {"id": "008", "modelo": "Adidas Stan Smith","marca": "Adidas",       "precio": 1800.00, "talla": "8",  "stock": 8, "descripcion": "Clásico minimalista"},
    {"id": "009", "modelo": "Nike Air Max 90",  "marca": "Nike",         "precio": 3100.00, "talla": "9.5", "stock": 7, "descripcion": "Leyenda del aire"},
    {"id": "010", "modelo": "Salomon XT-6",     "marca": "Salomon",      "precio": 4500.00, "talla": "10",  "stock": 3, "descripcion": "Trail running premium"},
]
   
historial_ventas = [] 
STOCK_MINIMO = 3


def mostrar_bienvenida():
    total_modelos = len(inventario)
    total_pares = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(1 for v in historial_ventas
                     if datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M").date() == datetime.now().date())
    productos_stock_bajo = sum(1 for t in inventario if t['stock'] > 0 and t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "      /\\_/\\  \n")
    texto.insert(tk.END, "     ( o.o )   >  ^^\n")
    texto.insert(tk.END, "      > ^ <\n\n")
    texto.insert(tk.END, "Bienvenido a Bunny Sneaker Store \\n\\n")

    texto.insert(tk.END, "-----------------------------\n\n")
    texto.insert(tk.END, "RESUMEN RÁPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"• Modelos Únicos: {total_modelos}\n")
    texto.insert(tk.END, f"• Total de Pares en Stock: {total_pares}\n")
    texto.insert(tk.END, f"• Ventas Registradas (Hoy): {ventas_hoy}\n\n")

    if productos_stock_bajo > 0:
        texto.insert(tk.END,
                     f"ALERTA DE STOCK BAJO: {productos_stock_bajo} productos necesitan reabastecimiento.\n",
                     "alerta")
    else:
        texto.insert(tk.END, "Inventario en buen estado\n")

    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")


def validar_numero_positivo(valor, nombre_campo):
    """Valida que el valor sea un número positivo."""
    try:
        num = float(valor)
        if num < 0:
            messagebox.showerror("Error de Validación",
                                 f"El campo '{nombre_campo}' no puede ser negativo.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error de Validación",
                             f"El campo '{nombre_campo}' debe ser un número válido.")
        return None


def generar_nuevo_id():
    """Genera un nuevo ID consecutivo basado en el ID más alto actual."""
    if not inventario:
        return "001"

    max_id = 0
    for tenis in inventario:
        try:
            num_id = int(tenis['id'])
            if num_id > max_id:
                max_id = num_id
        except ValueError:
            continue

    return str(max_id + 1).zfill(3)


def mostrar_inventario():
    """Muestra el listado completo del inventario."""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "=== INVENTARIO COMPLETO ===\n\n", "titulo")
    activar_boton(btn1)

    if not inventario:
        texto.insert(tk.END, "X No hay tenis en el inventario\n")
    else:
        texto.insert(tk.END,
                     f"{'ID':<4} | {'MODELO':<25} | {'PRECIO':<10} | {'TALLA':<6} | {'MARCA':<10} | {'STOCK':<5}\n")
        texto.insert(tk.END, "-" * 70 + "\n")

        for tenis in inventario:
            linea = f"{tenis['id']:<4} | {tenis['modelo']:<25} | ${tenis['precio']:<9.0f} | {tenis['talla']:<6} | {tenis['marca']:<10} | {tenis['stock']}"
            texto.insert(tk.END, linea + "\n")

            if tenis['stock'] > 0 and tenis['stock'] <= STOCK_MINIMO:
                texto.insert(tk.END, "  → STOCK BAJO\n", "alerta")
            elif tenis['stock'] == 0:
                texto.insert(tk.END, "  → AGOTADO\n", "agotado")

        texto.insert(tk.END, "\n Usa el botón 'AGREGAR' para incorporar nuevos productos.\n")


def agregar_tenis():
    """Agrega un nuevo producto al inventario."""
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    modelo = simpledialog.askstring("Agregar Tenis", "1. Nombre del modelo (Obligatorio):", parent=ventana)
    if not modelo: return

    marca = simpledialog.askstring("Agregar Tenis", "2. Marca/Categoría (Obligatorio):", parent=ventana)
    if not marca: return

    precio_str = simpledialog.askstring("Agregar Tenis", "3. Precio unitario (Obligatorio):", parent=ventana)
    if not precio_str: return
    precio_validado = validar_numero_positivo(precio_str, "Precio")
    if precio_validado is None: return

    talla = simpledialog.askstring("Agregar Tenis", "4. Talla (Obligatorio):", parent=ventana)
    if not talla: return

    stock_str = simpledialog.askstring("Agregar Tenis", "5. Cantidad inicial (Stock) (Obligatorio):", parent=ventana)
    if not stock_str: return
    stock_validado = validar_numero_positivo(stock_str, "Cantidad inicial")
    if stock_validado is None: return

    descripcion = simpledialog.askstring("Agregar Tenis", "6. Descripción adicional (Opcional):", parent=ventana)

    nuevo_tenis = {
        "id": new_id,
        "modelo": modelo,
        "marca": marca,
        "precio": float(precio_validado),
        "talla": talla,
        "stock": int(stock_validado),
        "descripcion": descripcion if descripcion else "Sin descripción"
    }

    inventario.append(nuevo_tenis)

    messagebox.showinfo("Éxito", f"✔ {modelo} agregado con ID {new_id} al inventario.")
    mostrar_inventario()


def activar_boton(boton):
    """Actualiza el color del botón activo."""
    global boton_activo

    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg="#000000")

    if boton:
        boton.config(bg="#006fee")
        boton_activo = boton


def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg="#006fee")


def on_leave(e, boton):
    if boton != boton_activo:
        boton.config(bg="#000000")


ventana = tk.Tk()
ventana.title("(｡◕‿◕｡) Bunny Sneaker Store (｡◕‿◕｡)")
ventana.geometry("1200x800")
ventana.configure(bg="#f5f5f5")

boton_activo = None

titulo = tk.Label(ventana, text="(｡◕‿◕｡) BUNNY SNEAKER STORE (｡◕‿◕｡)",
                  font=("Albert Sans", 32, "bold"), bg="#f5f5f5", fg="#000000")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE VENTAS E INVENTARIO",
                     font=("Albert Sans", 12), bg="#f5f5f5", fg="#666666")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)

btn_style = {"font": ("Albert Sans", 11, "bold"), "bg": "#000000", "fg": "white",
            "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

# Botón HOME
btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)

# INVENTARIO
btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn1.grid(row=0, column=1, padx=8)

# AGREGAR
btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_tenis, **btn_style)
btn2.grid(row=0, column=2, padx=8)

# VENDER
btn3 = tk.Button(frame_botones, text="VENDER", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 3 (Miércoles)"), **btn_style)
btn3.grid(row=0, column=3, padx=8)

# BUSCAR
btn4 = tk.Button(frame_botones, text="BUSCAR", command=lambda: messagebox.showinfo("Info", "Función disponible en Día 3 (Miércoles)"), **btn_style)
btn4.grid(row=0, column=4, padx=8)

# Hover
for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

# Cuadro de texto
texto = scrolledtext.ScrolledText(ventana,
                                  font=("Open Sans", 11),
                                  bg="#ffffff",
                                  fg="#000000",
                                  height=18,
                                  padx=20, pady=20,
                                  relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

# Tags
texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground="#000000")
texto.tag_config("alerta", background="#ffeecc", foreground="#006fee", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", background="#ffdede", foreground="#006fee", font=("Open Sans", 11, "bold"))

# Footer
footer = tk.Label(ventana, text="© 2025 Bunny Sneaker Store | DÍA 2 (MARTES) - Botón Inventario y Agregar Productos",
                  font=("Helvetica", 10), bg="#f5f5f5", fg="#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()
