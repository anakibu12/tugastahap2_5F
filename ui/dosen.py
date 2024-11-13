from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
import sys

# Fungsi slot yang akan dipanggil ketika tombol ditekan
def on_tombol_diklik():
    # Mengambil teks dari QLineEdit
    id_dosen = input_id.text()
    nama_dosen = input_nama.text()
    mata_kuliah_dosen = input_mata_kuliah.text()

    # Menampilkan data di konsol
    print(f"ID Dosen: {id_dosen}, Nama: {nama_dosen}, Mata Kuliah: {mata_kuliah_dosen}")
    # Menampilkan data di label
    label.setText(f"Dosen {nama_dosen} berhasil ditambahkan!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Form Input Dosen')

# Membuat inputan teks
input_id = QLineEdit()
input_id.setPlaceholderText("Masukkan ID Dosen")
input_nama = QLineEdit()
input_nama.setPlaceholderText("Masukkan Nama Dosen")
input_mata_kuliah = QLineEdit()
input_mata_kuliah.setPlaceholderText("Masukkan Mata Kuliah")
button = QPushButton('Submit')
label = QLabel("Output: ")

# Menghubungkan signal tombol ke slot
button.clicked.connect(on_tombol_diklik)

# Menambahkan widget ke layout
layout = QVBoxLayout()
layout.addWidget(input_id)
layout.addWidget(input_nama)
layout.addWidget(input_mata_kuliah)
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)

# Menampilkan window
window.show()

# Menjalankan aplikasi
sys.exit(app.exec())
