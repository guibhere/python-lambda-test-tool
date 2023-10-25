# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lambda-test-tool-ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setBaseSize(QtCore.QSize(800, 600))
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setMidLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(12)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.evento_groupBox = QtWidgets.QGroupBox(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.evento_groupBox.sizePolicy().hasHeightForWidth())
        self.evento_groupBox.setSizePolicy(sizePolicy)
        self.evento_groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.evento_groupBox.setBaseSize(QtCore.QSize(0, 1000))
        self.evento_groupBox.setToolTipDuration(-2)
        self.evento_groupBox.setAutoFillBackground(True)
        self.evento_groupBox.setFlat(True)
        self.evento_groupBox.setObjectName("evento_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.evento_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.evento_textEdit = QtWidgets.QTextEdit(self.evento_groupBox)
        self.evento_textEdit.setMinimumSize(QtCore.QSize(0, 180))
        self.evento_textEdit.setObjectName("evento_textEdit")
        self.gridLayout_2.addWidget(self.evento_textEdit, 0, 0, 1, 1)
        self.logger_grouBox = QtWidgets.QGroupBox(self.splitter)
        self.logger_grouBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.logger_grouBox.setFont(font)
        self.logger_grouBox.setAutoFillBackground(True)
        self.logger_grouBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.logger_grouBox.setFlat(True)
        self.logger_grouBox.setObjectName("logger_grouBox")
        self.gridLayout = QtWidgets.QGridLayout(self.logger_grouBox)
        self.gridLayout.setObjectName("gridLayout")
        self.logger_textBrowser = QtWidgets.QTextBrowser(self.logger_grouBox)
        self.logger_textBrowser.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logger_textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.logger_textBrowser.setObjectName("logger_textBrowser")
        self.gridLayout.addWidget(self.logger_textBrowser, 1, 0, 2, 1)
        self.terminal_logger_checkBox = QtWidgets.QCheckBox(self.logger_grouBox)
        self.terminal_logger_checkBox.setChecked(True)
        self.terminal_logger_checkBox.setObjectName("terminal_logger_checkBox")
        self.gridLayout.addWidget(self.terminal_logger_checkBox, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 1, 0, 1, 1)
        self.config_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.config_groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.config_groupBox.setAutoFillBackground(True)
        self.config_groupBox.setObjectName("config_groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.config_groupBox)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self._2 = QtWidgets.QGridLayout()
        self._2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self._2.setContentsMargins(2, 2, -1, 2)
        self._2.setSpacing(2)
        self._2.setObjectName("_2")
        self.label = QtWidgets.QLabel(self.config_groupBox)
        self.label.setObjectName("label")
        self._2.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4 = QtWidgets.QLabel(self.config_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setMaximumSize(QtCore.QSize(999, 999))
        self.label_4.setObjectName("label_4")
        self._2.addWidget(self.label_4, 1, 0, 1, 1)
        self.evento_comboBox = QtWidgets.QComboBox(self.config_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.evento_comboBox.sizePolicy().hasHeightForWidth())
        self.evento_comboBox.setSizePolicy(sizePolicy)
        self.evento_comboBox.setMinimumSize(QtCore.QSize(300, 0))
        self.evento_comboBox.setObjectName("evento_comboBox")
        self._2.addWidget(self.evento_comboBox, 3, 1, 1, 1)
        self.select_dep_dir_pushButton = QtWidgets.QPushButton(self.config_groupBox)
        self.select_dep_dir_pushButton.setMinimumSize(QtCore.QSize(0, 32))
        self.select_dep_dir_pushButton.setObjectName("select_dep_dir_pushButton")
        self._2.addWidget(self.select_dep_dir_pushButton, 1, 2, 1, 1)
        self.select_lambda_pushButton = QtWidgets.QPushButton(self.config_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_lambda_pushButton.sizePolicy().hasHeightForWidth())
        self.select_lambda_pushButton.setSizePolicy(sizePolicy)
        self.select_lambda_pushButton.setMinimumSize(QtCore.QSize(150, 32))
        self.select_lambda_pushButton.setMaximumSize(QtCore.QSize(0, 0))
        self.select_lambda_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.select_lambda_pushButton.setObjectName("select_lambda_pushButton")
        self._2.addWidget(self.select_lambda_pushButton, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_2 = QtWidgets.QLabel(self.config_groupBox)
        self.label_2.setObjectName("label_2")
        self._2.addWidget(self.label_2, 2, 0, 1, 1)
        self.dep_path_TextEdit = QtWidgets.QPlainTextEdit(self.config_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dep_path_TextEdit.sizePolicy().hasHeightForWidth())
        self.dep_path_TextEdit.setSizePolicy(sizePolicy)
        self.dep_path_TextEdit.setMinimumSize(QtCore.QSize(360, 24))
        self.dep_path_TextEdit.setMaximumSize(QtCore.QSize(9464646, 24))
        self.dep_path_TextEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.dep_path_TextEdit.setObjectName("dep_path_TextEdit")
        self._2.addWidget(self.dep_path_TextEdit, 1, 1, 1, 1)
        self.app_path_textEdit = QtWidgets.QTextEdit(self.config_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.app_path_textEdit.sizePolicy().hasHeightForWidth())
        self.app_path_textEdit.setSizePolicy(sizePolicy)
        self.app_path_textEdit.setMinimumSize(QtCore.QSize(360, 24))
        self.app_path_textEdit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.app_path_textEdit.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.app_path_textEdit.setFont(font)
        self.app_path_textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.app_path_textEdit.setAutoFillBackground(False)
        self.app_path_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.app_path_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.app_path_textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.app_path_textEdit.setObjectName("app_path_textEdit")
        self._2.addWidget(self.app_path_textEdit, 0, 1, 1, 1)
        self.handler_name_textEdit = QtWidgets.QPlainTextEdit(self.config_groupBox)
        self.handler_name_textEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.handler_name_textEdit.sizePolicy().hasHeightForWidth())
        self.handler_name_textEdit.setSizePolicy(sizePolicy)
        self.handler_name_textEdit.setMinimumSize(QtCore.QSize(128, 24))
        self.handler_name_textEdit.setMaximumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.handler_name_textEdit.setFont(font)
        self.handler_name_textEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.handler_name_textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.handler_name_textEdit.setAutoFillBackground(False)
        self.handler_name_textEdit.setLineWidth(1)
        self.handler_name_textEdit.setObjectName("handler_name_textEdit")
        self._2.addWidget(self.handler_name_textEdit, 2, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3 = QtWidgets.QLabel(self.config_groupBox)
        self.label_3.setObjectName("label_3")
        self._2.addWidget(self.label_3, 3, 0, 1, 1)
        self.horizontalLayout.addLayout(self._2)
        self.gridLayout_3.addWidget(self.config_groupBox, 0, 0, 1, 1)
        self.invoke_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.invoke_groupBox.setObjectName("invoke_groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.invoke_groupBox)
        self.gridLayout_5.setContentsMargins(-1, 2, -1, 2)
        self.gridLayout_5.setVerticalSpacing(1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.invoke_async_checkBox = QtWidgets.QCheckBox(self.invoke_groupBox)
        self.invoke_async_checkBox.setObjectName("invoke_async_checkBox")
        self.gridLayout_5.addWidget(self.invoke_async_checkBox, 0, 0, 1, 1)
        self.limpar_cache_modulos_checkBox = QtWidgets.QCheckBox(self.invoke_groupBox)
        self.limpar_cache_modulos_checkBox.setChecked(True)
        self.limpar_cache_modulos_checkBox.setObjectName("limpar_cache_modulos_checkBox")
        self.gridLayout_5.addWidget(self.limpar_cache_modulos_checkBox, 2, 0, 1, 1)
        self.invoke_lambda_pushButton = QtWidgets.QPushButton(self.invoke_groupBox)
        self.invoke_lambda_pushButton.setMinimumSize(QtCore.QSize(233, 32))
        self.invoke_lambda_pushButton.setStyleSheet("")
        self.invoke_lambda_pushButton.setIconSize(QtCore.QSize(48, 48))
        self.invoke_lambda_pushButton.setObjectName("invoke_lambda_pushButton")
        self.gridLayout_5.addWidget(self.invoke_lambda_pushButton, 0, 1, 3, 1)
        self.gridLayout_3.addWidget(self.invoke_groupBox, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbrir_Json = QtWidgets.QAction(MainWindow)
        self.actionAbrir_Json.setObjectName("actionAbrir_Json")
        self.actionSalvar_Json = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Json.setObjectName("actionSalvar_Json")
        self.actionSelecionar_diretorio_de_eventos = QtWidgets.QAction(MainWindow)
        self.actionSelecionar_diretorio_de_eventos.setObjectName("actionSelecionar_diretorio_de_eventos")
        self.actionInstalar_dependencias_do_projeto_requirements_txt = QtWidgets.QAction(MainWindow)
        self.actionInstalar_dependencias_do_projeto_requirements_txt.setObjectName("actionInstalar_dependencias_do_projeto_requirements_txt")
        self.menuFile.addAction(self.actionAbrir_Json)
        self.menuFile.addAction(self.actionSalvar_Json)
        self.menuFile.addAction(self.actionSelecionar_diretorio_de_eventos)
        self.menuFile.addAction(self.actionInstalar_dependencias_do_projeto_requirements_txt)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Lambda Test Tool"))
        self.evento_groupBox.setToolTip(_translate("MainWindow", "Aqui é mostrado o payload de seu evento!"))
        self.evento_groupBox.setTitle(_translate("MainWindow", "Evento"))
        self.logger_grouBox.setToolTip(_translate("MainWindow", "Configurações para a invocação da lambda"))
        self.logger_grouBox.setTitle(_translate("MainWindow", "Logger"))
        self.terminal_logger_checkBox.setToolTip(_translate("MainWindow", "Se marcado a ferramenta ira logar tanto no terminal quanto em sua caixa de texto."))
        self.terminal_logger_checkBox.setText(_translate("MainWindow", "Logar no terminal"))
        self.config_groupBox.setTitle(_translate("MainWindow", "Configurações"))
        self.label.setToolTip(_translate("MainWindow", "Localização do entrypoint da aplicação lambda."))
        self.label.setText(_translate("MainWindow", "Aplicação Lambda: "))
        self.label_4.setToolTip(_translate("MainWindow", "Caminho para o diretorio da raiz de dependencias do projeto."))
        self.label_4.setText(_translate("MainWindow", "Raiz das dependencias:"))
        self.evento_comboBox.setToolTip(_translate("MainWindow", "Payload/evento com o qual a lambda será invocada."))
        self.select_dep_dir_pushButton.setText(_translate("MainWindow", "Selecionar diretorio raiz"))
        self.select_lambda_pushButton.setText(_translate("MainWindow", "Selecionar Lambda Function"))
        self.label_2.setToolTip(_translate("MainWindow", "Nome do método handler da aplicação."))
        self.label_2.setText(_translate("MainWindow", "Lambda Handler:"))
        self.dep_path_TextEdit.setToolTip(_translate("MainWindow", "Caminho para o diretorio da raiz de dependencias do projeto."))
        self.app_path_textEdit.setToolTip(_translate("MainWindow", "Localização do entrypoint da aplicação lambda."))
        self.app_path_textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:7pt;\"><br /></p></body></html>"))
        self.handler_name_textEdit.setToolTip(_translate("MainWindow", "Nome do método handler da aplicação."))
        self.label_3.setToolTip(_translate("MainWindow", "Payload/evento com o qual a lambda será invocada."))
        self.label_3.setText(_translate("MainWindow", "Selecionar evento:"))
        self.invoke_groupBox.setTitle(_translate("MainWindow", "Invoke"))
        self.invoke_async_checkBox.setToolTip(_translate("MainWindow", "Opção experimental:  permite a invocação da lambda de forma assíncrona, liberando a thread principal da tela."))
        self.invoke_async_checkBox.setText(_translate("MainWindow", "Invocação assíncrona"))
        self.limpar_cache_modulos_checkBox.setToolTip(_translate("MainWindow", "<html><head/><body><p>Limpa o cache de módulos entre execuções, permitindo a edição de dependências entre invocações.</p></body></html>"))
        self.limpar_cache_modulos_checkBox.setText(_translate("MainWindow", "Limpar module cache entre execuções"))
        self.invoke_lambda_pushButton.setToolTip(_translate("MainWindow", "Invocar a lambda de acordo com as definições."))
        self.invoke_lambda_pushButton.setText(_translate("MainWindow", "Invocar Lambda"))
        self.invoke_lambda_pushButton.setShortcut(_translate("MainWindow", "Shift+F5"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionAbrir_Json.setText(_translate("MainWindow", "Abrir Json"))
        self.actionSalvar_Json.setText(_translate("MainWindow", "Salvar Json"))
        self.actionSelecionar_diretorio_de_eventos.setText(_translate("MainWindow", "Selecionar diretorio de eventos"))
        self.actionInstalar_dependencias_do_projeto_requirements_txt.setText(_translate("MainWindow", "Instalar dependencias do projeto(requirements.txt)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
