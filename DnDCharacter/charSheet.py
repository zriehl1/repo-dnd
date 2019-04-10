import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from charSheetUI import Ui_CharacterSheet

class CompletionTrack(QtWidgets.QDialog):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_CharacterSheet()
        self.ui.setupUi(self)

        self.skills = [self.ui.a, self.ui.b, self.ui.c, self.ui.d, self.ui.e, self.ui.f, self.ui.g, self.ui.h, self.ui.i, self.ui.j, self.ui.k, self.ui.l, self.ui.m, self.ui.n, self.ui.o, self.ui.p, self.ui.q, self.ui.r, self.ui.s, self.ui.t, self.ui.u, self.ui.v, self.ui.w, self.ui.x]
        self.ui.hpMinusBtn.clicked.connect(self.subHP)
        self.ui.hpPlusBtn.clicked.connect(self.addHP)
        self.show()

    def addHP(self):
        print("adding hp")

    def subHP(self):
        print('subtracting hp')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ctr = CompletionTrack()
    ctr.show()
    sys.exit(app.exec_())
    
