import random # mengimpor modul random dari library 
import string # mengimpor modul string dari library
import tkinter as tk # mengimpor modul tkinter dan memberikan alias tk ke modul 
from tkinter import messagebox # mengimpor fungsi messagebox dari modul tkinter.

def open_password_generator(): # deklarasi untuk sebuah fungsi membuka aplikasi password generator
    root.destroy() # memanggil metode destroy() pada objek root
    password_generator() # membuka jendela baru untuk menghasilkan password dengan memanggil fungsi

def password_generator(): # deklarasi untuk sebuah fungsi membuat jendela aplikasi password generator 
    
    def generate_password(): # deklarasi untuk sebuah fungsi dipanggil ketika tombol "Generate" dijepret oleh pengguna
        
        length = length_entry.get() # mengambil nilai yang dimasukkan oleh pengguna pada length_entry dan menyimpannya dalam variabel length
        try:
            length = int(length) # nilai length dikonversi menjadi integer 
            if length > 10: # memeriksa apakah panjang password yang dimasukkan oleh pengguna lebih besar dari 10
                messagebox.showerror("Error", "Panjang password maksimal adalah 10!")
            else:
                characters = string.ascii_letters + string.digits + string.punctuation # membuat string characters yang berisi kombinasi
                password = ''.join(random.choice(characters) for _ in range(length)) # menggunakan perulangan for untuk memilih karakter secara acak
                password_label.config(text="Password: " + password) # Mengatur teks label
        except ValueError:
            messagebox.showerror("Error", "Silahkan masukkan angka sebagai panjang password!")
    
    # Inisialisasi jendela utama (root) menggunakan tk.Tk()        
    root = tk.Tk()
    root.title("UAS PBO KELOMPOK 14 - Password Generator")

    # Background color
    root.configure(bg="black")

    # Header
    header_label = tk.Label(root, text="Welcome to Random Password Generator", font=("Times New Roman", 20), bg="black", fg="white")
    header_label.pack(pady=20)

    # Password Length
    length_frame = tk.Frame(root, bg="black") # Membuat objek frame 
    length_frame.pack() # Mengatur tata letak (layout) frame

    length_label = tk.Label(length_frame, text="Silahkan masukkan angka panjang password! : ", font=("Times New Roman", 10), bg="black", fg="white") # Membuat objek label
    length_label.pack(side=tk.LEFT, padx=10) # Mengatur tata letak (layout) label 

    length_entry = tk.Entry(length_frame, font=("Times New Roman", 10)) # Membuat objek Entry (length_entry) 
    length_entry.pack(side=tk.LEFT, padx=10) # Mengatur tata letak (layout) input field 

    # Generate Button
    generate_button = tk.Button(root, text="Generate", font=("Times New Roman", 10), bg="gray", command=generate_password)
    generate_button.pack(pady=10)

    # Password Display
    password_label = tk.Label(root, text="Password:", font=("Times New Roman", 14), bg="black", fg="white")
    password_label.pack(pady=10)

    # Kode ini menjalankan siklus utama aplikasi Tkinter
    root.mainloop()

# Kode memeriksa apakah skrip dijalankan langsung sebagai file utama 
if __name__ == "__main__":
    root = tk.Tk() # Membuat objek root yang merupakan instance dari kelas Tk dari modul tkinter
    root.title("UAS PBO KELOMPOK 14") # Mengatur judul jendela utama aplikasi 

    # Background color
    root.configure(bg="black")

    # Header
    header_label = tk.Label(root, text="Cara Pemakaian Aplikasi", font=("Times New Roman", 20), bg="black", fg="white")
    header_label.pack(pady=20)

    # Instructions
    instructions = [
        "1. Jalankan aplikasi dengan menjalankan script ini.",
        "2. Aplikasi akan membuka jendela utama yang berisi instruksi penggunaan.",
        "3. Pada jendela utama, masukkan panjang password yang diinginkan.",
        "4. Tekan tombol 'Generate' untuk membuat password.",
        "5. Password yang dihasilkan akan ditampilkan pada jendela utama.",
        "6. Jika ingin membuat password baru, ulangi langkah 3-5.",
        "7. Tutup aplikasi dengan menutup jendela."
    ]

    # Membuat dan menampilkan beberapa label teks 
    for instruction in instructions:
        label = tk.Label(root, text=instruction, font=("Times New Roman", 12), bg="black", fg="white")
        label.pack()

    # Open Password Generator Button
    open_button = tk.Button(root, text="Buka Aplikasi", font=("Times New Roman", 12), bg="gray", command=open_password_generator)
    open_button.pack(pady=20)

    # Kode ini menjalankan siklus utama aplikasi Tkinter
    root.mainloop()
