from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
import sys


def on_tombol_diklik():

    id_dokter = input_id.text()
    nama_dokter = input_nama.text()
    spesialisasi_dokter = input_spesialisasi.text()


    print(f"ID Dokter: {id_dokter}, Nama: {nama_dokter}, Spesialisasi: {spesialisasi_dokter}")

    label.setText(f"Dokter {nama_dokter} berhasil ditambahkan!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Form Input Dokter')


input_id = QLineEdit()
input_id.setPlaceholderText("Masukkan ID Dokter")
input_nama = QLineEdit()
input_nama.setPlaceholderText("Masukkan Nama Dokter")
input_spesialisasi = QLineEdit()
input_spesialisasi.setPlaceholderText("Masukkan Spesialisasi Dokter")
button = QPushButton('Submit')
label = QLabel("Output: ")


button.clicked.connect(on_tombol_diklik)


layout = QVBoxLayout()
layout.addWidget(input_id)
layout.addWidget(input_nama)
layout.addWidget(input_spesialisasi)
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)


window.show()

# Menjalankan aplikasi
sys.exit(app.exec())
