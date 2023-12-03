import tkinter as tk
from tkinter import ttk

def konversi_suhu():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_hasil["text"] = f"Hasil konversi: {fahrenheit:.2f} Fahrenheit"
    except ValueError:
        label_hasil["text"] = "Masukkan suhu dalam angka!"

# Membuat instance dari Tkinter
root = tk.Tk()
root.title("Konverter Suhu")

# Menyesuaikan warna latar belakang
root.configure(bg="#3498db") 

# Mengatur tata letak dan gaya
root.geometry("400x300")
root.resizable(width=False, height=False)  

style = ttk.Style()
style.configure("TButton", padding=5, relief="flat", background="#2ecc71", foreground="white")
style.configure("TLabel", padding=5, background="#3498db", foreground="#ffffff")

# Membuat dan menata widget
label_celsius = ttk.Label(root, text="Masukkan suhu Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_celsius = ttk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

button_konversi = ttk.Button(root, text="Konversi", command=konversi_suhu)
button_konversi.grid(row=1, column=0, columnspan=2, pady=10)

label_hasil = ttk.Label(root, text="")
label_hasil.grid(row=2, column=0, columnspan=2, pady=10)

# Menjalankan loop utama
root.mainloop()