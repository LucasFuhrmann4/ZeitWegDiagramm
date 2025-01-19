from PyQt6.QtCharts import QChartView, QChart, QLineSeries, QValueAxis
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor


class CentralWidget(QChartView):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        # Daten für die Y-Werte des Graphen
        y_values = [0, 10, 12.5, 15, 15, 15, 15, 10, 5]

        # Liniendiagramm erstellen und konfigurieren
        self.__series_line = QLineSeries()
        self.__series_line.setName("Linie")
        self.__series_line.setColor(QColor('lightblue'))

        # Punkte zur Serie hinzufügen
        for x, y in enumerate(y_values, start=1):  # Startet x bei 1
            self.__series_line.append(x, y)

        # X-Achse (Werte 1 bis 9) erstellen und konfigurieren
        x_axis = QValueAxis()
        x_axis.setRange(1, 9)  # Bereich von 1 bis 9
        x_axis.setTickCount(9)  # 9 Ticks (für Werte 1 bis 9)
        x_axis.setTitleText("Zeit")

        # Y-Achse erstellen und konfigurieren
        y_axis = QValueAxis()
        y_axis.setRange(0, 20)  # Bereich von 0 bis 20
        y_axis.setTickCount(5)  # 5 Ticks
        y_axis.setTitleText("in m")

        # Chart erstellen und konfigurieren
        chart = QChart()
        chart.setTitle("Zeit-Weg-Diagramm")
        chart.addSeries(self.__series_line)
        chart.addAxis(x_axis, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(y_axis, Qt.AlignmentFlag.AlignLeft)

        # Achsen an die Serie anhängen
        self.__series_line.attachAxis(x_axis)
        self.__series_line.attachAxis(y_axis)

        # Chart dem QChartView hinzufügen
        self.setChart(chart)

