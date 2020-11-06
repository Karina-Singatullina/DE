import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide2.QtGui import (QPixmap)
from PySide2.QtWidgets import *

from numpy import double, exp
import functions


class Ui_Dialog(object):
    def setupUi(self, DE):
        if DE.objectName():
            DE.setObjectName(u"DE")
        DE.resize(923, 550)
        error_dialog = QErrorMessage()
        error_dialog.showMessage('Incorrect input, try again')
        self.pushButton = QPushButton(DE)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 410, 161, 28))
        self.tabWidget = QTabWidget(DE)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(250, 20, 620, 480))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.graphicsView = QGraphicsView(self.tab)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 640, 480))
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.scene.addPixmap(QPixmap("functions.png"))
        self.tabWidget.addTab(self.tab, "")
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.graphicsView_2 = QGraphicsView(self.widget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(0, 0, 640, 480))
        self.scene2 = QGraphicsScene()
        self.graphicsView_2.setScene(self.scene2)
        self.scene2.addPixmap(QPixmap("GTE.png"))
        self.tabWidget.addTab(self.widget, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.graphicsView_3 = QGraphicsView(self.tab_3)
        self.graphicsView_3.setObjectName(u"graphicsView_3")
        self.graphicsView_3.setGeometry(QRect(0, 0, 640, 480))
        self.scene3 = QGraphicsScene()
        self.graphicsView_3.setScene(self.scene3)
        self.scene3.addPixmap(QPixmap("LTE.png"))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.graphicsView_4 = QGraphicsView(self.tab_4)
        self.graphicsView_4.setObjectName(u"graphicsView_4")
        self.graphicsView_4.setGeometry(QRect(0, 0, 640, 480))
        self.scene4 = QGraphicsScene()
        self.graphicsView_4.setScene(self.scene4)
        self.scene4.addPixmap(QPixmap("max_GTE.png"))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.graphicsView_5 = QGraphicsView(self.tab_2)
        self.graphicsView_5.setObjectName(u"graphicsView_5")
        self.graphicsView_5.setGeometry(QRect(0, 0, 640, 480))
        self.scene5 = QGraphicsScene()
        self.graphicsView_5.setScene(self.scene5)
        self.scene5.addPixmap(QPixmap("max_LTE.png"))
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayoutWidget = QWidget(DE)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 250, 164, 141))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)
        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setChecked(True)
        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setChecked(True)
        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox1 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox1.setObjectName(u"checkBox1")
        self.checkBox1.setChecked(True)
        self.verticalLayout.addWidget(self.checkBox1)

        self.label_4 = QLabel(DE)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 79, 41, 31))
        self.label = QLabel(DE)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 41, 31))
        self.label_2 = QLabel(DE)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 210, 41, 21))
        self.label_3 = QLabel(DE)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 40, 41, 31))
        self.verticalLayoutWidget_2 = QWidget(DE)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(60, 30, 161, 221))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_2.addWidget(self.lineEdit_5)

        self.label_5 = QLabel(DE)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 160, 41, 31))

        self.retranslateUi(DE)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(DE)



    def retranslateUi(self, DE):
        DE.setWindowTitle(QCoreApplication.translate("DE", u"DE", None))
        self.pushButton.setText(QCoreApplication.translate("DE", u"Start", None))
        self.pushButton.clicked.connect(self.execute)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("DE", u"Function", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), QCoreApplication.translate("DE", u"GTE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("DE", u"LTE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("DE", u"GTE max", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("DE", u"LTE max", None))
        self.checkBox.setText(QCoreApplication.translate("DE", u"Exact", None))
        self.checkBox_3.setText(QCoreApplication.translate("DE", u"Euler method", None))
        self.checkBox_2.setText(QCoreApplication.translate("DE", u"Improved-Euler method", None))
        self.checkBox1.setText(QCoreApplication.translate("DE", u"Runge-Kutta method", None))
        self.label_4.setText(QCoreApplication.translate("DE", u"x0 = ", None))
        self.label.setText(QCoreApplication.translate("DE", u"X = ", None))
        self.label_2.setText(QCoreApplication.translate("DE", u"N = ", None))
        self.label_3.setText(QCoreApplication.translate("DE", u"y0 = ", None))
        self.label_5.setText(QCoreApplication.translate("DE", u"n = ", None))


    try:
        def execute(self):
            if (self.lineEdit.text() == ""):
                y_0 = -2
            else:
                y_0 = double(self.lineEdit.text())

            if (self.lineEdit_4.text() == ""):
                x_0 = 1
            else:
                x_0 = double(self.lineEdit_4.text())

            if (self.lineEdit_3.text() == ""):
                X = 7
            else:
                X = double(self.lineEdit_3.text())

            if (self.lineEdit_2.text() == ""):
                n = 60
            else:
                n = double(self.lineEdit_2.text())

            if (self.lineEdit_5.text() == ""):
                N = 120
            else:
                N = double(self.lineEdit_5.text())

            C = 1 / x_0 - 1 / (exp(y_0) * x_0 ** 2)
            assert x_0 != 0, "x cannot be equal to 0"
            assert X > x_0, "X should be greater than x"
            assert N >= n, "N should be greater or equal to n " + str(N) + " " + str(n)
            assert n > 0, "n should be greater than 0"
            assert C != 0, "C cannot be equal to 0"
            assert C * x_0 < 1, "Incorrect input"

            information = functions.DifferentialEquation(x_0=x_0, y_0=y_0, X=X, n=n, N=N,
                                                         check_E=self.checkBox.isChecked(),
                                                         check_IE=self.checkBox_3.isChecked(),
                                                         check_RK=self.checkBox_2.isChecked(),
                                                         check_exact=self.checkBox1.isChecked())
            information.solve()
            information.functions()
            self.scene.addPixmap(QPixmap("functions.png"))

            information.GTE()
            self.scene2.addPixmap(QPixmap("GTE.png"))

            information.LTE()
            self.scene3.addPixmap(QPixmap("LTE.png"))

            information.GTEM()
            self.scene4.addPixmap(QPixmap("max_GTE.png"))

            information.LTEM()
            self.scene5.addPixmap(QPixmap("max_LTE.png"))
    except Exception:
        pass


app = QApplication(sys.argv)
main_win = QMainWindow()
ui = Ui_Dialog()
ui.setupUi(main_win)
main_win.show()
sys.exit(app.exec_())