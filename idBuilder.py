import sys
import cv2
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp

class Principale(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setUI()

	def setUI(self):
		exitAction=QAction('&Exit', self)
		exitAction.setShortcut('Ctrl+Q')
		exitAction.setStatusTip("Quitter l'application")
		exitAction.triggered.connect(qApp.exit)

		menu=self.menuBar()
		fichierMenu=menu.addMenu("&Fichier")
		fichierMenu.addAction(exitAction)
		
		self.barreOutils=self.addToolBar('Quitter')
		self.barreOutils.addAction(exitAction)

		self.setGeometry(300,300,500,250)
		self.setWindowTitle('Fenêtre principale')
		self.statusBar().showMessage('Barre de statut')
		self.show()


print(cv2.__version__)


monApp=QApplication(sys.argv)
fenetre=Principale()
sys.exit(monApp.exec_())
