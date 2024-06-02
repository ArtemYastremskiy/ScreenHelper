from PySide6.QtWidgets import QApplication, QRubberBand, QWidget
from PySide6.QtCore import Qt, QRect, QSize, Signal



class ScreenshotWidget(QWidget):
    closed = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Screenshot Widget')
        self.setGeometry(300, 300, 300, 220)
        self.setWindowOpacity(0.1)

        self.selection_started = False
        self.rubberband = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = None
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = event.pos()
            self.rubberband.setGeometry(QRect(self.origin, QSize()))
            self.rubberband.show()
            self.selection_started = True

    def mouseMoveEvent(self, event):
        if self.selection_started:
            self.rubberband.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.selection_started:
            self.selection_started = False
            self.rubberband.hide()
            self.capture_screenshot(self.rubberband.geometry())


    def capture_screenshot(self, geometry):
        screen = QApplication.primaryScreen()
        if screen is not None:
            screenshot = screen.grabWindow(0, geometry.x(), geometry.y(),
                                           geometry.width(), geometry.height())
            
            screenshot.save("screenshot.png")

            self.isDone = True
            self.close()
    
    
    def closeEvent(self, event):
        self.closed.emit()
        event.accept()
