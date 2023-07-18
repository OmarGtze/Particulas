from PySide2.QtWidgets import *
from ui_mainwindow import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import Slot

from random import randint

from listaParticulas import listaParticulas
from particula import Particula
from algoritmos import get_puntos, puntos_mas_cercanos

from pprint import pprint

from kruskal import runKruskal
from prim import prim
from dijkstra import runDijkstra
from graham import coordenadas

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.listaparticulas = listaParticulas()
        self.puntos = []

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregarInicio_pushButton.clicked.connect(self.click_agregarInicio)
        self.ui.agregarFinal_pushButton.clicked.connect(self.click_agregarFinal)

        self.ui.actionAbrir.triggered.connect(self.action_Abrir_Archivo)
        self.ui.actionGuardar.triggered.connect(self.action_Guardar_Archivo)

        self.ui.action_ordenar_id.triggered.connect(self.action_ordenar_id)
        self.ui.action_ordenar_velocidad.triggered.connect(self.action_ordenar_velocidad)
        self.ui.action_ordenar_distancia.triggered.connect(self.action_ordenar_distancia)

        self.ui.dibujar_puntos_pushButton.clicked.connect(self.click_dibujarPuntos)
        self.ui.fuerza_bruta_pushButton.clicked.connect(self.click_fuerzaBruta)

        self.ui.mostrar_grafo_pushButton.clicked.connect(self.click_mostrarGrafo)

        self.ui.mostrarTabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        
        self.ui.limpiar_particulas_pushButton.clicked.connect(self.limpiar_particulas)
        self.scene = QGraphicsScene()
        self.ui.grafica.setScene(self.scene)
        self.ui.dibujar_lineas_pushButton.clicked.connect(self.click_dibujar_lineas)

        self.ui.actionDijkstra.triggered.connect(self.algoritmo_dijkstra)
        self.ui.actionPrim.triggered.connect(self.algoritmo_prim)
        self.ui.actionGraham.triggered.connect(self.algoritmo_graham)
        self.ui.actionKruskal.triggered.connect(self.algoritmo_kruskal)
    
    @Slot()
    def algoritmo_dijkstra(self):
        print("dijkstra")

        self.ui.salida.clear()
        results = runDijkstra('particulas.json')

        for result in results:
            self.ui.salida.insertPlainText(str(result) + '\n')

    @Slot()
    def algoritmo_prim(self):
        print("prim")

        self.ui.salida.clear()
        self.ui.salida.insertPlainText(prim('particulas.json'))

    @Slot()
    def algoritmo_kruskal(self):
        print("kruskal")

        self.ui.salida.clear()

        results = runKruskal('particulas.json')

        for result in results:
            self.ui.salida.insertPlainText(str(result) + '\n') 

    @Slot()
    def algoritmo_graham(self):
        print("graham")

        self.ui.salida.clear()

        results = coordenadas('particulas.json')

        for result in results:
            self.ui.salida.insertPlainText(str(result) + '\n')

    @Slot()
    def click_mostrarGrafo(self):
        print("mostrar grafo")

        grafo ={}

        for particula in self.listaparticulas:
            origen = (particula.origen_x, particula.origen_y)
            destino = (particula.destino_x, particula.destino_y)
            distancia = int(particula.distancia)

            if origen not in grafo:
                grafo[origen] = []

            grafo[origen].append([origen, distancia])

            if destino not in grafo:
                grafo[destino] = []

            grafo[destino].append([origen, distancia])

        pprint(str(grafo))
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(grafo))
        

    @Slot()
    def click_dibujarPuntos(self):
        print("Dibujar puntos")
        pen = QPen()
        pen.setWidth(2)

        for particula in self.listaparticulas:
            r = particula.red
            g = particula.green
            b = particula.blue
            
            color = QColor(r, g, b)
            pen.setColor(color)

            x_origin = particula.origen_x
            y_origin = particula.origen_y
            x_destin = particula.destino_x
            y_destin = particula.destino_y

            self.scene.addEllipse(x_origin, y_origin, 6, 6, pen)
            self.scene.addEllipse(x_destin, y_destin, 6, 6, pen)
    
    @Slot()
    def click_fuerzaBruta(self):
        print("Fuerza bruta")

        pen = QPen()
        pen.setWidth(2)

        for particula in self.listaparticulas:
            punto1 = (particula.origen_x, particula.origen_y, particula.destino_y, particula.destino_y)
            punto2 = (particula.origen_x, particula.origen_y, particula.destino_y, particula.destino_y)

            self.puntos.append(punto1)
            self.puntos.append(punto2)

        resultado = puntos_mas_cercanos(self.puntos)
        pprint(resultado)

        for particula in self.listaparticulas:
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)

            for punto1, punto2 in resultado:
                origen_x = punto1[0]
                origen_y = punto1[1]
                destino_x = punto2[0]
                destino_y = punto2[1]

                self.scene.addLine(origen_x, origen_y, destino_x, destino_y, pen)

    @Slot()
    def action_ordenar_velocidad(self):
        print("ordenar por velocidad")

        self.listaparticulas.ordenar_porVelocidad(self)

    @Slot()
    def action_ordenar_distancia(self):
        print("ordenar por distancia")

        self.listaparticulas.ordenar_porDistancia(self)

    @Slot()
    def action_ordenar_id(self):
        print("ordenar por id")

        self.listaparticulas.ordenar_porID(self)

    @Slot()
    def limpiar_particulas(self):
          print("limpiar")

          self.scene.clear()

    @Slot()
    def click_dibujar_lineas(self):
        pen = QPen()
        pen.setWidth(2)

        for particula in self.listaparticulas:
            r = particula.red
            g = particula.green
            b = particula.blue
            
            color = QColor(r, g, b)
            pen.setColor(color)

            x_origin = particula.origen_x
            y_origin = particula.origen_y
            x_destin = particula.destino_x
            y_destin = particula.destino_y

            self.scene.addEllipse(x_origin, y_origin, 6, 6, pen)
            self.scene.addEllipse(x_destin, y_destin, 6, 6, pen)
            self.scene.addLine(x_origin, y_origin, x_destin, y_destin, pen)

    def wheelEvent(self, event):
        print(event.delta())

        if event.delta() > 0:
            self.ui.grafica.scale(1.2, 1.2)
        else:
            self.ui.grafica.scale(0.8, 0.8)

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()

        encontrado = False
        for particula in self.listaparticulas:
            if id == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(particula.id))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, destino_x_widget)
                self.ui.tabla.setItem(0, 2, origen_x_widget)
                self.ui.tabla.setItem(0, 3, destino_y_widget)
                self.ui.tabla.setItem(0, 4, origen_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, distancia_widget)
                self.ui.tabla.setItem(0, 7, red_widget)
                self.ui.tabla.setItem(0, 8, green_widget)
                self.ui.tabla.setItem(0, 9, blue_widget)

                encontrado = True
                return
            
            if not encontrado:
                QMessageBox.warning(
                    self,
                    "Atencion",
                    f'La particula con el identificador "{id}" no fue encontrado'
                )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Destino X", "Origen X", "Destino Y", "Origen Y", "Velocidad", "Distancia", "Rojo", "Verde", "Azul"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.listaparticulas))

        row = 0
        for particula in self.listaparticulas:
                id_widget = QTableWidgetItem(str(particula.id))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                distancia_widget = QTableWidgetItem(str(particula.distancia))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))

                self.ui.tabla.setItem(row, 0, id_widget)
                self.ui.tabla.setItem(row, 1, destino_x_widget)
                self.ui.tabla.setItem(row, 2, origen_x_widget)
                self.ui.tabla.setItem(row, 3, destino_y_widget)
                self.ui.tabla.setItem(row, 4, origen_y_widget)
                self.ui.tabla.setItem(row, 5, velocidad_widget)
                self.ui.tabla.setItem(row, 6, distancia_widget)
                self.ui.tabla.setItem(row, 7, red_widget)
                self.ui.tabla.setItem(row, 8, green_widget)
                self.ui.tabla.setItem(row, 9, blue_widget)

                row += 1


    @Slot()
    def click_agregarInicio(self):
        id = self.ui.id_lineEdit.text()
        destino_x = self.ui.destinoX_spinBox.value()
        origen_x = self.ui.origenX_spinBox.value()
        destino_y = self.ui.destinoY_spinBox.value()
        origen_y = self.ui.origenY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id, destino_x, origen_x, destino_y, origen_y, velocidad,
                                          rojo, verde, azul)
        
        self.listaparticulas.agregar_inicio(particula)

    @Slot()
    def click_agregarFinal(self):
        id = self.ui.id_lineEdit.text()
        destino_x = self.ui.destinoX_spinBox.value()
        origen_x = self.ui.origenX_spinBox.value()
        destino_y = self.ui.destinoY_spinBox.value()
        origen_y = self.ui.origenY_spinBox.value()
        velocidad = self.ui.velocidad_spinBox.value()
        rojo = self.ui.rojo_spinBox.value()
        verde = self.ui.verde_spinBox.value()
        azul = self.ui.azul_spinBox.value()

        particula = Particula(id, destino_x, origen_x, destino_y, origen_y, velocidad,
                                          rojo, verde, azul)
        self.listaparticulas.agregar_final(particula)

    @Slot()
    def action_Guardar_Archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.listaparticulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Exito",
                "Se pudo crear el archivo" + ubicacion
            )

        else:
            QMessageBox.information(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )

    @Slot()
    def action_Abrir_Archivo(self):
        print("Abrir Archivo")
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        self.listaparticulas.abrir(ubicacion)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.listaparticulas))
