from PyQt5 import QtCore, QtGui, QtWidgets  #Impor modul Pyqt5 yang akan digunakan sebagai GUI
import os, shutil, glob  #Impor modul untuk penanganan file
from PIL import Image  #Impor modul untuk Konversi gambar


class Ui_JendelaUtama(object):
    def penyiapanUi(self, JendelaUtama):
        JendelaUtama.setObjectName("JendelaUtama")
        JendelaUtama.resize(480, 144)
        JendelaUtama.setStyleSheet(
            "\n"
            "QMainWindow {\n"
            "    background-image: url(Wallpaper.jpg);\n"
            "    background-color: '008ef2';\n"
            "    background-repeat: no-repeat;\n"
            "    background-position: center;\n"
            "}\n"
            "QPushButton{\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-bottom-color: rgb(58, 58, 58);\n"
            "    border-bottom-width: 1px;\n"
            "    border-style: solid;\n"
            "    color: rgb(255, 255, 255);\n"
            "    padding: 2px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
            "}\n"
            "QPushButton:hover{\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
            "    border-bottom-color: rgb(115, 115, 115);\n"
            "    border-bottom-width: 1px;\n"
            "    border-style: solid;\n"
            "    color: rgb(255, 255, 255);\n"
            "    padding: 2px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
            "}\n"
            "QPushButton:pressed{\n"
            "    border-style: outset;\n"
            "    border-width: 2px;\n"
            "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));\n"
            "    border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
            "    border-bottom-color: rgb(58, 58, 58);\n"
            "    border-bottom-width: 1px;\n"
            "    border-style: solid;\n"
            "    color: rgb(255, 255, 255);\n"
            "    padding: 2px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
            "}\n"
            )

        self.widgetPusat = QtWidgets.QWidget(JendelaUtama)
        self.widgetPusat.setObjectName("widgetPusat")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widgetPusat)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.TombolImport = QtWidgets.QPushButton(self.widgetPusat)
        self.TombolImport.setMinimumSize(QtCore.QSize(150, 40))
        self.TombolImport.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.TombolImport.setFont(font)
        self.TombolImport.setObjectName("TombolImport")
        self.TombolImport.clicked.connect(self.importBerkas)
        self.horizontalLayout_2.addWidget(self.TombolImport)
        self.KotakKombo = QtWidgets.QComboBox(self.widgetPusat)
        self.KotakKombo.setMinimumSize(QtCore.QSize(150, 40))
        self.KotakKombo.setMaximumSize(QtCore.QSize(150, 40))
        self.KotakKombo.setFont(font)
        self.KotakKombo.setObjectName("KotakKombo")
        self.KotakKombo.addItem("")
        self.KotakKombo.addItem("")
        self.KotakKombo.addItem("")
        self.KotakKombo.addItem("")
        self.KotakKombo.addItem("")

        self.horizontalLayout_2.addWidget(self.KotakKombo)
        self.TombolExport = QtWidgets.QPushButton(self.widgetPusat)
        self.TombolExport.setMinimumSize(QtCore.QSize(150, 40))
        self.TombolExport.setMaximumSize(QtCore.QSize(150, 40))
        self.TombolExport.setFont(font)
        self.TombolExport.setObjectName("TombolExport")
        self.TombolExport.clicked.connect(self.exportBerkas)
        self.horizontalLayout_2.addWidget(self.TombolExport)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        JendelaUtama.setCentralWidget(self.widgetPusat)

        self.retranslateUi(JendelaUtama)
        QtCore.QMetaObject.connectSlotsByName(JendelaUtama)

    def retranslateUi(self, JendelaUtama):
        _translate = QtCore.QCoreApplication.translate
        JendelaUtama.setWindowTitle(_translate("JendelaUtama", "Konverter Gambar"))
        self.TombolImport.setText(_translate("JendelaUtama", "Import Berkas"))
        self.KotakKombo.setItemText(0, _translate("JendelaUtama", "-> JPG"))
        self.KotakKombo.setItemText(1, _translate("JendelaUtama", "-> PDF"))
        self.KotakKombo.setItemText(2, _translate("JendelaUtama", "-> PNG"))
        self.KotakKombo.setItemText(3, _translate("JendelaUtama", "-> WEBP"))
        self.KotakKombo.setItemText(4, _translate("JendelaUtama", "-> TIFF/TIF"))
        self.TombolExport.setText(_translate("JendelaUtama", "Export Berkas"))

    #Kumpulan fungsi penanganan file
    def importBerkas(self):
        AlamatImport = QtWidgets.QFileDialog.getOpenFileName(
            caption = "Pilih Berkas Gambar",
            directory = os.path.expanduser('~/Pictures'),
            filter = "(*.jpg *.jpeg *.png *.tiff *.webp)   "
            )[0]

        if AlamatImport != "":
            shutil.copy(AlamatImport, "Import")

    def exportBerkas(self):
        opsi = self.KotakKombo.currentText()

        for alamatBerkas in glob.glob("Import/*"):
            if opsi == "-> JPG":
                formatBerkas = ".jpg"
                tipeBerkas = "JPEG"
            elif opsi == "-> PNG":
                formatBerkas = ".png"
                tipeBerkas = "PNG"
            elif opsi == "-> PDF":
                formatBerkas = ".pdf"
                tipeBerkas = "PDF"
            elif opsi == "-> WEBP":
                formatBerkas = ".webp"
                tipeBerkas = "WEBP"
            elif opsi == "-> TIFF/TIF":
                formatBerkas = ".tiff"
                tipeBerkas = "TIFF"

            Berkas = os.path.splitext(alamatBerkas)[0]

            im = Image.open(alamatBerkas).convert("RGB")
            im.save(Berkas + formatBerkas, tipeBerkas)

            exportedBerkas = glob.glob((f"Import/*{formatBerkas}"))[0]
            alamatExport = QtWidgets.QFileDialog.getSaveFileName(
                parent = None, caption = Berkas, directory = os.path.expanduser(f'~/Pictures/{Berkas}'),
                filter = f"{tipeBerkas} (*{formatBerkas})"
                )[0]


        if alamatExport != '':
            shutil.copy(exportedBerkas, alamatExport)
            QtWidgets.QMessageBox.information(
                None, "Selamat", f"{Berkas}{formatBerkas} telah tersimpan di \n:{alamatExport}"
                )
            hapusBerkas()

        else:
            QtWidgets.QMessageBox.information(
                None, "Error", f"Tidak ada berkas terpilih"
                )

def hapusBerkas():
    for berkas in glob.glob(("Import/*")):
        os.remove(berkas)


if __name__ == "__main__":
    import sys
    hapusBerkas()
    app = QtWidgets.QApplication(sys.argv) #mendefinisikan app berfungsi sebagai pengelola aliran kontrol aplikasi GUI dan pengaturan utama.
    JendelaUtama = QtWidgets.QMainWindow() #mendefinisikan Jendela Utama menyediakan struktur basic (framework) untuk membangun user interface
    ui = Ui_JendelaUtama()
    ui.penyiapanUi(JendelaUtama)
    JendelaUtama.show()
    sys.exit(app.exec_())