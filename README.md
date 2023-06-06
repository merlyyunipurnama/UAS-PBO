# Ujian Akhir Semester-PBO
Membuat password dengan menggunakan skrip python dengan beberapa batasan seperti campuran huruf besar, huruf kecil, simbol, dan angka.

Anggota kelompok 14:
* G1A022006 - Merly Yuni Purnama
* G1A022040 - Sinta Ezra Wati Gulo 
* G1A022068 - Anugrah Herianto

## Penjelasan Source Code
```py
import random # mengimpor modul random dari library 
import string # mengimpor modul string dari library
import tkinter as tk # mengimpor modul tkinter dan memberikan alias tk ke modul 
from tkinter import messagebox # mengimpor fungsi messagebox dari modul tkinter
```

Kode di atas adalah kode untuk mengimport beberapa modul dan fungsi dari library tkinter.

* Kode ```import random``` mengimpor modul random dari library Python. Modul ini berisi fungsi-fungsi yang berkaitan dengan angka acak (random number). Dengan mengimpor modul ini, kita dapat menggunakan fungsi-fungsi seperti ```random.randint()``` untuk menghasilkan angka acak.
* Kode ```import string``` mengimpor modul string dari library Python. Modul ini berisi kumpulan fungsi-fungsi yang berkaitan dengan manipulasi string. Dengan mengimpor modul ini, kita dapat menggunakan fungsi-fungsi seperti ```string.ascii_letters``` atau ```string.digits``` untuk mendapatkan karakter alfabet atau angka.
* Kode ```import tkinter as tk``` mengimpor modul tkinter dan memberikan alias tk ke modul tersebut. Dimana tkinter adalah library standar Python untuk membuat antarmuka grafis (GUI). Dengan memberikan alias tk, kita dapat menggunakan tk sebagai prefix saat memanggil fungsi dan objek dari modul ini, misalnya ```tk.Tk()``` untuk membuat jendela utama aplikasi.
* Kode ```from tkinter import messagebox``` mengimpor fungsi messagebox dari modul tkinter. Fungsi messagebox digunakan untuk menampilkan kotak pesan pop-up dengan berbagai jenis pesan, seperti pesan informasi, peringatan, atau kesalahan kepada pengguna. 

```py
def open_password_generator(): # deklarasi untuk sebuah fungsi membuka aplikasi password generator
    root.destroy() # memanggil metode destroy() pada objek root
    password_generator() # membuka jendela baru untuk menghasilkan password dengan memanggil fungsi
```

* Kode diatas adalah fungsi ```open_password_generator()``` untuk menggabungkan langkah-langkah untuk menutup jendela utama aplikasi yang ada dan membuka jendela baru untuk menghasilkan password dalam aplikasi password generator.
* Kode ```root.destroy()``` yang memanggil metode ```destroy()``` pada objek root. root adalah objek utama dalam aplikasi GUI, yang telah dibuat sebelumnya menggunakan modul tkinter. Metode ```destroy()``` digunakan untuk menutup jendela utama aplikasi. Dengan memanggil ```root.destroy()```, fungsi ini bertujuan untuk menutup jendela utama aplikasi sebelum membuka jendela baru.
* Kode ```password_generator()``` yang memanggil fungsi ```password_generator()```. Tujuan dari pemanggilan ini adalah untuk membuka jendela baru yang khusus untuk menghasilkan password. Fungsi ```password_generator()``` kemungkinan besar akan menampilkan antarmuka pengguna atau melakukan operasi yang relevan dengan menghasilkan password secara interaktif.

```py
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
```
Kode tersebut merupakan definisi dari fungsi   ```password_generator()  ```, yang bertanggung jawab untuk membuat jendela aplikasi pembuat password. Berikut adalah penjelasan untuk setiap baris kode dalam fungsi tersebut:
*  ```def password_generator()``` bertujuan untuk membuat jendela aplikasi pembuat password.
*   ```def generate_password()``` yang akan dipanggil ketika tombol "Generate" diklik oleh pengguna. Fungsi ini berisi logika untuk menghasilkan password secara acak.
*   ```length = length_entry.get()``` akan mengambil nilai yang dimasukkan oleh pengguna pada   ```length_entry```, yaitu panjang password yang diinginkan, dan menyimpannya dalam variabel length.
*   ```length = int(length)``` akan mengonversi nilai length menjadi integer. Hal ini dilakukan karena nilai yang diambil dari   ```length_entry``` awalnya dalam bentuk string.
*   ```if length > 10: ... else: ...```akan memeriksa apakah panjang password yang dimasukkan oleh pengguna lebih besar dari 10. Jika lebih besar dari 10, maka akan muncul pesan kesalahan menggunakan   ```messagebox.showerror()```. Jika tidak, maka akan dilakukan proses pembuatan password.
*   ```characters = string.ascii_letters + string.digits + string.punctuation``` akan membuat string characters yang berisi kombinasi dari huruf alfabet (besar dan kecil), angka, dan tanda baca.
*   ```password = ''.join(random.choice(characters) for _ in range(length))``` akan menggunakan perulangan for untuk memilih karakter secara acak dari characters, sebanyak length kali. Kemudian, karakter-karakter tersebut digabungkan menjadi string password menggunakan metode   ```join()```.
*   ```password_label.config(text="Password: " + password)``` akan mengatur teks dari   ```password_label``` dengan menambahkan string "Password: " diikuti dengan nilai password.
* Inisialisasi jendela utama   ```(root)``` dengan kode di bawah deklarasi fungsi adalah inisialisasi jendela utama aplikasi menggunakan   ```tk.Tk()```. Ini membuat objek root yang merupakan instance dari kelas Tk dari modul tkinter. Jendela utama ini akan menampilkan antarmuka aplikasi pembuat password.
* Pengaturan tampilan jendela utama yaitu pengaturan tampilan jendela utama, seperti memberikan judul jendela, mengatur warna latar belakang, dan menambahkan label serta tombol ke dalam jendela.
*   ```root.mainloop()``` akan menjalankan siklus utama aplikasi Tkinter. Ini akan memperbarui dan menampilkan jendela aplikasi, serta menangani peristiwa yang terjadi di dalamnya.

 ```py
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
```
Pada kode di atas terdapat beberapa fungsi yaitu:

* ```if __name__ == "__main__"``` adalah kondisi yang memeriksa apakah skrip ini dijalankan langsung sebagai file utama. Ini digunakan untuk memastikan bahwa kode di dalamnya hanya dijalankan ketika file ini dieksekusi langsung, dan tidak ketika file ini diimpor sebagai modul oleh file lain.
* ```root = tk.Tk()``` membuat objek root yang merupakan instance dari kelas Tk Ini merupakan jendela utama atau window dari aplikasi GUI.
* ```root.title("UAS PBO KELOMPOK 14")``` mengatur judul jendela utama aplikasi menjadi "UAS PBO KELOMPOK 14".
* ```root.configure(bg="black")``` mengatur warna latar belakang (background color) jendela utama menjadi hitam.
* ```header_label = tk.Label(root, text="Cara Pemakaian Aplikasi", font=("Times New Roman", 20), bg="black", fg="white")``` membuat objek header_label yang merupakan label teks dengan teks "Cara Pemakaian Aplikasi". Parameter font digunakan untuk mengatur jenis font dan ukuran teks, bg digunakan untuk mengatur warna latar belakang label, dan fg digunakan untuk mengatur warna teks label.
* ```header_label.pack(pady=20)```  menempatkan label header_label di jendela utama menggunakan metode ```pack()```. Parameter pady digunakan untuk memberikan jarak (padding) di atas dan di bawah label.
* ```instructions``` adalah sebuah daftar yang berisi beberapa instruksi yang akan ditampilkan dalam bentuk label teks di jendela utama. Setiap instruksi adalah sebuah string.
* ```Loop for instruction in instructions``` digunakan untuk mengiterasi melalui setiap instruksi dalam instructions.
* ```label = tk.Label(root, text=instruction, font=("Times New Roman", 12), bg="black", fg="white")``` membuat objek label yang merupakan label teks untuk setiap instruksi. * Nilai teks dari label diatur sesuai dengan instruksi yang sedang diiterasi. Parameter lainnya seperti font, bg, dan fg digunakan untuk mengatur tampilan label yang serupa dengan ```header_label```.
* ```label.pack()``` menempatkan label di jendela utama.
* ```open_button = tk.Button(root, text="Buka Aplikasi", font=("Times New Roman", 12), bg="gray", command=open_password_generator)``` membuat objek open_button yang merupakan sebuah tombol dengan teks "Buka Aplikasi". Parameter font, bg, dan command diatur seperti sebelumnya. 
* ```command=open_password_generator``` mengacu pada fungsi ```open_password_generator``` yang diharapkan ada di kode yang tidak ditampilkan.
* ```open_button.pack(pady=20)``` menempatkan tombol ```open_button``` di jendela utama dengan jarak ```(padding)``` di atas dan di bawah tombol.
* ```root.mainloop()``` merupakan perintah yang menjalankan siklus utama aplikasi Tkinter. Ini membuat aplikasi tetap berjalan dan merespons terhadap berbagai interaksi pengguna hingga jendela utama ditutup.

## Penjelasan Aplikasi Password
Aplikasi yang dibuat atau output dari program tersebut adalah aplikasi pembuat password secara acak dengan memanfaatkan konsep OOP. Meskipun program yang dibuat tidak memanfaatkan konsep OOP secara luas, beberapa prinsip OOP seperti penggunaan objek, pengelompokan fungsi-fungsi terkait, dan penggunaan kelas-kelas dari modul tkinter dapat ditemukan dalam kode tersebut.

* Page pertama akan menampilkan intruksi bagaimana penggunaan aplikasi pembuat password yang tekah diprogramkan, setelah itu pengguna dapat mengklik 'Buka Aplikasi' dan akan beralih ke halaman kedua.
* Pada page kedua, pengguna akan diminta untuk menginput panjang dari password yang diinginkan dan mengkilik 'Generate'. Jika pengguna memasukkan panjang password lebih dari 10, maka akan muncul pop-up message yang berisi "Panjang password maksimal adalah 10!". Namun, jika pengguna memasukkan angka dari rentang 1-10 maka aplikasi akan menampilkan password random yang berisi huruf besar/kecil, serta beberapa karakter lainnya.

Program untuk membuat password dengan skrip phyton :

https://github.com/merlyyunipurnama/UAS-PBO/blob/main/passwordGenerator.py

## Authors

- [@merlyyunipurnama](https://www.github.com/octokatherine)
