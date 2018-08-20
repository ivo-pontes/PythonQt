from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

def addItem():
	if dialog.resultadoEdit.text() != "":
		dialog.lista.addItem(dialog.resultadoEdit.text())
	else:
		showMessage("Título", "Mensagem Vazia!")
	

def showMessage(title, message):
	QMessageBox.information(None,title, message)

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	dialog = uic.loadUi('main.ui')

	
	dialog.resultadoEdit.setFocus()
	dialog.resultadoEdit.returnPressed.connect(addItem)
	dialog.converterBtn.clicked.connect(addItem)

	dialog.show()
	app.exec()

	print("Fim de execução!!")


