from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import random
from objects import (usd_sb, eur_sb, launch_btn, close_btn)

time: QTimer
plt = pg.PlotWidget
usd: float
eur: float
k = 0.1
count = 0
sensor = False


def check_state():
    if sensor:
        stop()
    else:
        start()


def start():
    global usd, eur, plt, sensor

    sensor = True
    usd = usd_sb.value()
    eur = eur_sb.value()

    title = "Simulation: Currency - GRAPH"
    plt = pg.plot(title=title)
    plt.setBackground("w")
    plt.showGrid(x=True, y=True)
    plt.addLegend()

    timer()


def timer():
    global time

    time = QTimer()
    time.start()
    time.setInterval(1000)
    time.timeout.connect(shot)


def shot():
    global usd, eur, count

    count += 1
    usd = usd * (1 + k * (random.random() - 0.5))
    eur = eur * (1 + k * (random.random() - 0.5))
    draw()


def draw():
    global plt

    if count == 1:
        usd_gr = pg.BarGraphItem(x=[count], y=[usd], width=0.2, height=0.2, brush='#FFD700', name='Usd')
        eur_gr = pg.BarGraphItem(x=[count], y=[eur], width=0.2, height=0.2, brush='#20B2AA', name='Eur')
    else:
        usd_gr = pg.BarGraphItem(x=[count], y=[usd], width=0.2, height=0.2, brush='#FFD700')
        eur_gr = pg.BarGraphItem(x=[count], y=[eur], width=0.2, height=0.2, brush='#20B2AA')

    plt.addItem(usd_gr)
    plt.addItem(eur_gr)


def stop():
    global count, sensor, time

    time.stop()
    time.deleteLater()
    count = 0
    sensor = False


def close():
    pg.exit()


launch_btn.clicked.connect(check_state)
close_btn.clicked.connect(close)
