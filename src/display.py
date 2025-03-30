
import math

from PyQt5.QtGui import QColor, QFont, QTextOption, QPolygonF, QBrush, QPen, QPixmap, QPainterPath
from PyQt5.QtCore import Qt, QPointF, QRectF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem

from map import get_x_change, get_y_change

TEXT_COLOR = QColor("black")
DARK_TEXT_COLOR = QColor("white")
DARK_COLOR = QColor("#555555")
FONT = QFont("sans-serif", pointSize=10)
SMALL_FONT = QFont("sans-serif", pointSize=6)
TEXT_OPTION = QTextOption(Qt.AlignCenter)

ELLIPSE_SCALE = 1 / math.sqrt(2)
ARROWHEAD_SCALE = 5
ARROWHEAD_BRUSH = QBrush()
ARROWHEAD_BRUSH.setColor(QColor("black"))
ARROWHEAD_BRUSH.setStyle(Qt.SolidPattern)
DASH_PEN = QPen()
DASH_PEN.setDashPattern([5, 5])
DASH_DOT_PEN = QPen()
DASH_DOT_PEN.setStyle(Qt.PenStyle.DashDotLine)
DASH_DOT_PEN.setWidth(2)
DOT_PEN = QPen()
DOT_PEN.setStyle(Qt.PenStyle.DotLine)
DOT_PEN.setWidth(2)
DOT_PEN.setCapStyle(Qt.PenCapStyle.FlatCap)
DASHED_DIRECTION = ['u', 'd', 'in', 'out']


opposites = { 'n': 's', 'ne': 'sw', 'e': 'w', 'se': 'nw', 's': 'n', 'sw': 'ne',
              'w': 'e', 'nw': 'se', 'u': 'd', 'd': 'u', 'in': 'out', 'out': 'in'}

def opposite(direction):
    return opposites[direction]


def attachment_point(subtype, room_rect, direction):
    if not subtype:
        if direction == 'n' or direction == 'u':
            return QPointF(room_rect.x() + room_rect.width() / 2, room_rect.y())
        elif direction == 'ne':
            return QPointF(room_rect.x() + room_rect.width(), room_rect.y())
        elif direction == 'e' or direction == 'in':
            return QPointF(room_rect.x() + room_rect.width(), room_rect.y() + room_rect.height() / 2)
        elif direction == 'se':
            return QPointF(room_rect.x() + room_rect.width(), room_rect.y() + room_rect.height())
        elif direction == 's' or direction == 'd':
            return QPointF(room_rect.x() + room_rect.width() / 2, room_rect.y() + room_rect.height())
        elif direction == 'sw':
            return QPointF(room_rect.x(), room_rect.y() + room_rect.height())
        elif direction == 'w' or direction == 'out':
            return QPointF(room_rect.x(), room_rect.y() + room_rect.height() / 2)
        elif direction == 'nw':
            return QPointF(room_rect.x(), room_rect.y())
        else: 
            raise RuntimeError("I don't understand direction: " + str(direction))

    elif subtype:
        center_x = room_rect.x() + room_rect.width() / 2
        center_y = room_rect.y() + room_rect.height() / 2
        if direction == 'n' or direction == 'u':
            return QPointF(center_x, room_rect.y())
        elif direction == 'ne':
            return QPointF(center_x + room_rect.width() / 2 * ELLIPSE_SCALE, center_y - room_rect.height() / 2 * ELLIPSE_SCALE)
        elif direction == 'e' or direction == 'in':
            return QPointF(room_rect.x() + room_rect.width(), center_y)
        elif direction == 'se':
            return QPointF(center_x + room_rect.width() / 2 * ELLIPSE_SCALE, center_y + room_rect.height() / 2 * ELLIPSE_SCALE)
        elif direction == 's' or direction == 'd':
            return QPointF(center_x, room_rect.y() + room_rect.height())
        elif direction == 'sw':
            return QPointF(center_x - room_rect.width() / 2 * ELLIPSE_SCALE, center_y + room_rect.height() / 2 * ELLIPSE_SCALE)
        elif direction == 'w' or direction == 'out':
            return QPointF(room_rect.x(), room_rect.y() + room_rect.height() / 2)
        elif direction == 'nw':
            return QPointF(center_x - room_rect.width() / 2 * ELLIPSE_SCALE, center_y - room_rect.height() / 2 * ELLIPSE_SCALE)
        else: 
            raise RuntimeError("I don't understand direction: " + str(direction))
        


def add_arrowhead(scene, to_point, from_point):
    point1 = to_point
    dx = from_point.x() - to_point.x()
    dy = from_point.y() - to_point.y()
    dist = math.sqrt(dx * dx + dy * dy) + 0.001
    dx /= dist
    dy /= dist
    point_aux = QPointF(point1.x() + ARROWHEAD_SCALE * dx, point1.y() + ARROWHEAD_SCALE * dy)
    odx = ARROWHEAD_SCALE * dy / 2
    ody = ARROWHEAD_SCALE * -dx / 2
    point2 = QPointF(point_aux.x() + odx, point_aux.y() + ody)
    point3 = QPointF(point_aux.x() - odx, point_aux.y() - ody)
    polygon = QPolygonF()
    polygon.append(point1)
    polygon.append(point2)
    polygon.append(point3)
    scene.addPolygon(polygon, brush=ARROWHEAD_BRUSH)

class Display:
    def display(self, map, scene:QGraphicsScene):

         
        room_to_rect = {}
        splines = map.splines()

        for room in map.rooms.values():
            dark = room.dark()
            x = 200+150*room.position[0]
            y = 200+150*room.position[1]
            text = scene.addText(room.display_name())
            text.setPos(x,-y)
            if dark:
                text.setDefaultTextColor(DARK_TEXT_COLOR)
            else:
                text.setDefaultTextColor(TEXT_COLOR)
            text.setZValue(0)

            text.setFont(FONT)
            text.setTextWidth(50)
            text.document().setDefaultTextOption(TEXT_OPTION)
            if len(room.display_name()) > 12:
                text.setFont(SMALL_FONT)
            text_bounding_rect = text.boundingRect()
            room.bounding_rect = QRectF(x - text_bounding_rect.width()/2, -y - text_bounding_rect.height()/2, max(50, text_bounding_rect.width()), text_bounding_rect.height())
            text.setPos(x - text_bounding_rect.width()/2, -y - text_bounding_rect.height()/2)
            if dark:
                brush = QBrush(DARK_COLOR)
            if not room.subtype:
                if dark:
                    rect:QRectF = scene.addRect(room.bounding_rect, brush=brush)
                else:
                    rect:QRectF = scene.addRect(room.bounding_rect)
                room_to_rect[room] = rect
            elif room.subtype:
                if dark:
                    room_to_rect[room] = scene.addEllipse(room.bounding_rect, brush=brush)
                else:
                    room_to_rect[room] = scene.addEllipse(room.bounding_rect)

            text.setZValue(50)

        pairs = {}
        for passage in map.passages:
            from_room = passage.from_room
            to_room = passage.to_room
            if (to_room, from_room) in pairs:
                current = pairs[(to_room, from_room)]
                current.append(passage)
            elif (from_room, to_room) in pairs:
                current = pairs[(from_room, to_room)]
                current.append(passage)
            else:
                pairs[(from_room, to_room)] = [passage]
        
        for passage in map.passages:
            passage_splines = passage.splines()
            if passage_splines == "inherit":
                pass # just use map value
            elif passage_splines == "never":
                splines = False
            elif passage_splines == "always":
                splines = True
            draw_arrows = passage.draw_arrows()
            if passage.two_way:
                from_room = passage.from_room
                to_room = passage.to_room
                from_direction = passage.direction
                to_direction = passage.back_direction
                if not to_direction:
                    to_direction = opposite(from_direction)
                from_point = attachment_point(from_room.subtype, from_room.bounding_rect, from_direction)
                to_point = attachment_point(to_room.subtype, to_room.bounding_rect, to_direction)

                if splines:
                    p = QPainterPath(from_point)
                    ctrl_pt_1 = QPointF(from_point.x() + get_x_change(from_direction)*20, from_point.y() - get_y_change(from_direction)*20)
                    ctrl_pt_2 = QPointF(to_point.x() + get_x_change(to_direction)*20, to_point.y() - get_y_change(to_direction)*20)
                    p.cubicTo(ctrl_pt_1, ctrl_pt_2, to_point)
                    line = scene.addPath(p)
                else:
                    line = scene.addLine(from_point.x(), from_point.y(), to_point.x(), to_point.y())


                if (from_direction in DASHED_DIRECTION or to_direction in DASHED_DIRECTION) and passage.hidden():
                    line.setPen(DASH_DOT_PEN)
                elif from_direction in DASHED_DIRECTION or to_direction in DASHED_DIRECTION:
                    line.setPen(DASH_PEN)
                elif passage.hidden():
                    line.setPen(DOT_PEN)
                if draw_arrows:
                    if splines:
                        add_arrowhead(scene, to_point, ctrl_pt_2)
                        add_arrowhead(scene, from_point, ctrl_pt_1)
                    else:
                        add_arrowhead(scene, to_point, from_point)
                        add_arrowhead(scene, from_point, to_point)
            else:
                from_room = passage.from_room
                to_room = passage.to_room
                from_direction = passage.direction
                to_direction = opposite(passage.direction)
                from_point = attachment_point(from_room.subtype, from_room.bounding_rect, from_direction)
                to_point = attachment_point(to_room.subtype, to_room.bounding_rect, to_direction)

                if splines:
                    p = QPainterPath(from_point)
                    ctrl_pt_1 = QPointF(from_point.x() + get_x_change(from_direction)*20, from_point.y() - get_y_change(from_direction)*20)
                    ctrl_pt_2 = QPointF(to_point.x() + get_x_change(to_direction)*20, to_point.y() - get_y_change(to_direction)*20)
                    p.cubicTo(ctrl_pt_1, ctrl_pt_2, to_point)
                    line = scene.addPath(p)
                else:
                    line = scene.addLine(from_point.x(), from_point.y(), to_point.x(), to_point.y())


                if from_direction in DASHED_DIRECTION and passage.hidden():
                    line.setPen(DASH_DOT_PEN)
                elif from_direction in DASHED_DIRECTION:
                    line.setPen(DASH_PEN)
                elif passage.hidden():
                    line.setPen(DOT_PEN)
                if draw_arrows:
                    if splines:
                        add_arrowhead(scene, to_point, ctrl_pt_2)
                    else:
                        add_arrowhead(scene, to_point, from_point)
        

        # pixmap = QPixmap(self.background_image)
        # height = pixmap.height()
        # width = pixmap.width()
        # x_offset = scene.sceneRect().x() - 500
        # y_offset = scene.sceneRect().y() - 500
        # rect_width = scene.sceneRect().width() + 1000
        # rect_height = scene.sceneRect().height() + 1000
        # num_x = int(rect_width // width + 1)
        # num_y = int(rect_height // height + 1)
        # for i in range(0,num_x):
        #     for j in range(0,num_y):
        #         pixmap_item = QGraphicsPixmapItem(pixmap)
        #         pixmap_item.setOffset(x_offset + i*width, y_offset + j*height)
        #         scene.addItem(pixmap_item)
        #         pixmap_item.setZValue(-1)
