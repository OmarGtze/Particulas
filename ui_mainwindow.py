# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1307, 837)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.action_ordenar_id = QAction(MainWindow)
        self.action_ordenar_id.setObjectName(u"action_ordenar_id")
        self.action_ordenar_distancia = QAction(MainWindow)
        self.action_ordenar_distancia.setObjectName(u"action_ordenar_distancia")
        self.action_ordenar_velocidad = QAction(MainWindow)
        self.action_ordenar_velocidad.setObjectName(u"action_ordenar_velocidad")
        self.action_ver_puntos = QAction(MainWindow)
        self.action_ver_puntos.setObjectName(u"action_ver_puntos")
        self.action_unir_puntos = QAction(MainWindow)
        self.action_unir_puntos.setObjectName(u"action_unir_puntos")
        self.actionDijkstra = QAction(MainWindow)
        self.actionDijkstra.setObjectName(u"actionDijkstra")
        self.actionKruskal = QAction(MainWindow)
        self.actionKruskal.setObjectName(u"actionKruskal")
        self.actionGraham = QAction(MainWindow)
        self.actionGraham.setObjectName(u"actionGraham")
        self.actionPrim = QAction(MainWindow)
        self.actionPrim.setObjectName(u"actionPrim")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(20, 10, 1221, 771))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 2, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.id_label = QLabel(self.groupBox)
        self.id_label.setObjectName(u"id_label")

        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.velocidad_label = QLabel(self.groupBox_4)
        self.velocidad_label.setObjectName(u"velocidad_label")

        self.gridLayout_7.addWidget(self.velocidad_label, 0, 0, 1, 1)

        self.velocidad_spinBox = QSpinBox(self.groupBox_4)
        self.velocidad_spinBox.setObjectName(u"velocidad_spinBox")

        self.gridLayout_7.addWidget(self.velocidad_spinBox, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 4, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_10 = QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.agregarInicio_pushButton = QPushButton(self.groupBox_7)
        self.agregarInicio_pushButton.setObjectName(u"agregarInicio_pushButton")

        self.gridLayout_10.addWidget(self.agregarInicio_pushButton, 0, 0, 1, 1)

        self.agregarFinal_pushButton = QPushButton(self.groupBox_7)
        self.agregarFinal_pushButton.setObjectName(u"agregarFinal_pushButton")

        self.gridLayout_10.addWidget(self.agregarFinal_pushButton, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_7, 5, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.destinoX_spinBox = QSpinBox(self.groupBox_2)
        self.destinoX_spinBox.setObjectName(u"destinoX_spinBox")
        self.destinoX_spinBox.setMaximum(500)

        self.gridLayout_5.addWidget(self.destinoX_spinBox, 3, 3, 1, 1)

        self.destinoX_label = QLabel(self.groupBox_2)
        self.destinoX_label.setObjectName(u"destinoX_label")

        self.gridLayout_5.addWidget(self.destinoX_label, 3, 0, 1, 1)

        self.destinoY_spinBox = QSpinBox(self.groupBox_2)
        self.destinoY_spinBox.setObjectName(u"destinoY_spinBox")
        self.destinoY_spinBox.setMaximum(500)

        self.gridLayout_5.addWidget(self.destinoY_spinBox, 3, 1, 1, 1)

        self.destinoY_label = QLabel(self.groupBox_2)
        self.destinoY_label.setObjectName(u"destinoY_label")

        self.gridLayout_5.addWidget(self.destinoY_label, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.origenY_label = QLabel(self.groupBox_3)
        self.origenY_label.setObjectName(u"origenY_label")

        self.gridLayout_6.addWidget(self.origenY_label, 0, 2, 1, 1)

        self.origenX_spinBox = QSpinBox(self.groupBox_3)
        self.origenX_spinBox.setObjectName(u"origenX_spinBox")

        self.gridLayout_6.addWidget(self.origenX_spinBox, 0, 1, 1, 1)

        self.origenX_label = QLabel(self.groupBox_3)
        self.origenX_label.setObjectName(u"origenX_label")

        self.gridLayout_6.addWidget(self.origenX_label, 0, 0, 1, 1)

        self.origenY_spinBox = QSpinBox(self.groupBox_3)
        self.origenY_spinBox.setObjectName(u"origenY_spinBox")

        self.gridLayout_6.addWidget(self.origenY_spinBox, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 2, 2)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout.addWidget(self.id_lineEdit, 0, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_9 = QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.mostrar_pushButton = QPushButton(self.groupBox_6)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_9.addWidget(self.mostrar_pushButton, 0, 0, 1, 1)

        self.mostrar_grafo_pushButton = QPushButton(self.groupBox_6)
        self.mostrar_grafo_pushButton.setObjectName(u"mostrar_grafo_pushButton")

        self.gridLayout_9.addWidget(self.mostrar_grafo_pushButton, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_6, 5, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_8 = QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.azul_label = QLabel(self.groupBox_5)
        self.azul_label.setObjectName(u"azul_label")

        self.gridLayout_8.addWidget(self.azul_label, 3, 0, 1, 1)

        self.verde_label = QLabel(self.groupBox_5)
        self.verde_label.setObjectName(u"verde_label")

        self.gridLayout_8.addWidget(self.verde_label, 2, 0, 1, 1)

        self.rojo_label = QLabel(self.groupBox_5)
        self.rojo_label.setObjectName(u"rojo_label")

        self.gridLayout_8.addWidget(self.rojo_label, 0, 0, 1, 1)

        self.rojo_spinBox = QSpinBox(self.groupBox_5)
        self.rojo_spinBox.setObjectName(u"rojo_spinBox")
        self.rojo_spinBox.setMaximum(255)

        self.gridLayout_8.addWidget(self.rojo_spinBox, 0, 1, 1, 1)

        self.verde_spinBox = QSpinBox(self.groupBox_5)
        self.verde_spinBox.setObjectName(u"verde_spinBox")
        self.verde_spinBox.setMaximum(255)

        self.gridLayout_8.addWidget(self.verde_spinBox, 2, 1, 1, 1)

        self.azul_spinBox = QSpinBox(self.groupBox_5)
        self.azul_spinBox.setObjectName(u"azul_spinBox")
        self.azul_spinBox.setMaximum(255)

        self.gridLayout_8.addWidget(self.azul_spinBox, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 4, 1, 1, 1)

        self.limpiar_pushButton = QPushButton(self.groupBox)
        self.limpiar_pushButton.setObjectName(u"limpiar_pushButton")

        self.gridLayout.addWidget(self.limpiar_pushButton, 7, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_3.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_3.addWidget(self.buscar_lineEdit, 2, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_3.addWidget(self.buscar_pushButton, 2, 1, 1, 1)

        self.mostrarTabla_pushButton = QPushButton(self.tab_2)
        self.mostrarTabla_pushButton.setObjectName(u"mostrarTabla_pushButton")

        self.gridLayout_3.addWidget(self.mostrarTabla_pushButton, 2, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.grafica_tab = QWidget()
        self.grafica_tab.setObjectName(u"grafica_tab")
        self.grafica_groupBox = QGroupBox(self.grafica_tab)
        self.grafica_groupBox.setObjectName(u"grafica_groupBox")
        self.grafica_groupBox.setGeometry(QRect(0, 20, 1061, 711))
        self.gridLayout_4 = QGridLayout(self.grafica_groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.dibujar_puntos_pushButton = QPushButton(self.grafica_groupBox)
        self.dibujar_puntos_pushButton.setObjectName(u"dibujar_puntos_pushButton")

        self.gridLayout_4.addWidget(self.dibujar_puntos_pushButton, 1, 1, 1, 1)

        self.limpiar_particulas_pushButton = QPushButton(self.grafica_groupBox)
        self.limpiar_particulas_pushButton.setObjectName(u"limpiar_particulas_pushButton")

        self.gridLayout_4.addWidget(self.limpiar_particulas_pushButton, 1, 3, 1, 1)

        self.grafica = QGraphicsView(self.grafica_groupBox)
        self.grafica.setObjectName(u"grafica")

        self.gridLayout_4.addWidget(self.grafica, 0, 0, 1, 4)

        self.dibujar_lineas_pushButton = QPushButton(self.grafica_groupBox)
        self.dibujar_lineas_pushButton.setObjectName(u"dibujar_lineas_pushButton")

        self.gridLayout_4.addWidget(self.dibujar_lineas_pushButton, 1, 0, 1, 1)

        self.fuerza_bruta_pushButton = QPushButton(self.grafica_groupBox)
        self.fuerza_bruta_pushButton.setObjectName(u"fuerza_bruta_pushButton")

        self.gridLayout_4.addWidget(self.fuerza_bruta_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.grafica_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1307, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuOrdenar = QMenu(self.menubar)
        self.menuOrdenar.setObjectName(u"menuOrdenar")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuOrdenar.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuOrdenar.addAction(self.action_ordenar_id)
        self.menuOrdenar.addAction(self.action_ordenar_distancia)
        self.menuOrdenar.addAction(self.action_ordenar_velocidad)
        self.menuAlgoritmos.addAction(self.actionDijkstra)
        self.menuAlgoritmos.addAction(self.actionKruskal)
        self.menuAlgoritmos.addAction(self.actionGraham)
        self.menuAlgoritmos.addAction(self.actionPrim)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.action_ordenar_id.setText(QCoreApplication.translate("MainWindow", u"Por ID", None))
        self.action_ordenar_distancia.setText(QCoreApplication.translate("MainWindow", u"Por Distancia", None))
        self.action_ordenar_velocidad.setText(QCoreApplication.translate("MainWindow", u"Por Velocidad", None))
        self.action_ver_puntos.setText(QCoreApplication.translate("MainWindow", u"Ver Puntos", None))
        self.action_unir_puntos.setText(QCoreApplication.translate("MainWindow", u"Unir Puntos", None))
        self.actionDijkstra.setText(QCoreApplication.translate("MainWindow", u"Dijkstra", None))
        self.actionKruskal.setText(QCoreApplication.translate("MainWindow", u"Kruskal", None))
        self.actionGraham.setText(QCoreApplication.translate("MainWindow", u"Graham", None))
        self.actionPrim.setText(QCoreApplication.translate("MainWindow", u"Prim", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Agrega Part\u00edculas", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">ID</span></p></body></html>", None))
        self.groupBox_4.setTitle("")
        self.velocidad_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Velocidad</span></p></body></html>", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.agregarInicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.agregarFinal_pushButton.setText(QCoreApplication.translate("MainWindow", u"Final", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.destinoX_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">X</span></p></body></html>", None))
        self.destinoY_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Y</span></p></body></html>", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.origenY_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Y</span></p></body></html>", None))
        self.origenX_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">X</span></p></body></html>", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Part\u00edculas", None))
        self.mostrar_grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Grafo", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Colores", None))
        self.azul_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">B</span></p></body></html>", None))
        self.verde_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">G</span></p></body></html>", None))
        self.rojo_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">R</span></p></body></html>", None))
        self.limpiar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.buscar_lineEdit.setText("")
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Identificador de Particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrarTabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.grafica_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Veamos las Part\u00edculas", None))
        self.dibujar_puntos_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar Puntos", None))
        self.limpiar_particulas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.dibujar_lineas_pushButton.setText(QCoreApplication.translate("MainWindow", u"Dibujar Lineas", None))
        self.fuerza_bruta_pushButton.setText(QCoreApplication.translate("MainWindow", u"Fuerza Bruta", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.grafica_tab), QCoreApplication.translate("MainWindow", u"P\u00e1gina", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuOrdenar.setTitle(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

