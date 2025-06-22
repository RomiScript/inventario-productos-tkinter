import tkinter as tk
from tkinter import messagebox

# ----- Lógica de productos -----
class Producto:
    def __init__(self, id, nombre, precio, cantidad):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f'{self.nombre} (ID: {self.id}) - Precio: ${self.precio} - Cantidad: {self.cantidad}'

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id in self.productos:
            self.productos[producto.id].cantidad += producto.cantidad
        else:
            self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            return True
        return False

    def obtener_productos(self):
        return [str(p) for p in self.productos.values()]

# ----- Interfaz gráfica -----
inventario = Inventario()

def agregar():
    try:
        id = int(entry_id.get())
        nombre = entry_nombre.get()
        precio = float(entry_precio.get())
        cantidad = int(entry_cantidad.get())

        producto = Producto(id, nombre, precio, cantidad)
        inventario.agregar_producto(producto)

        messagebox.showinfo("Éxito", "Producto agregado correctamente.")
        actualizar_lista()
        limpiar_entradas()
    except ValueError:
        messagebox.showerror("Error", "Verificá los campos. Deben ser valores numéricos válidos.")

def eliminar():
    try:
        id = int(entry_id.get())
        if inventario.eliminar_producto(id):
            messagebox.showinfo("Éxito", f"Producto con ID {id} eliminado.")
            actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Producto no encontrado.")
    except ValueError:
        messagebox.showerror("Error", "ID debe ser un número.")

def actualizar_lista():
    lista_productos.delete(0, tk.END)
    for p in inventario.obtener_productos():
        lista_productos.insert(tk.END, p)

def limpiar_entradas():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)

# ----- Construcción de ventana -----
root = tk.Tk()
root.title("Inventario de Productos")
root.geometry("500x500")
root.config(bg="#ECEFF1")

# Entradas
tk.Label(root, text="ID:", bg="#ECEFF1").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Nombre:", bg="#ECEFF1").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Precio:", bg="#ECEFF1").pack()
entry_precio = tk.Entry(root)
entry_precio.pack()

tk.Label(root, text="Cantidad:", bg="#ECEFF1").pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

# Botones
tk.Button(root, text="Agregar Producto", command=agregar, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Eliminar por ID", command=eliminar, bg="#F44336", fg="white").pack(pady=5)

# Lista de productos
tk.Label(root, text="Inventario:", bg="#ECEFF1").pack(pady=10)
lista_productos = tk.Listbox(root, width=60)
lista_productos.pack()

root.mainloop()



