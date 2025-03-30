"""
Map, Passage and Room models.
"""

import random

opposites = { 'n': 's', 'ne': 'sw', 'e': 'w', 'se': 'nw', 's': 'n', 'sw': 'ne',
              'w': 'e', 'nw': 'se', 'u': 'd', 'd': 'u', 'in': 'out', 'out': 'in'}

def opposite(direction):
    return opposites[direction]


def get_x_change(direction):
    if 'e' in direction:
        return 1
    if 'w' in direction:
        return -1
    if direction == 'in':
        return 1
    if direction == 'out':
        return -1
    return 0


def get_y_change(direction):
    if direction in ['n', 'nw', 'ne']:
        return 1
    if direction in ['s', 'sw', 'se']:
        return -1
    if direction == 'd':
        return -1
    if direction == 'u':
        return 1
    return 0

scale_by_modifier = { '<': 0.5, '>': 2.0, 'short': 0.5, 'normal': 1.0, 'long': 2.0 }

def calculate_position_for(room, map):
    if room.pos():
        pos = room.pos()
        room.position = (float(pos[0]), float(pos[1]))
        return
    cx = 0
    cy = 0
    count = 0
    for passage in room.passages:
        opposite_room = passage.from_room if passage.to_room == room else passage.to_room
        if opposite_room and opposite_room.position:
            direction = passage.direction if passage.to_room == room else passage.back_direction
            if not direction:
                direction = opposite(passage.direction)
            opposite_position = opposite_room.position
            scale = scale_by_modifier[map.path_length()] 
            scale = scale_by_modifier[passage.modifier()] if passage.modifier() else scale
            
            if passage.to_room.subtype == 'Unknown':
                scale = 0.5
            new_position = (opposite_position[0] + scale*get_x_change(direction), opposite_position[1] + scale*get_y_change(direction))
            cx += new_position[0]
            cy += new_position[1]
            count += 1

            if not passage.to_room.subtype:
                opposite_direction = passage.back_direction if passage.to_room == room else passage.direction
                if not opposite_direction:
                    opposite_direction = opposite(passage.direction)
                new_position = (opposite_position[0] - scale * get_x_change(opposite_direction), opposite_position[1] - scale * get_y_change(opposite_direction))
                cx += new_position[0]
                cy += new_position[1]
                count += 1

    room.position = (cx / max(1, count), cy / max(1, count))



class Passage:
    def __init__(self):
        self.from_room = None
        self.direction = None
        self.back_direction = None
        self.to_room = None
        self.attrs = {}
        self.two_way = False

    # def __init__(self, from_room, direction, to_room=None, back_direction=None, modifier=None, two_way=False) -> None:
    #     self.from_room = from_room
    #     self.direction = direction
    #     self.to_room = to_room
    #     self.from_room.passages.append(self)
    #     if to_room:
    #         to_room.passages.append(self)
    #     self.modifier = modifier
    #     self.two_way = two_way
    #     if back_direction:
    #         self.back_direction = back_direction
    #     else:
    #         self.back_direction = opposite(direction)

    def splines(self) -> bool:
        return self.attrs.get("splines", "inherit")

    def set_left_end(self, room, port:str) -> None:
        self.from_room = room
        self.from_room.add_passage(self)
        self.direction = port

    def set_right_end(self, room, port:str) -> None:
        self.to_room = room
        self.to_room.add_passage(self)
        self.back_direction = port

    def set_attrs(self, attrs:dict) -> None:
        self.attrs.update(attrs)

    def set_one_way(self) -> None:
        self.two_way = False

    def set_two_way(self) -> None:
        self.two_way = True

    def get_back_direction(self) -> str:
        return self.back_direction or opposite(self.direction)
    
    def draw_arrows(self) -> bool:
        return not self.attrs.get("noarrows", False)
    
    def hidden(self) -> bool:
        return self.attrs.get("hidden", False)

    def modifier(self) -> str:
        if "short" in self.attrs:
            return 'short'
        if "long" in self.attrs:
            return 'long'
        if "normal" in self.attrs:
            return "normal"
        return None

    def __str__(self):
        if self.to_room:
            return f'[{self.from_room}]{self.direction}-->[{self.to_room}]'
        else:
            return f'[{self.from_room}]{self.direction}-->?'


    def __repr__(self):
        return self.__str__()



def remove_underscores(text:str) -> str:
    return text.replace('_', ' ')

def remove_quotes(text:str) -> str:
    if text[0] == '"' and text[-1] == '"':
        return text[1:-1]
    return text

class Room:
    def __init__(self, id, label, subtype=None, free=False) -> None:
        self.id = id

        self.name = label
        self.subtype = subtype
        self.position = None
        self.passages = []
        self.attrs = {}

    def dark(self):
        return self.attrs.get("dark", False)

    def free(self):
        return self.subtype or self.attrs.get("free", False)

    def fixed(self) -> bool:
        return self.attrs.get("fixed", False)

    def pos(self) -> tuple:
        return self.attrs.get("pos", None)

    def set_attrs(self, attrs:dict) -> None:
        self.attrs.update(attrs)

    def add_passage(self, passage):
        self.passages.append(passage)
    
    def label(self) -> str:
        return self.attrs.get("label", None)

    def display_name(self) -> str:
        if self.subtype == 'Unknown':
            return '?'
        return remove_quotes(remove_underscores(self.label() or self.name or self.id))

    def __str__(self):
        return f'[{self.display_name()}]'

    def __repr__(self):
        return self.__str__()

class Map:
    def __init__(self, id_) -> None:
        self.id_ = id_
        self.first_room = None
        self.rooms = {}
        self.passages = []
        self.arranged = False
        self.options = {}
        self.graph_attrs:dict = {}
        self.node_attrs:dict = {}
        self.edge_attrs:dict = {}

    def display_name(self):
        return remove_quotes(remove_underscores(self.id_))

    def set_option(self,key, value):
        self.options[key] = value

    def path_length(self):
        return self.graph_attrs.get("path_length", "normal")

    def splines(self) -> bool:
        return "splines" in self.graph_attrs

    def free(self) -> bool:
        return "free" in self.graph_attrs and self.graph_attrs["free"]

    def add_room(self, id, label=None, subtype=None, free=False):
        if id not in self.rooms.keys():
            room = Room(id, label=label, subtype=subtype, free=free)
            self.rooms[id] = room
            if not self.first_room:
                self.first_room = room
            return room
        elif free:
            room = self.rooms[id]
            room.free = free
        return self.rooms[id]

    def set_graph_attrs(self, attrs:dict):
        self.graph_attrs.update(**attrs)

    def set_node_attrs(self, attrs:dict):
        self.node_attrs.update(**attrs)

    def set_edge_attrs(self, attrs:dict):
        self.edge_attrs.update(**attrs)

    def add_passage(self):
        from_passage = Passage()
        self.passages.append(from_passage)
        return from_passage

    def position_rooms(self):
        if not self.first_room:
            return
        rooms_by_position = {}
        all_rooms = list(self.rooms.values())
        current_node = self.first_room
        current_node.position = (0, 0)
        frontier = [current_node]
        while all_rooms or frontier:
            while frontier:
                current_node = frontier.pop(0)
                all_rooms.remove(current_node)
                for passage in current_node.passages:
                    next_room = passage.from_room if passage.to_room == current_node else passage.to_room
                    if not next_room or next_room.position:
                        continue
                    frontier.append(next_room)
                    if not next_room.position:
                        calculate_position_for(next_room, self)
                    rooms_by_position[next_room.position] = next_room
            if all_rooms:
                one_room = all_rooms[0]
                frontier.append(one_room)
                one_room.position = (0, 0)

    def __str__(self):
        return self.display_name()


    
