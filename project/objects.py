from PyQt6.QtWidgets import (QMainWindow, QLabel, QDoubleSpinBox, QPushButton, QTableWidget)

# window
window = QMainWindow()
window.setWindowTitle("Simulation: Currency")
window.setGeometry(350, 300, 270, 200)


# parameters
def SetSpinBox(spin_box: QDoubleSpinBox, above: int) -> None:
    spin_box.setRange(0, 1000)
    spin_box.setSingleStep(0.01)
    spin_box.move(100, above)


def SetLable(label: QLabel, text: str, above: int, left: int = 60) -> None:
    label.setText(text)
    label.move(left, above)


initial_l = QLabel(window)
SetLable(initial_l, "Initial price:", 20)

usd_l = QLabel(window)
usd_sb = QDoubleSpinBox(window)
usd_sb.setValue(74.9)

eur_l = QLabel(window)
eur_sb = QDoubleSpinBox(window)
eur_sb.setValue(79.46)


param = {usd_l: usd_sb, eur_l: eur_sb}
text = ["Usd", "Eur"]
i = 1
for key, value in param.items():
    SetLable(key, text[i - 1], 40 * i + 20)
    SetSpinBox(value, 40 * i + 20)
    i += 1

# buttons
launch_btn = QPushButton(window)
launch_btn.move(20, 150)
launch_btn.setText("Start/Stop")

close_btn = QPushButton(window)
close_btn.move(130, 150)
close_btn.setText("Close")

window.show()

