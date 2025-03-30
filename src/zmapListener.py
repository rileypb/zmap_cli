# Generated from src/zmap.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .zmapParser import zmapParser
else:
    from zmapParser import zmapParser

# This class defines a complete listener for a parse tree produced by zmapParser.
class zmapListener(ParseTreeListener):

    # Enter a parse tree produced by zmapParser#parse.
    def enterParse(self, ctx:zmapParser.ParseContext):
        pass

    # Exit a parse tree produced by zmapParser#parse.
    def exitParse(self, ctx:zmapParser.ParseContext):
        pass


    # Enter a parse tree produced by zmapParser#graph.
    def enterGraph(self, ctx:zmapParser.GraphContext):
        pass

    # Exit a parse tree produced by zmapParser#graph.
    def exitGraph(self, ctx:zmapParser.GraphContext):
        pass


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
        pass


    # Enter a parse tree produced by zmapParser#attr_list.
    def enterAttr_list(self, ctx:zmapParser.Attr_listContext):
        pass

    # Exit a parse tree produced by zmapParser#attr_list.
    def exitAttr_list(self, ctx:zmapParser.Attr_listContext):
        pass


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
        pass


    # Enter a parse tree produced by zmapParser#tuple_.
    def enterTuple_(self, ctx:zmapParser.Tuple_Context):
        pass

    # Exit a parse tree produced by zmapParser#tuple_.
    def exitTuple_(self, ctx:zmapParser.Tuple_Context):
        pass


    # Enter a parse tree produced by zmapParser#edge_stmt.
    def enterEdge_stmt(self, ctx:zmapParser.Edge_stmtContext):
        pass

    # Exit a parse tree produced by zmapParser#edge_stmt.
    def exitEdge_stmt(self, ctx:zmapParser.Edge_stmtContext):
        pass


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
        pass


    # Enter a parse tree produced by zmapParser#dark_unknown.
    def enterDark_unknown(self, ctx:zmapParser.Dark_unknownContext):
        pass

    # Exit a parse tree produced by zmapParser#dark_unknown.
    def exitDark_unknown(self, ctx:zmapParser.Dark_unknownContext):
        pass


    # Enter a parse tree produced by zmapParser#edgeop.
    def enterEdgeop(self, ctx:zmapParser.EdgeopContext):
        pass

    # Exit a parse tree produced by zmapParser#edgeop.
    def exitEdgeop(self, ctx:zmapParser.EdgeopContext):
        pass


    # Enter a parse tree produced by zmapParser#node_stmt.
    def enterNode_stmt(self, ctx:zmapParser.Node_stmtContext):
        pass

    # Exit a parse tree produced by zmapParser#node_stmt.
    def exitNode_stmt(self, ctx:zmapParser.Node_stmtContext):
        pass


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
        pass


    # Enter a parse tree produced by zmapParser#node_id_right.
    def enterNode_id_right(self, ctx:zmapParser.Node_id_rightContext):
        pass

    # Exit a parse tree produced by zmapParser#node_id_right.
    def exitNode_id_right(self, ctx:zmapParser.Node_id_rightContext):
        pass


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