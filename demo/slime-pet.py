import sys
import random
import logging
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt, QTimer

log = logging.getLogger("SlimePet")  # 日志输出
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
log.addHandler(handler)


class SlimePet(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Slime Pet")
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明背景
        self.setGeometry(100, 100, 200, 200)
        self.slime_color = QColor(0, 255, 0)  # 史莱姆的颜色
        self.eye_color = QColor(255, 255, 255)  # 眼睛的色
        self.eye_size = 10  # 眼睛的大小
        self.eye_pos = (80, 80)  # 眼睛的位置
        self.jump_height = 30  # 跳跃高度
        self.roll_distance = 30  # 滚动距离

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run_forever)
        self.timer.start(1000)  # 每秒运行一次

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.NoPen))
        painter.setBrush(QBrush(self.slime_color))
        painter.drawEllipse(0, 0, self.width(), self.height())
        painter.setBrush(QBrush(self.eye_color))
        painter.drawEllipse(
            self.eye_pos[0], self.eye_pos[1], self.eye_size, self.eye_size
        )

    def _move(self, x, y):
        self.move(self.x() + x, self.y() + y)

    def _move_by_roll(self):
        direction = random.choice(["left", "right", "up", "down"])
        if direction == "left":
            self._move(-self.roll_distance, 0)
        elif direction == "right":
            self._move(self.roll_distance, 0)
        elif direction == "up":
            self._move(0, -self.roll_distance)
        elif direction == "down":
            self._move(0, self.roll_distance)
        log.info(f"Rolling {direction}")

    def _move_by_jump(self):
        self._move(0, -self.jump_height)
        log.info("Jumping")
        self.update()
        QTimer.singleShot(500, self._fall)

    def _fall(self):
        self._move(0, self.jump_height)
        self.update()

    def run_forever(self):
        events = {
            "move_by_roll": self._move_by_roll,
            "move_by_jump": self._move_by_jump,
        }
        event = random.choice(list(events.keys()))
        func = events[event]
        func()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pet = SlimePet()
    pet.show()
    sys.exit(app.exec_())
