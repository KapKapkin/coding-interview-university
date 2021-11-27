import sys, sqlite3, os

from PyQt5 import QtGui, QtWidgets, uic, QtCore

class Coffee(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        sorts_lst = self.cur.execute('''SELECT title FROM sort_table''').fetchall()
        for i in sorts_lst: self.sorts.addItem(i[0])
        self.change()
        self.sorts.currentIndexChanged.connect(self.change)

    def change(self):
        text = self.sorts.currentText()
        self.title_label.setText(text)

        inf = self.cur.execute(f'''SELECT * FROM sort_table WHERE title = '{text}' ''').fetchall()
        id, title, roasting, type, discription, cost, volume = inf[0]

        roasting = self.cur.execute(f'''SELECT title FROM roasting_table WHERE id = {roasting}''').fetchone()[0]
        type = self.cur.execute(f'''SELECT title FROM type_table WHERE id = {type}''').fetchone()[0]
        volume = self.cur.execute(f'''SELECT value FROM volume_table WHERE id = {volume}''').fetchone()[0]
        
        self.roasting_label.setText(roasting + ' обжарка')
        self.type_label.setText(type)
        self.cost_label.setText(f'{cost}руб/{volume}г')
        self.textEdit.setText(discription)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    programm = Coffee()
    programm.show()
    sys.exit(app.exec())
