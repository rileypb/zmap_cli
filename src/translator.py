import re


source = """
[Sandy Beach]s<->[Shore]
[Sandy Beach]ne<->[Sandy Cave]

[Shore]s<->[Aragain Falls]

"""

with open('out.txt', 'w') as file:
    lines = source.split('\n')
    room_regex = '\[(.*?)\]'
    roomp = re.compile(room_regex)
    passage_regex = '(n|ne|e|se|s|sw|w|nw|d|u)(-->|<->)'
    passp = re.compile(passage_regex)
    right_room_regex='(n|ne|e|se|s|sw|w|nw|d|u)?\[(.*?)](<|>)?'
    right_roomp = re.compile(right_room_regex)
    right_special_regex='\*(?:\[|\()(.*?)(?:\)|\])(<|>)?'
    right_specialp = re.compile(right_special_regex)
    right_unknown_regex='\?'
    right_unknownp = re.compile(right_unknown_regex)
    for line in lines:
        full_line = line
        m = roomp.match(line)
        if m:
            from_room = m[1]
            from_room = from_room.replace(' ', '_')
            line = line[len(from_room) + 2:]
            m2 = passp.match(line)
            direction = m2[1]
            type = m2[2]
            line = line[len(direction) + len(type):]
            file.write(f"{from_room}:{direction}{type}")
            right_room_match = right_roomp.match(line)
            right_special_match = right_specialp.match(line)
            right_unknown_match = right_unknownp.match(line)
            if right_room_match:
                opposite_direction = right_room_match[1]
                opposite_room = right_room_match[2]
                modifier = right_room_match[3]
                opposite_room = opposite_room.replace(' ', '_')
                if opposite_direction:
                    file.write(f'{opposite_direction}:{opposite_room}')
                else:
                    file.write(opposite_room)
                if modifier:
                    modstring = "short" if modifier == '<' else "long"
                    file.write(f" [{modstring}]")
                file.write('\n')
            elif right_special_match:
                special_description = right_special_match[1]
                special_description = special_description.replace(' ', '_')
                modifier = right_special_match[2]
                file.write(f'{special_description}*')
                if modifier:
                    modstring = "short" if modifier == '<' else "long"
                    file.write(f" [{modstring}]")
                file.write('\n')
            elif right_unknown_match:
                file.write('?\n')
            else:
                raise RuntimeError("unmatched line: " + full_line)
            


