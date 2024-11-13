from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
import sys

# Fungsi slot yang akan dipanggil ketika tombol ditekan
def on_tombol_diklik():
    # Mengambil teks dari QLineEdit
    id_pasien = input_id.text()
    nama_pasien = input_nama.text()
    umur_pasien = input_umur.text()

    # Menampilkan data di konsol
    print(f"ID Pasien: {id_pasien}, Nama: {nama_pasien}, Umur: {umur_pasien}")
    # Menampilkan data di label
    label.setText(f"Pasien {nama_pasien} berhasil ditambahkan!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Form Input Pasien')

# Membuat inputan teks
input_id = QLineEdit()
input_id.setPlaceholderText("Masukkan ID Pasien")
input_nama = QLineEdit()
input_nama.setPlaceholderText("Masukkan Nama Pasien")
input_umur = QLineEdit()
input_umur.setPlaceholderText("Masukkan Umur Pasien")
button = QPushButton('Submit')
label = QLabel("Output: ")

# Menghubungkan signal tombol ke slot
button.clicked.connect(on_tombol_diklik)

# Menambahkan widget ke layout
layout = QVBoxLayout()
layout.addWidget(input_id)
layout.addWidget(input_nama)
layout.addWidget(input_umur)
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)

# Menampilkan window
window.show()

# Menjalankan aplikasi
sys.exit(app.exec())
