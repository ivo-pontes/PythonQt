from PyQt5 import QtWidgets, uic

def converter():
	dialog.brlEdit.setText(str(float(dialog.usdEdit.text())*3.4))

if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	dialog = uic.loadUi('main.ui')

	dialog.usdEdit.setFocus()
	dialog.usdEdit.setPlaceholderText("USD")
	dialog.converterBtn.clicked.connect(converter)
	dialog.usdEdit.returnPressed.connect(converter)
	dialog.brlEdit.setReadOnly(True)

	dialog.show()
	app.exec()

	print("Fim de execução!!")


