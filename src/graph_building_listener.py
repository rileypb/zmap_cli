# Generated from /Users/rileypb/dev/zmap/src/main/python/zmap.g4 by ANTLR 4.9.3
from antlr4 import *
from graphviz import Graph
if __name__ is not None and "." in __name__:
    from .zmapParser import zmapParser
else:
    from zmapParser import zmapParser

from map import Map, Room, Passage
from utils import Stack


def remove_underscores(text:str) -> str:
    return text.replace('_', ' ')

def remove_quotes(text:str) -> str:
    if text[0] == '"' and text[-1] == '"':
        return text[1:-1]
    return text

directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'u', 'd', 'in', 'out']

# This class defines a complete listener for a parse tree produced by zmapParser.
class GraphBuildingListener(ParseTreeListener):

    # Enter a parse tree produced by zmapParser#parse.
    def enterParse(self, ctx:zmapParser.ParseContext):
        self.maps = {}
        self.context_stack:Stack = Stack()
        self.attrs = None

    # Exit a parse tree produced by zmapParser#parse.
    def exitParse(self, ctx:zmapParser.ParseContext):
        pass


    # Enter a parse tree produced by zmapParser#graph.
    def enterGraph(self, ctx:zmapParser.GraphContext):
        id_ = remove_quotes(remove_underscores(ctx.id_().getText()))
        self.new_map = Map(id_)
        self.maps[id_] = self.new_map
        self.context_stack.append(self.new_map)

    # Exit a parse tree produced by zmapParser#graph.
    def exitGraph(self, ctx:zmapParser.GraphContext):
        self.context_stack.pop()


    # Enter a parse tree produced by zmapParser#stmt_list.
    def enterStmt_list(self, ctx:zmapParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by zmapParser#stmt_list.
    def exitStmt_list(self, ctx:zmapParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by zmapParser#stmt.
    def enterStmt(self, ctx:zmapParser.StmtContext):
        pass

    # Exit a parse tree produced by zmapParser#stmt.
    def exitStmt(self, ctx:zmapParser.StmtContext):
        pass


    # Enter a parse tree produced by zmapParser#attr_stmt.
    def enterAttr_stmt(self, ctx:zmapParser.Attr_stmtContext):
        pass

    # Exit a parse tree produced by zmapParser#attr_stmt.
    def exitAttr_stmt(self, ctx:zmapParser.Attr_stmtContext):
        if ctx.GRAPH():
            self.graph_attr_stmt()
        elif ctx.NODE():
            self.node_attr_stmt()
        elif ctx.EDGE():
            self.edge_attr_stmt()
        else:
            raise RuntimeError("attr stmt of unknown type")
        self.attrs = None

    def graph_attr_stmt(self):
        parent = self.context_stack.peek()
        parent.set_graph_attrs(self.attrs)

    def node_attr_stmt(self):
        parent = self.context_stack.peek()
        parent.set_node_attrs(self.attrs)

    def edge_attr_stmt(self):
        parent = self.context_stack.peek()
        parent.set_edge_attrs(self.attrs)


    # Enter a parse tree produced by zmapParser#attr_list.
    def enterAttr_list(self, ctx:zmapParser.Attr_listContext):
        self.context_stack.push(dict())

    # Exit a parse tree produced by zmapParser#attr_list.
    def exitAttr_list(self, ctx:zmapParser.Attr_listContext):
        self.attrs = self.context_stack.pop()


    # Enter a parse tree produced by zmapParser#a_list.
    def enterA_list(self, ctx:zmapParser.A_listContext):
        pass

    # Exit a parse tree produced by zmapParser#a_list.
    def exitA_list(self, ctx:zmapParser.A_listContext):
        pass


    # Enter a parse tree produced by zmapParser#attr.
    def enterAttr(self, ctx:zmapParser.AttrContext):
        pass

    # Exit a parse tree produced by zmapParser#attr.
    def exitAttr(self, ctx:zmapParser.AttrContext):
        ids = ctx.id_()
        if len(ids) == 1 and not ctx.tuple_():
            self.context_stack.peek()[ids[0].getText()] = True
        elif len(ids) == 1 and ctx.tuple_():
            actual_tuple = (ctx.tuple_().id_()[0].getText(), ctx.tuple_().id_()[1].getText())
            self.context_stack.peek()[ids[0].getText()] = actual_tuple
        elif len(ids) == 2:
            self.context_stack.peek()[ids[0].getText()] = ids[1].getText()
        else:
            raise RuntimeError(f"Invalid attribute: {ctx.getText()}")


    # Enter a parse tree produced by zmapParser#edge_stmt.
    def enterEdge_stmt(self, ctx:zmapParser.Edge_stmtContext):
        passage = self.context_stack.peek().add_passage()
        self.context_stack.push(passage)

    # Exit a parse tree produced by zmapParser#edge_stmt.
    def exitEdge_stmt(self, ctx:zmapParser.Edge_stmtContext):
        passage = self.context_stack.pop()
        if self.attrs:
            passage.set_attrs(self.attrs)
            self.attrs = None


    # Enter a parse tree produced by zmapParser#edgeRHS.
    def enterEdgeRHS(self, ctx:zmapParser.EdgeRHSContext):
        pass

    # Exit a parse tree produced by zmapParser#edgeRHS.
    def exitEdgeRHS(self, ctx:zmapParser.EdgeRHSContext):
        pass


    # Enter a parse tree produced by zmapParser#unknown.
    def enterUnknown(self, ctx:zmapParser.UnknownContext):
        pass

    # Exit a parse tree produced by zmapParser#unknown.
    def exitUnknown(self, ctx:zmapParser.UnknownContext):
        id_ = str(id(ctx))
        room = id_ and self.new_map.add_room(id_)
        self.context_stack.peek().set_right_end(room, None)
        room.subtype = "Unknown"


    # Enter a parse tree produced by zmapParser#dark_unknown.
    def enterDark_unknown(self, ctx:zmapParser.Dark_unknownContext):
        pass

    # Exit a parse tree produced by zmapParser#dark_unknown.
    def exitDark_unknown(self, ctx:zmapParser.Dark_unknownContext):
        id_ = str(id(ctx))
        room = id_ and self.new_map.add_room(id_)
        self.context_stack.peek().set_right_end(room, None)
        room.subtype = "Unknown"
        room.attrs["dark"] = True


    # Enter a parse tree produced by zmapParser#edgeop.
    def enterEdgeop(self, ctx:zmapParser.EdgeopContext):
        pass

    # Exit a parse tree produced by zmapParser#edgeop.
    def exitEdgeop(self, ctx:zmapParser.EdgeopContext):
        op = ctx.getText()
        if op == '-->':
            self.context_stack.peek().set_one_way()
        elif op == '<->':
            self.context_stack.peek().set_two_way()
        else:
            raise RuntimeError(f'Unknown edgeop {op}')


    # Enter a parse tree produced by zmapParser#node_stmt.
    def enterNode_stmt(self, ctx:zmapParser.Node_stmtContext):
        node_id = ctx.node_id().getText()
        room = self.context_stack.peek().add_room(node_id)
        self.context_stack.push(room)

    # Exit a parse tree produced by zmapParser#node_stmt.
    def exitNode_stmt(self, ctx:zmapParser.Node_stmtContext):
        room = self.context_stack.pop()
        if self.attrs:
            room.set_attrs(self.attrs)
            self.attrs = None


    # Enter a parse tree produced by zmapParser#node_id.
    def enterNode_id(self, ctx:zmapParser.Node_idContext):
        pass

    # Exit a parse tree produced by zmapParser#node_id.
    def exitNode_id(self, ctx:zmapParser.Node_idContext):
        pass


    # Enter a parse tree produced by zmapParser#node_id_left.
    def enterNode_id_left(self, ctx:zmapParser.Node_id_leftContext):
        pass

    # Exit a parse tree produced by zmapParser#node_id_left.
    def exitNode_id_left(self, ctx:zmapParser.Node_id_leftContext):
        id_ = ctx.id_() and ctx.id_().getText()
        room = id_ and self.new_map.add_room(id_)
        port_left = ctx.port_left() and ctx.port_left().getText()[1:]
        if port_left not in directions:
            raise RuntimeError((ctx.port_left().start.line, 0, f'Unrecognized direction: {port_left}'),)
        self.context_stack.peek().set_left_end(room, port_left)


    # Enter a parse tree produced by zmapParser#node_id_right.
    def enterNode_id_right(self, ctx:zmapParser.Node_id_rightContext):
        pass

    # Exit a parse tree produced by zmapParser#node_id_right.
    def exitNode_id_right(self, ctx:zmapParser.Node_id_rightContext):
        id_ = ctx.id_() and ctx.id_().getText()
        if ctx.special():
            id_ = str(id(ctx))
        room = id_ and self.new_map.add_room(id_)
        port_right = ctx.port_right() and ctx.port_right().getText()[:-1]
        if port_right and port_right not in directions:
            raise RuntimeError((ctx.port_right().start.line, 0, f'Unrecognized direction: {port_right}'),)
        self.context_stack.peek().set_right_end(room, port_right)
        if ctx.special():
            room.attrs["label"] = ctx.id_().getText()
            room.subtype = "Special"


    # Enter a parse tree produced by zmapParser#special.
    def enterSpecial(self, ctx:zmapParser.SpecialContext):
        pass

    # Exit a parse tree produced by zmapParser#special.
    def exitSpecial(self, ctx:zmapParser.SpecialContext):
        pass


    # Enter a parse tree produced by zmapParser#port_left.
    def enterPort_left(self, ctx:zmapParser.Port_leftContext):
        pass

    # Exit a parse tree produced by zmapParser#port_left.
    def exitPort_left(self, ctx:zmapParser.Port_leftContext):
        pass


    # Enter a parse tree produced by zmapParser#port_right.
    def enterPort_right(self, ctx:zmapParser.Port_rightContext):
        pass

    # Exit a parse tree produced by zmapParser#port_right.
    def exitPort_right(self, ctx:zmapParser.Port_rightContext):
        pass


    # Enter a parse tree produced by zmapParser#id_.
    def enterId_(self, ctx:zmapParser.Id_Context):
        pass

    # Exit a parse tree produced by zmapParser#id_.
    def exitId_(self, ctx:zmapParser.Id_Context):
        pass



del zmapParser