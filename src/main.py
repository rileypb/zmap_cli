import sys, os, datetime

from compiler import Compiler

from arrange import Arranger
from layout import Layout
from display import Display

from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QColor, QTextCharFormat
from PyQt5.QtWidgets import QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QBrush
from PyQt5.QtCore import Qt

class ZApp:
    def __init__(self):
        self.application = QApplication(sys.argv)
        self.current_filename = None
        self.zmap_compiler = Compiler()
        self.arranger = Arranger()
        self.layout = Layout()
        self.display = Display()
        self.original_text = ""
        self.scene = None
        self.text = None

    def do_layout(self):
        self.scene.clear()
        self.layout.one_step(map)
        self.display.display(map, self.scene)    

    def textChanged(self, *args):
        if self.highlighter and self.highlighter.is_highlighted():
            self.highlighter.clear_highlight()

    def run(self):
        exit_code = self.appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
        self.settings.sync()
        sys.exit(exit_code)

    def highlight_error(self, line):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor("red"))
        self.highlighter.clear_highlight()
        self.highlighter.highlight_line(line-1, fmt)
        self.win.plainTextEdit.update();

    def compile(self, *args):
        self.maps, exc = self.zmap_compiler.compile(self.text)
        
        if exc:
            raise exc
        else:
            now = datetime.datetime.now()
            time = now.strftime("%H:%M:%S")
            for name, map in self.maps.items():
                print(f"{time} {name} compiled")
                self.arranger.arrange(map)

    def display_map(self, *args):    
        map = None
        for name, m in self.maps.items():
            map = m
        if not map.arranged:
            self.arranger.arrange(map)
            
        self.scene = QGraphicsScene()

        for i in range(200):
            self.layout.one_step(map)

        self.display.display(map, self.scene) 
         
    def export(self):
        pass


    def open_zmap(self):
        self.text = ""
        for line in sys.stdin:
            self.text += line + "\n"

    def save_scene_as_image(self, file_path):
        """Saves the given QGraphicsScene as an image to the specified file path.

        Args:
            scene (QGraphicsScene): The scene to save.
            file_path (str): The path to save the image to.
        """
        self.scene.setBackgroundBrush(QBrush(QColor(255, 255, 255)))  # Set the background color to white
        rect = self.scene.sceneRect()
        image = QImage(rect.size().toSize(), QImage.Format_ARGB32)
        image.fill(0)  # Make the background transparent
        painter = QPainter(image)
        self.scene.render(painter, QRectF(image.rect()), rect)
        painter.end()
        image.save(file_path)

if __name__ == '__main__':
    map = ZApp()
    map.open_zmap()
    map.compile()
    map.display_map()
    map.save_scene_as_image("output.png")