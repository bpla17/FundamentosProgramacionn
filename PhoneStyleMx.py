import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from datetime import datetime

# ==========================================================
#   📱 INVENTARIO INICIAL – PhoneStyleMx
#   Precios reales basados en Apple México (2025)
# ==========================================================

inventario = [
    {"id": "001", "modelo": "iPhone 16 Pro Max 256 GB",   "marca": "Apple", "precio": 28999.00, "categoria": "iPhone",      "stock": 5,  "descripcion": "Titanium – Chip A18 Pro"},
    {"id": "002", "modelo": "iPhone 16 Pro 256 GB",       "marca": "Apple", "precio": 25999.00, "categoria": "iPhone",      "stock": 4,  "descripcion": "Compacto – Titanium"},
    {"id": "003", "modelo": "iPhone 15 128 GB",           "marca": "Apple", "precio": 17999.00, "categoria": "iPhone",      "stock": 6,  "descripcion": "Dynamic Island – USB-C"},
    {"id": "004", "modelo": "AirPods Pro 2 USB-C",        "marca": "Apple", "precio": 4999.00,  "categoria": "AirPods",     "stock": 10, "descripcion": "Cancelación de ruido avanzada"},
    {"id": "005", "modelo": "AirPods 3ra Generación",     "marca": "Apple", "precio": 3999.00,  "categoria": "AirPods",     "stock": 7,  "descripcion": "Audio espacial"},
    {"id": "006", "modelo": "Apple Watch Series 10 41mm", "marca": "Apple", "precio": 8999.00,  "categoria": "Watch",       "stock": 4,  "descripcion": "Pantalla más grande"},
    {"id": "007", "modelo": "Funda iPhone 16 Pro Max",     "marca": "Apple", "precio": 999.00,   "categoria": "Accesorio",  "stock": 15, "descripcion": "Funda de silicón original"},
    {"id": "008", "modelo": "Cable USB-C Apple Original", "marca": "Apple", "precio": 499.00,   "categoria": "Accesorio",  "stock": 20, "descripcion": "Carga rápida"},
    {"id": "009", "modelo": "Cargador 20W Apple",         "marca": "Apple", "precio": 599.00,   "categoria": "Accesorio",  "stock": 25, "descripcion": "Carga rápida oficial"},
    {"id": "010", "modelo": "AirTag Individual",          "marca": "Apple", "precio": 749.00,   "categoria": "Accesorio",  "stock": 18, "descripcion": "Encuentra tus objetos rápido"}
]

historial_ventas = []
STOCK_MINIMO = 3
boton_activo = None


# ==========================================================
#    VALIDACIONES / FUNCIONES AUXILIARES
# ==========================================================

def validar_numero_positivo(valor, nombre_campo):
    """Valida que el valor sea un número positivo."""
    try:
        num = float(valor)
        if num <= 0:
            messagebox.showerror("Error", f"El campo '{nombre_campo}' debe ser mayor a 0.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error", f"El campo '{nombre_campo}' debe ser un número válido.")
        return None


def generar_nuevo_id():
    """Genera un nuevo ID consecutivo basado en los ya existentes."""
    if not inventario:
        return "001"
    max_id = max(int(item["id"]) for item in inventario)
    return str(max_id + 1).zfill(3)


# ==========================================================
#             PANTALLA DE BIENVENIDA
# ==========================================================

def mostrar_bienvenida():
    global boton_activo
    texto.delete(1.0, tk.END)
    activar_boton(btn_home)

    total_productos = len(inventario)
    total_stock = sum(t["stock"] for t in inventario)
    ventas_hoy = sum(
        1 for v in historial_ventas
        if datetime.strptime(v["fecha"], "%d/%m/%Y %H:%M").date() == datetime.now().date()
    )
    productos_stock_bajo = sum(1 for i in inventario if 0 < i["stock"] <= STOCK_MINIMO)

    texto.insert(tk.END, "       📱✨\n")
    texto.insert(tk.END, "   Bienvenido a\n")
    texto.insert(tk.END, "   ⭐ PhoneStyleMx ⭐\n\n")

    texto.insert(tk.END, "------ RESUMEN ------\n\n", "titulo")
    texto.insert(tk.END, f"Modelos disponibles: {total_productos}\n")
    texto.insert(tk.END, f"Stock total: {total_stock}\n")
    texto.insert(tk.END, f"Ventas registradas hoy: {ventas_hoy}\n")

    if productos_stock_bajo > 0:
        texto.insert(tk.END,
                     f"⚠ Hay {productos_stock_bajo} productos con stock bajo.\n",
                     "alerta")
    else:
        texto.insert(tk.END, "✔ Todo en orden.\n")

    texto.insert(tk.END, "\nSelecciona una opción del menú.\n")


# ==========================================================
#             MOSTRAR INVENTARIO
# ==========================================================

def mostrar_inventario():
    texto.delete(1.0, tk.END)
    activar_boton(btn1)

    texto.insert(tk.END, "--- INVENTARIO PhoneStyleMx ---\n\n", "titulo")

    texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<30} | {'PRECIO':<10} | {'CATEGORIA':<12} | {'STOCK':<6}\n")
    texto.insert(tk.END, "-" * 80 + "\n")

    for item in inventario:
        linea = f"{item['id']:<4} | {item['modelo']:<30} | ${item['precio']:<9.2f} | {item['categoria']:<12} | {item['stock']:<6}"
        texto.insert(tk.END, linea)

        if item["stock"] == 0:
            texto.insert(tk.END, " → AGOTADO", "agotado")
        elif item["stock"] <= STOCK_MINIMO:
            texto.insert(tk.END, " → STOCK BAJO", "alerta")

        texto.insert(tk.END, "\n")


# ==========================================================
#             AGREGAR NUEVO PRODUCTO
# ==========================================================

def agregar_producto():
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    modelo = simpledialog.askstring("Agregar Producto", "1. Nombre del modelo:", parent=ventana)
    if not modelo: return

    categoria = simpledialog.askstring("Agregar Producto", "2. Categoría (iPhone, AirPods, Accesorio…):", parent=ventana)
    if not categoria: return

    precio = simpledialog.askstring("Agregar Producto", "3. Precio:", parent=ventana)
    precio = validar_numero_positivo(precio, "Precio")
    if precio is None: return

    stock = simpledialog.askstring("Agregar Producto", "4. Stock inicial:", parent=ventana)
    stock = validar_numero_positivo(stock, "Stock")
    if stock is None: return

    descripcion = simpledialog.askstring("Agregar Producto", "5. Descripción:", parent=ventana)

    nuevo_item = {
        "id": new_id,
        "modelo": modelo,
        "marca": "Apple",
        "precio": float(precio),
        "categoria": categoria,
        "stock": int(stock),
        "descripcion": descripcion if descripcion else "Sin descripción"
    }

    inventario.append(nuevo_item)
    messagebox.showinfo("Éxito", f"'{modelo}' agregado correctamente.")
    mostrar_inventario()


# ==========================================================
#    BÚSQUEDA DE PRODUCTOS
# ==========================================================

def buscar_producto():
    activar_boton(btn4)

    criterio = simpledialog.askstring("Buscar", "Ingresa ID, Modelo o Categoría:", parent=ventana)
    if not criterio: return

    criterio = criterio.lower()
    resultados = [
        i for i in inventario
        if criterio in i["id"].lower() or criterio in i["modelo"].lower() or criterio in i["categoria"].lower()
    ]

    texto.delete(1.0, tk.END)
    texto.insert(tk.END, f"Resultados de búsqueda para: '{criterio}'\n\n", "titulo")

    if not resultados:
        texto.insert(tk.END, "No se encontró nada.\n")
        return

    for item in resultados:
        texto.insert(tk.END, f"• {item['modelo']} – ${item['precio']:,.2f} – Stock: {item['stock']}\n")


# ==========================================================
#           REGISTRAR VENTA
# ==========================================================

def vender_producto():
    activar_boton(btn3)

    opciones = "\n".join([f"{i+1}. {p['modelo']}  (${p['precio']}) – Stock: {p['stock']}"
                          for i, p in enumerate(inventario)])

    seleccion = simpledialog.askinteger("Vender", f"Selecciona producto:\n\n{opciones}", parent=ventana)
    if not seleccion or seleccion < 1 or seleccion > len(inventario):
        return

    producto = inventario[seleccion - 1]

    cantidad = simpledialog.askinteger("Cantidad", "¿Cuántas unidades quieres vender?", parent=ventana, minvalue=1)
    if not cantidad: return

    if cantidad > producto["stock"]:
        messagebox.showerror("Error", "No hay suficiente stock.")
        return

    total = cantidad * producto["precio"]
    producto["stock"] -= cantidad

    historial_ventas.append({
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "modelo": producto["modelo"],
        "cantidad": cantidad,
        "total": total
    })

    messagebox.showinfo("Venta registrada", f"Venta realizada por ${total:,.2f}")
    mostrar_inventario()


# ==========================================================
#           BOTONES Y HOVERS
# ==========================================================

def activar_boton(boton):
    global boton_activo
    for b in [btn_home, btn1, btn2, btn3, btn4]:
        b.config(bg="#000000")
    boton.config(bg="#007bff")
    boton_activo = boton


def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg="#0056c9")


def on_leave(e, boton):
    if boton != boton_activo:
        boton.config(bg="#000000")


# ==========================================================
#           INTERFAZ TKINTER
# ==========================================================

ventana = tk.Tk()
ventana.title("📱 PhoneStyleMx – Gestión de Inventario")
ventana.geometry("1200x800")
ventana.configure(bg="#f8f8f8")

titulo = tk.Label(ventana, text="📱 PhoneStyleMx 📱",
                  font=("Helvetica", 34, "bold"),
                  bg="#f8f8f8", fg="#000000")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="Sistema de Inventario, Ventas y Gestión",
                     font=("Helvetica", 13), bg="#f8f8f8", fg="#555555")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f8f8f8")
frame_botones.pack(pady=20)

btn_style = {
    "font": ("Helvetica", 11, "bold"),
    "bg": "#000000",
    "fg": "white",
    "width": 12,
    "height": 2,
    "cursor": "hand2",
    "relief": tk.FLAT
}

btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_producto, **btn_style)
btn3 = tk.Button(frame_botones, text="VENDER", command=vender_producto, **btn_style)
btn4 = tk.Button(frame_botones, text="BUSCAR", command=buscar_producto, **btn_style)

btn_home.grid(row=0, column=0, padx=10)
btn1.grid(row=0, column=1, padx=10)
btn2.grid(row=0, column=2, padx=10)
btn3.grid(row=0, column=3, padx=10)
btn4.grid(row=0, column=4, padx=10)

for b in [btn_home, btn1, btn2, btn3, btn4]:
    b.bind("<Enter>", lambda e, btn=b: on_enter(e, btn))
    b.bind("<Leave>", lambda e, btn=b: on_leave(e, btn))

texto = scrolledtext.ScrolledText(ventana,
                                  font=("Open Sans", 11),
                                  bg="#ffffff", fg="#000000",
                                  height=18,
                                  padx=20, pady=20)
texto.pack(padx=30, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 12, "bold"), foreground="#000000")
texto.tag_config("alerta", foreground="#d9534f", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", foreground="#b30000", font=("Open Sans", 11, "bold"))

footer = tk.Label(ventana,
                  text="© 2025 PhoneStyleMx – Inventario, Ventas y Gestión",
                  font=("Helvetica", 10),
                  bg="#f8f8f8",
                  fg="#777777")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()
