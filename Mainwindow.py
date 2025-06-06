# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowpcQIwc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(659, 767)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 661, 771))
        self.tab_0 = QWidget()
        self.tab_0.setObjectName(u"tab_0")
        self.gridLayoutWidget = QWidget(self.tab_0)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(120, 10, 521, 27))
        self.HLayout_Language = QHBoxLayout(self.gridLayoutWidget)
        self.HLayout_Language.setObjectName(u"HLayout_Language")
        self.HLayout_Language.setContentsMargins(0, 0, 0, 0)
        self.radioButton_Language_Catala = QRadioButton(self.gridLayoutWidget)
        self.radioButton_Language_Catala.setObjectName(u"radioButton_Language_Catala")
        font = QFont()
        font.setPointSize(8)
        self.radioButton_Language_Catala.setFont(font)
        self.radioButton_Language_Catala.setChecked(True)

        self.HLayout_Language.addWidget(self.radioButton_Language_Catala)

        self.radioButton_Language_Castellano = QRadioButton(self.gridLayoutWidget)
        self.radioButton_Language_Castellano.setObjectName(u"radioButton_Language_Castellano")
        self.radioButton_Language_Castellano.setFont(font)
        self.radioButton_Language_Castellano.setChecked(False)

        self.HLayout_Language.addWidget(self.radioButton_Language_Castellano)

        self.radioButton_Language_English = QRadioButton(self.gridLayoutWidget)
        self.radioButton_Language_English.setObjectName(u"radioButton_Language_English")
        self.radioButton_Language_English.setFont(font)
        self.radioButton_Language_English.setChecked(False)

        self.HLayout_Language.addWidget(self.radioButton_Language_English)

        self.radioButton_Language_Xertoli = QRadioButton(self.gridLayoutWidget)
        self.radioButton_Language_Xertoli.setObjectName(u"radioButton_Language_Xertoli")
        self.radioButton_Language_Xertoli.setEnabled(True)
        self.radioButton_Language_Xertoli.setFont(font)
        self.radioButton_Language_Xertoli.setChecked(False)

        self.HLayout_Language.addWidget(self.radioButton_Language_Xertoli)

        self.line_4 = QFrame(self.tab_0)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(20, 450, 621, 20))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.label_Stage3 = QLabel(self.tab_0)
        self.label_Stage3.setObjectName(u"label_Stage3")
        self.label_Stage3.setGeometry(QRect(30, 480, 47, 71))
        font1 = QFont()
        font1.setPointSize(36)
        self.label_Stage3.setFont(font1)
        self.label_InsertText = QLabel(self.tab_0)
        self.label_InsertText.setObjectName(u"label_InsertText")
        self.label_InsertText.setGeometry(QRect(120, 210, 331, 21))
        font2 = QFont()
        font2.setPointSize(9)
        self.label_InsertText.setFont(font2)
        self.line = QFrame(self.tab_0)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 50, 621, 20))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.tab_0)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 330, 621, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.tab_0)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(20, 570, 621, 20))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.plainTextEdit_ErrorConsole = QPlainTextEdit(self.tab_0)
        self.plainTextEdit_ErrorConsole.setObjectName(u"plainTextEdit_ErrorConsole")
        self.plainTextEdit_ErrorConsole.setGeometry(QRect(30, 600, 601, 87))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(255, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.plainTextEdit_ErrorConsole.setPalette(palette)
        self.plainTextEdit_ErrorConsole.setFont(font)
        self.plainTextEdit_ErrorConsole.setReadOnly(True)
        self.label_Stage1 = QLabel(self.tab_0)
        self.label_Stage1.setObjectName(u"label_Stage1")
        self.label_Stage1.setGeometry(QRect(30, 80, 47, 71))
        self.label_Stage1.setFont(font1)
        self.label_Stage2 = QLabel(self.tab_0)
        self.label_Stage2.setObjectName(u"label_Stage2")
        self.label_Stage2.setGeometry(QRect(30, 220, 47, 81))
        self.label_Stage2.setFont(font1)
        self.pushButton_LoadFile = QPushButton(self.tab_0)
        self.pushButton_LoadFile.setObjectName(u"pushButton_LoadFile")
        self.pushButton_LoadFile.setGeometry(QRect(120, 80, 131, 41))
        self.pushButton_LoadFile.setFont(font2)
        self.lineEdit_Insert = QLineEdit(self.tab_0)
        self.lineEdit_Insert.setObjectName(u"lineEdit_Insert")
        self.lineEdit_Insert.setGeometry(QRect(120, 280, 161, 31))
        self.lineEdit_Insert.setFont(font2)
        self.line_2 = QFrame(self.tab_0)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 170, 621, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.formLayoutWidget = QWidget(self.tab_0)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 360, 621, 81))
        self.FLayout_pagesInfo = QFormLayout(self.formLayoutWidget)
        self.FLayout_pagesInfo.setObjectName(u"FLayout_pagesInfo")
        self.FLayout_pagesInfo.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.FLayout_pagesInfo.setContentsMargins(0, 0, 0, 0)
        self.label_NpagesOriginalText = QLabel(self.formLayoutWidget)
        self.label_NpagesOriginalText.setObjectName(u"label_NpagesOriginalText")
        self.label_NpagesOriginalText.setFont(font2)
        self.label_NpagesOriginalText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FLayout_pagesInfo.setWidget(0, QFormLayout.LabelRole, self.label_NpagesOriginalText)

        self.label_NpagesOriginal = QLabel(self.formLayoutWidget)
        self.label_NpagesOriginal.setObjectName(u"label_NpagesOriginal")
        self.label_NpagesOriginal.setFont(font2)

        self.FLayout_pagesInfo.setWidget(0, QFormLayout.FieldRole, self.label_NpagesOriginal)

        self.label_NpagesInsertedText = QLabel(self.formLayoutWidget)
        self.label_NpagesInsertedText.setObjectName(u"label_NpagesInsertedText")
        self.label_NpagesInsertedText.setFont(font2)
        self.label_NpagesInsertedText.setScaledContents(False)
        self.label_NpagesInsertedText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FLayout_pagesInfo.setWidget(1, QFormLayout.LabelRole, self.label_NpagesInsertedText)

        self.label_NpagesInserted = QLabel(self.formLayoutWidget)
        self.label_NpagesInserted.setObjectName(u"label_NpagesInserted")
        self.label_NpagesInserted.setFont(font2)

        self.FLayout_pagesInfo.setWidget(1, QFormLayout.FieldRole, self.label_NpagesInserted)

        self.label_ValidText = QLabel(self.formLayoutWidget)
        self.label_ValidText.setObjectName(u"label_ValidText")
        self.label_ValidText.setFont(font2)
        self.label_ValidText.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.FLayout_pagesInfo.setWidget(2, QFormLayout.LabelRole, self.label_ValidText)

        self.label_Valid = QLabel(self.formLayoutWidget)
        self.label_Valid.setObjectName(u"label_Valid")
        self.label_Valid.setFont(font2)

        self.FLayout_pagesInfo.setWidget(2, QFormLayout.FieldRole, self.label_Valid)

        self.pushButton_Convert = QPushButton(self.tab_0)
        self.pushButton_Convert.setObjectName(u"pushButton_Convert")
        self.pushButton_Convert.setGeometry(QRect(420, 500, 211, 41))
        self.pushButton_Convert.setFont(font2)
        self.lineEdit_OpenFile = QLineEdit(self.tab_0)
        self.lineEdit_OpenFile.setObjectName(u"lineEdit_OpenFile")
        self.lineEdit_OpenFile.setGeometry(QRect(120, 130, 521, 20))
        self.lineEdit_OpenFile.setReadOnly(True)
        self.label_InsertInstructionText = QLabel(self.tab_0)
        self.label_InsertInstructionText.setObjectName(u"label_InsertInstructionText")
        self.label_InsertInstructionText.setGeometry(QRect(120, 230, 471, 31))
        self.label_InsertInstructionText.setFont(font2)
        self.frame_SaveDivide = QFrame(self.tab_0)
        self.frame_SaveDivide.setObjectName(u"frame_SaveDivide")
        self.frame_SaveDivide.setGeometry(QRect(110, 480, 221, 71))
        self.frame_SaveDivide.setFrameShape(QFrame.StyledPanel)
        self.frame_SaveDivide.setFrameShadow(QFrame.Raised)
        self.radioButton_Save_Whole = QRadioButton(self.frame_SaveDivide)
        self.radioButton_Save_Whole.setObjectName(u"radioButton_Save_Whole")
        self.radioButton_Save_Whole.setGeometry(QRect(10, 10, 171, 21))
        self.radioButton_Save_Whole.setFont(font2)
        self.radioButton_Save_Whole.setChecked(True)
        self.radioButton_Save_Separately = QRadioButton(self.frame_SaveDivide)
        self.radioButton_Save_Separately.setObjectName(u"radioButton_Save_Separately")
        self.radioButton_Save_Separately.setGeometry(QRect(10, 40, 191, 21))
        self.radioButton_Save_Separately.setFont(font2)
        self.pushButton_Convert_NoReorder = QPushButton(self.tab_0)
        self.pushButton_Convert_NoReorder.setObjectName(u"pushButton_Convert_NoReorder")
        self.pushButton_Convert_NoReorder.setGeometry(QRect(420, 280, 211, 41))
        self.pushButton_Convert_NoReorder.setFont(font2)
        self.tabWidget.addTab(self.tab_0, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), u";)")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.textBrowser = QTextBrowser(self.tab_1)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(20, 20, 621, 661))
        self.textBrowser.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Acreditacions:</span><span style=\" font-size:11pt;\"><br />Este programa s'ha fet gr\u00e0cies a Qt Designer i a les llibrer\u00edes PyPDF2 i PySide6. Pots trobar m\u00e9s projectes en </span><a href=\"https://github.com/vicent-b\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">https://github.com/vicent-b</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><s"
                        "pan style=\" font-size:14pt;\"><br /></span><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Informaci\u00f3:</span><span style=\" font-size:11pt;\"><br />Este programa reordena las p\u00e0gines d'un PDF per tal que, al imprimir-lo, sols calga doblar el munt de fulles per la mitad per a formar un llibre. Ja que la quantita de fulles deu ser m\u00faltiple de 4, se permet insertar fulles en blanc. Per a imprimir la portada a color i la resta en blanc i negre, pots separar la fulla m\u00e9s exterior sel\u00b7leccionant la opci\u00f3 &quot;guarda la protada per separat&quot;<br /><br />Per a imprimir, has de configurar la impressi\u00f3 a 2 p\u00e0gines per fulla, a doble cara i per a passar p\u00e0gina pel costat curt.<br /><br />Per a encuadernar pots:<br />1) Grapar les fulles doblades per fora</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2) Grapar les fulles"
                        " doblades de tal manera que els extrems de la grapa queden a l'interior del llibre. Pot requerir d'una grapadora especialment llarga.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">3) Imitar el m\u00e8tode 2 perforant 2 parells de forats y nugant fil en un cercle en cada parell. Costa m\u00e9s teemps per\u00f2 la p\u00e0gina podr\u00e0 doblegar-se 180\u00ba (portada tocant la contraportada) sense trencar-se.</span><span style=\" font-size:6.6pt;\"><br /></span></p></body></html>")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.textBrowser_3 = QTextBrowser(self.tab_2)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(20, 20, 621, 661))
        self.textBrowser_3.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Acreditaciones:</span><span style=\" font-size:11pt;\"><br />Este programa se ha elaborado gracias a Qt Designer y a las librer\u00edas PyPDF2 y PySide6. Puedes encontrar m\u00e1s proyectos en </span><a href=\"https://github.com/vicent-b\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">https://github.com/vicent-b</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0p"
                        "x;\"><span style=\" font-size:14pt;\"><br /></span><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Informaci\u00f3n:</span><span style=\" font-size:11pt;\"><br />Este programa reordena las p\u00e1ginas de un PDF para que al imprimirlo, baste con doblar la monta\u00f1a de hojas por la mitad para formar un libro. Ya que la cantidad de hojas debe ser m\u00faltiplo de 4, se permite insertar hojas en blanco. Para imprimir la portada a color y el resto en blanco y negro, puede separar la hoja m\u00e1s exterior seleccionanco la opci\u00f3n &quot;guarda la portada por separado&quot;.<br /><br />Para imprimir, debe configurar la impresi\u00f3n a 2 p\u00e1ginas por hoja, a doble cara y para pasar p\u00e1gina por el lado corto.<br /><br />Para encuadernar, puede:<br />1) Grapar las hojas dobladas por fuera</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2) Grapar las hoj"
                        "as dobladas de tal forma que el cierre de la grapa quede en el interior del libro. Puede requerir de grapadora especialmente larga</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">3) Imitar el m\u00e9todo 2 perforando 2 pares de agujeros y atando hilo en 2 c\u00edrculos. Cuesta m\u00e1s tiempo pero la p\u00e1gina podr\u00e1 doblarse 180\u00ba (portada tocando la contraportada) sin romperse</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6.6pt;\"><br /></span></p></body></html>")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.textBrowser_4 = QTextBrowser(self.tab_3)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(20, 20, 621, 661))
        self.textBrowser_4.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Attributions:</span><span style=\" font-size:11pt;\"><br />This program has been made using Qt Designer and the libraries PyPDF2 and PySide6. You can find more projects at </span><a href=\"https://github.com/vicent-b\"><span style=\" font-size:11pt; text-decoration: underline; color:#0000ff;\">https://github.com/vicent-b</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" f"
                        "ont-size:14pt;\"><br /></span><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Information:</span><span style=\" font-size:11pt;\"><br />This program reorders the pages of a PDF so that when printed, it stitches the stack of pages together by folding them in half to form a book. Since the number of pages must be a multiple of 4, inserting pages is allowed. To print the cover in color and the rest in black and white, you can separate the outermost page by selecting the &quot;save cover separately&quot; option.<br /><br />To print, you must set the printer to 2 pages per sheet, double-sided and to turn the page on the short edge.<br /><br />To bind, you can:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">1) Staple the folded pages on the outside.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">2) Staple the folded pages so that the staple closure is on the inside of the book. This may require a particularly long stapler.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">3) Imitate method 2 by punching two pairs of holes and tying thread in two loops. It takes more time, but the page can be folded 180\u00b0 (front cover touching back cover) without breaking.</span><span style=\" font-size:6.6pt;\"><br /></span></p></body></html>")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.textBrowser_5 = QTextBrowser(self.tab_4)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(20, 20, 621, 661))
        self.textBrowser_5.setHtml(u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ERROR</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 659, 26))
        self.menubar.setDefaultUp(False)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PDF2Booklet", None))
        self.radioButton_Language_Catala.setText(QCoreApplication.translate("MainWindow", u"Catal\u00e0", None))
        self.radioButton_Language_Castellano.setText(QCoreApplication.translate("MainWindow", u"Castellano", None))
        self.radioButton_Language_English.setText(QCoreApplication.translate("MainWindow", u"English", None))
        self.radioButton_Language_Xertoli.setText(QCoreApplication.translate("MainWindow", u"Xertol\u00ed", None))
        self.label_Stage3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_InsertText.setText(QCoreApplication.translate("MainWindow", u"[Insert blank pages after page number:]", None))
        self.plainTextEdit_ErrorConsole.setPlainText("")
        self.label_Stage1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_Stage2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_LoadFile.setText(QCoreApplication.translate("MainWindow", u"[LOAD FILE]", None))
        self.lineEdit_Insert.setInputMask("")
        self.lineEdit_Insert.setText("")
        self.lineEdit_Insert.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ex: 2,-2", None))
        self.label_NpagesOriginalText.setText(QCoreApplication.translate("MainWindow", u"[Original number of pages:]", None))
        self.label_NpagesOriginal.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_NpagesInsertedText.setText(QCoreApplication.translate("MainWindow", u"[Number of inserted pages:]", None))
        self.label_NpagesInserted.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_ValidText.setText(QCoreApplication.translate("MainWindow", u"[Is it valid?:]", None))
        self.label_Valid.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.pushButton_Convert.setText(QCoreApplication.translate("MainWindow", u"[CONVERT]", None))
        self.label_InsertInstructionText.setText(QCoreApplication.translate("MainWindow", u"[(separate by commas, use negative sign to count from the back)]", None))
        self.radioButton_Save_Whole.setText(QCoreApplication.translate("MainWindow", u"[Save Whole File]", None))
        self.radioButton_Save_Separately.setText(QCoreApplication.translate("MainWindow", u"[Save cover separately]", None))
        self.pushButton_Convert_NoReorder.setText(QCoreApplication.translate("MainWindow", u"[Convert without reordering]", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Info", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Info", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Info", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

