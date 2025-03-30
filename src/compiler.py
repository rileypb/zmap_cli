
from io import StringIO
import sys
from antlr4 import *  
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException
from zmapLexer import zmapLexer
from zmapParser import zmapParser
# from zmapListenerImpl import zmapListenerImpl
from graph_building_listener import GraphBuildingListener

from map import *




class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseCancellationException((line, column, msg))


class Compiler:
    def compile(self, source):
        try:
            input_stream = InputStream(source)
            lexer = zmapLexer(input_stream)
            lexer.removeErrorListeners()
            lexer.addErrorListener(ThrowingErrorListener())
            stream = CommonTokenStream(lexer)
            parser = zmapParser(stream)
            parser.removeErrorListeners()
            parser.addErrorListener(ThrowingErrorListener())
            tree = parser.parse()
            self.listener = GraphBuildingListener()
            walker = ParseTreeWalker()
            try:
                walker.walk(self.listener, tree)
            except RuntimeError as err:
                raise ParseCancellationException(*err.args)
            return self.listener.maps, None
        except ParseCancellationException as pce:
            return None, pce


                    


 
if __name__ == '__main__':

    kalamontee ="""
   kalamontee {
Courtyard:d<->"Winding Stair"
"Plain Hall":s<->Courtyard
"Plain Hall":n<->"Rec Area"
"Plain Hall":ne<->"Rec Corridor"
"Courtyard":w<->"West Wing"
"Rec Area":e<->"Rec Corridor"
"Rec Corridor":e<->"Mess Corridor"
"Mess Corridor":s<->"Mess Hall"
"Mess Hall":s<->"Kitchen"
"Mess Corridor":n<->"Storage West"
"Mess Corridor":e<->"Dorm Corridor"
"Rec Corridor":n<->"Dorm B"
"Rec Corridor":s<->"Dorm A"
"Dorm A":s<->"SanFac A"
"Dorm B":n<->"SanFac B"
"Dorm Corridor":n<->"Dorm D"
"Dorm D":n<->"SanFac D"
"Dorm Corridor":s<->"Dorm C"
"Dorm C":s<->"SanFac C"
"Dorm Corridor":e<->"Corridor Junction"
"Corridor Junction":n<->"Admin Corridor South"
"Admin Corridor South":e<->"SanFac E"
"Admin Corridor South":n<->"Admin Corridor"
"Corridor Junction":s<->"Mech Corridor North"
"Corridor Junction":e<->"Elevator Lobby"
"Elevator Lobby":e<->"Booth 2"
"Elevator Lobby":n<->"Upper Elevator"
"Elevator Lobby":s<->"Lower Elevator"
"Admin Corridor":n<->"Admin Corridor North"
"Admin Corridor":w<->"Systems Monitors"
"Mech Corridor North":e<->"Storage East"
"Mech Corridor North":w<->ne"Physical Plant"
"Mech Corridor North":s<->"Mech Corridor"
"Physical Plant":se<->w:"Mech Corridor"
"Mech Corridor":e<->"Reactor Control"
"Mech Corridor":s<->"Mech Corridor South"
"Mech Corridor South":sw<->"Tool Room"
"Tool Room":e<->"Machine Shop"
"Mech Corridor South":s<->"Machine Shop"
"Mech Corridor South":se<->"Robot Shop"
"Machine Shop":e<->"Robot Shop"
"Reactor Control":e<->"Reactor Elevator"
"Reactor Control":d-->?
"Admin Corridor North":w<->"Small Office"
"Admin Corridor North":n-->?
"Admin Corridor North":e<->"Plan Room"
"Small Office":w<->"Large Office"
"Booth 1":s<->"Conference Room"
"Conference Room":s<->"Rec Area"
}
"""
#     tower="""
# [Upper Elevator]s<->[Tower Core]
# [Tower Core]ne<->[Comm Room]<
# [Tower Core]u<->[Helipad]
# [Tower Core]sw<->[Observation Deck]

# """
#     kalamontee_shuttle_station="""
# [Waiting Area]e<->[Kalamontee Platform]
# [Waiting Area]s<->[Lower Elevator]
# [Kalamontee Platform]s<->[Shuttle Car Alfie]
# [Shuttle Car Alfie]e<->[Alfie Control East]<
# [Shuttle Car Alfie]w<->[Alfie Control West]<
# """
#     lawanda="""
# [Alfie Control East]w<->[Shuttle Car Alfie]
# [Shuttle Car Alfie]w<->[Alfie Control West]
# [Shuttle Car Alfie]n<->[Lawanda Platform]
# [Lawanda Platform]n<->[Shuttle Car Betty]
# [Shuttle Car Betty]e<->[Betty Control East]
# [Shuttle Car Betty]w<->[Betty Control West]
# [Lawanda Platform]e<->[Escalator]
# [Escalator]e<->[Fork]
# [Fork]ne<->[Systems Corridor West]
# [Fork]se<->[Project Corridor West]
# [Project Corridor West]e<->[Project Corridor]
# [Project Corridor]e<->[Project Corridor East]
# [Project Corridor]s<->[ProjCon Office]
# [ProjCon Office]e<->[Computer Room]
# [Computer Room]n<->[Project Corridor East]
# [Computer Room]ne<->[Main Lab]
# [Computer Room]s<->[Miniaturization Booth]<
# [Main Lab]ne<->w[Radiation Lock West]
# [Radiation Lock West]e<->[Radiation Lock East]
# [Radiation Lock East]e-->?
# [Main Lab]se<->w[Bio Lock West]
# [Bio Lock West]e<->[Bio Lock East]
# [Bio Lock East]e<->[Bio Lab]
# [Auxiliary Booth]n<->[Lab Office]
# [Lab Office]w<->[Bio Lab]
# [Main Lab]s<->[Lab Storage]<
# [Project Corridor East]n<->[Library Lobby]
# [Project Corridor East]e<->[Main Lab]
# [Project Corridor West]w<->[SanFac F]
# [Systems Corridor West]e<->[Systems Corridor]
# [Systems Corridor]e<->[Systems Corridor East]
# [Systems Corridor East]e<->[Physical Plant]
# [Systems Corridor East]n<->[Course Control]
# [Systems Corridor East]s<->[Library Lobby]
# [Library Lobby]w<->[Library]
# [Library Lobby]e<->[Booth 3]<
# [Systems Corridor]n<->[Planetary Defense]
# [Systems Corridor West]nw<->[Infirmary]
# [Systems Corridor West]n<->[Repair Room]
# [Repair Room]n-->*(Behind Small Door)
# """
#     computer = """
# [Station 384]e<->[Strip Near Station]
# [Strip Near Station]n-->[Middle of Strip]
# [Middle of Strip]n<->[Strip Near Relay]
# """

    input_stream = InputStream(kalamontee)
    lexer = zmapLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = zmapParser(stream)
    tree = parser.parse()
    listener = GraphBuildingListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.new_map.position_rooms()
    for room_name in listener.new_map.rooms:
        room = listener.new_map.rooms[room_name]
        print(room)
