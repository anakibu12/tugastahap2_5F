from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
import sys


def on_tombol_diklik():
    # Mengambil teks dari QLineEdit
    id_calon = input_id.text()
    nama_calon = input_nama.text()
    status_calon = input_status.text()


    print(f"ID Calon: {id_calon}, Nama: {nama_calon}, Status: {status_calon}")
    # Menampilkan data di label
    label.setText(f"Calon {nama_calon} berhasil ditambahkan!")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Form Input Calon')


input_id = QLineEdit()
input_id.setPlaceholderText("Masukkan ID Calon")
input_nama = QLineEdit()
input_nama.setPlaceholderText("Masukkan Nama Calon")
input_status = QLineEdit()
input_status.setPlaceholderText("Masukkan Status Calon")
button = QPushButton('Submit')
label = QLabel("Output: ")

#
button.clicked.connect(on_tombol_diklik)


layout = QVBoxLayout()
layout.addWidget(input_id)
layout.addWidget(input_nama)
layout.addWidget(input_status)
layout.addWidget(button)
layout.addWidget(label)
window.setLayout(layout)


window.show()


sys.exit(app.exec())
