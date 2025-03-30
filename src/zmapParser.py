# Generated from src/zmap.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,24,154,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,1,1,1,1,1,1,1,1,1,1,
        2,1,2,3,2,57,8,2,5,2,59,8,2,10,2,12,2,62,9,2,1,3,1,3,1,3,3,3,67,
        8,3,1,4,1,4,1,4,1,5,1,5,3,5,74,8,5,1,5,4,5,77,8,5,11,5,12,5,78,1,
        6,1,6,3,6,83,8,6,5,6,85,8,6,10,6,12,6,88,9,6,1,6,1,6,1,7,1,7,1,7,
        3,7,95,8,7,1,7,1,7,1,7,1,7,3,7,101,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,
        9,1,9,1,9,3,9,112,8,9,1,10,1,10,1,10,1,10,3,10,118,8,10,1,11,1,11,
        1,12,1,12,1,13,1,13,1,14,1,14,3,14,128,8,14,1,15,1,15,3,15,132,8,
        15,1,16,1,16,1,16,1,17,3,17,138,8,17,1,17,1,17,3,17,142,8,17,1,18,
        1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,0,0,22,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,0,3,1,0,16,
        18,1,0,12,13,1,0,19,21,149,0,45,1,0,0,0,2,49,1,0,0,0,4,60,1,0,0,
        0,6,66,1,0,0,0,8,68,1,0,0,0,10,76,1,0,0,0,12,86,1,0,0,0,14,100,1,
        0,0,0,16,102,1,0,0,0,18,108,1,0,0,0,20,113,1,0,0,0,22,119,1,0,0,
        0,24,121,1,0,0,0,26,123,1,0,0,0,28,125,1,0,0,0,30,129,1,0,0,0,32,
        133,1,0,0,0,34,137,1,0,0,0,36,143,1,0,0,0,38,145,1,0,0,0,40,148,
        1,0,0,0,42,151,1,0,0,0,44,46,3,2,1,0,45,44,1,0,0,0,46,47,1,0,0,0,
        47,45,1,0,0,0,47,48,1,0,0,0,48,1,1,0,0,0,49,50,3,42,21,0,50,51,5,
        1,0,0,51,52,3,4,2,0,52,53,5,2,0,0,53,3,1,0,0,0,54,56,3,6,3,0,55,
        57,5,3,0,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,54,1,0,0,
        0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,5,1,0,0,0,62,60,1,
        0,0,0,63,67,3,28,14,0,64,67,3,18,9,0,65,67,3,8,4,0,66,63,1,0,0,0,
        66,64,1,0,0,0,66,65,1,0,0,0,67,7,1,0,0,0,68,69,7,0,0,0,69,70,3,10,
        5,0,70,9,1,0,0,0,71,73,5,4,0,0,72,74,3,12,6,0,73,72,1,0,0,0,73,74,
        1,0,0,0,74,75,1,0,0,0,75,77,5,5,0,0,76,71,1,0,0,0,77,78,1,0,0,0,
        78,76,1,0,0,0,78,79,1,0,0,0,79,11,1,0,0,0,80,82,3,14,7,0,81,83,5,
        6,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,80,1,0,0,0,85,
        88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,
        0,89,90,3,14,7,0,90,13,1,0,0,0,91,94,3,42,21,0,92,93,5,7,0,0,93,
        95,3,42,21,0,94,92,1,0,0,0,94,95,1,0,0,0,95,101,1,0,0,0,96,97,3,
        42,21,0,97,98,5,7,0,0,98,99,3,16,8,0,99,101,1,0,0,0,100,91,1,0,0,
        0,100,96,1,0,0,0,101,15,1,0,0,0,102,103,5,8,0,0,103,104,3,42,21,
        0,104,105,5,6,0,0,105,106,3,42,21,0,106,107,5,9,0,0,107,17,1,0,0,
        0,108,109,3,32,16,0,109,111,3,20,10,0,110,112,3,10,5,0,111,110,1,
        0,0,0,111,112,1,0,0,0,112,19,1,0,0,0,113,117,3,26,13,0,114,118,3,
        34,17,0,115,118,3,22,11,0,116,118,3,24,12,0,117,114,1,0,0,0,117,
        115,1,0,0,0,117,116,1,0,0,0,118,21,1,0,0,0,119,120,5,10,0,0,120,
        23,1,0,0,0,121,122,5,11,0,0,122,25,1,0,0,0,123,124,7,1,0,0,124,27,
        1,0,0,0,125,127,3,30,15,0,126,128,3,10,5,0,127,126,1,0,0,0,127,128,
        1,0,0,0,128,29,1,0,0,0,129,131,3,42,21,0,130,132,3,36,18,0,131,130,
        1,0,0,0,131,132,1,0,0,0,132,31,1,0,0,0,133,134,3,42,21,0,134,135,
        3,38,19,0,135,33,1,0,0,0,136,138,3,40,20,0,137,136,1,0,0,0,137,138,
        1,0,0,0,138,139,1,0,0,0,139,141,3,42,21,0,140,142,3,36,18,0,141,
        140,1,0,0,0,141,142,1,0,0,0,142,35,1,0,0,0,143,144,5,14,0,0,144,
        37,1,0,0,0,145,146,5,15,0,0,146,147,3,42,21,0,147,39,1,0,0,0,148,
        149,3,42,21,0,149,150,5,15,0,0,150,41,1,0,0,0,151,152,7,2,0,0,152,
        43,1,0,0,0,16,47,56,60,66,73,78,82,86,94,100,111,117,127,131,137,
        141
    ]

class zmapParser ( Parser ):

    grammarFileName = "zmap.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "';'", "'['", "']'", "','", 
                     "'='", "'('", "')'", "'?'", "'!'", "'-->'", "'<->'", 
                     "'*'", "':'", "'map'", "'room'", "'passage'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "GRAPH", "NODE", "EDGE", "NUMBER", "STRING", "ID", 
                      "COMMENT", "LINE_COMMENT", "WS" ]

    RULE_parse = 0
    RULE_graph = 1
    RULE_stmt_list = 2
    RULE_stmt = 3
    RULE_attr_stmt = 4
    RULE_attr_list = 5
    RULE_a_list = 6
    RULE_attr = 7
    RULE_tuple_ = 8
    RULE_edge_stmt = 9
    RULE_edgeRHS = 10
    RULE_unknown = 11
    RULE_dark_unknown = 12
    RULE_edgeop = 13
    RULE_node_stmt = 14
    RULE_node_id = 15
    RULE_node_id_left = 16
    RULE_node_id_right = 17
    RULE_special = 18
    RULE_port_left = 19
    RULE_port_right = 20
    RULE_id_ = 21

    ruleNames =  [ "parse", "graph", "stmt_list", "stmt", "attr_stmt", "attr_list", 
                   "a_list", "attr", "tuple_", "edge_stmt", "edgeRHS", "unknown", 
                   "dark_unknown", "edgeop", "node_stmt", "node_id", "node_id_left", 
                   "node_id_right", "special", "port_left", "port_right", 
                   "id_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    GRAPH=16
    NODE=17
    EDGE=18
    NUMBER=19
    STRING=20
    ID=21
    COMMENT=22
    LINE_COMMENT=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def graph(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.GraphContext)
            else:
                return self.getTypedRuleContext(zmapParser.GraphContext,i)


        def getRuleIndex(self):
            return zmapParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)




    def parse(self):

        localctx = zmapParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.graph()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(zmapParser.Id_Context,0)


        def stmt_list(self):
            return self.getTypedRuleContext(zmapParser.Stmt_listContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_graph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraph" ):
                listener.enterGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraph" ):
                listener.exitGraph(self)




    def graph(self):

        localctx = zmapParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_graph)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.id_()
            self.state = 50
            self.match(zmapParser.T__0)
            self.state = 51
            self.stmt_list()
            self.state = 52
            self.match(zmapParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.StmtContext)
            else:
                return self.getTypedRuleContext(zmapParser.StmtContext,i)


        def getRuleIndex(self):
            return zmapParser.RULE_stmt_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt_list" ):
                listener.enterStmt_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt_list" ):
                listener.exitStmt_list(self)




    def stmt_list(self):

        localctx = zmapParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4128768) != 0):
                self.state = 54
                self.stmt()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 55
                    self.match(zmapParser.T__2)


                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node_stmt(self):
            return self.getTypedRuleContext(zmapParser.Node_stmtContext,0)


        def edge_stmt(self):
            return self.getTypedRuleContext(zmapParser.Edge_stmtContext,0)


        def attr_stmt(self):
            return self.getTypedRuleContext(zmapParser.Attr_stmtContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = zmapParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stmt)
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.node_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.edge_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.attr_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_list(self):
            return self.getTypedRuleContext(zmapParser.Attr_listContext,0)


        def GRAPH(self):
            return self.getToken(zmapParser.GRAPH, 0)

        def NODE(self):
            return self.getToken(zmapParser.NODE, 0)

        def EDGE(self):
            return self.getToken(zmapParser.EDGE, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_attr_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_stmt" ):
                listener.enterAttr_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_stmt" ):
                listener.exitAttr_stmt(self)




    def attr_stmt(self):

        localctx = zmapParser.Attr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 69
            self.attr_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.A_listContext)
            else:
                return self.getTypedRuleContext(zmapParser.A_listContext,i)


        def getRuleIndex(self):
            return zmapParser.RULE_attr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_list" ):
                listener.enterAttr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_list" ):
                listener.exitAttr_list(self)




    def attr_list(self):

        localctx = zmapParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.match(zmapParser.T__3)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0):
                    self.state = 72
                    self.a_list()


                self.state = 75
                self.match(zmapParser.T__4)
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class A_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.AttrContext)
            else:
                return self.getTypedRuleContext(zmapParser.AttrContext,i)


        def getRuleIndex(self):
            return zmapParser.RULE_a_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA_list" ):
                listener.enterA_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA_list" ):
                listener.exitA_list(self)




    def a_list(self):

        localctx = zmapParser.A_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_a_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 80
                    self.attr()
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==6:
                        self.state = 81
                        self.match(zmapParser.T__5)

             
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 89
            self.attr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.Id_Context)
            else:
                return self.getTypedRuleContext(zmapParser.Id_Context,i)


        def tuple_(self):
            return self.getTypedRuleContext(zmapParser.Tuple_Context,0)


        def getRuleIndex(self):
            return zmapParser.RULE_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr" ):
                listener.enterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr" ):
                listener.exitAttr(self)




    def attr(self):

        localctx = zmapParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attr)
        self._la = 0 # Token type
        try:
            self.state = 100
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.id_()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 92
                    self.match(zmapParser.T__6)
                    self.state = 93
                    self.id_()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.id_()
                self.state = 97
                self.match(zmapParser.T__6)
                self.state = 98
                self.tuple_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tuple_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(zmapParser.Id_Context)
            else:
                return self.getTypedRuleContext(zmapParser.Id_Context,i)


        def getRuleIndex(self):
            return zmapParser.RULE_tuple_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple_" ):
                listener.enterTuple_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple_" ):
                listener.exitTuple_(self)




    def tuple_(self):

        localctx = zmapParser.Tuple_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tuple_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(zmapParser.T__7)
            self.state = 103
            self.id_()
            self.state = 104
            self.match(zmapParser.T__5)
            self.state = 105
            self.id_()
            self.state = 106
            self.match(zmapParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Edge_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edgeRHS(self):
            return self.getTypedRuleContext(zmapParser.EdgeRHSContext,0)


        def node_id_left(self):
            return self.getTypedRuleContext(zmapParser.Node_id_leftContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(zmapParser.Attr_listContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_edge_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge_stmt" ):
                listener.enterEdge_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge_stmt" ):
                listener.exitEdge_stmt(self)




    def edge_stmt(self):

        localctx = zmapParser.Edge_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_edge_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.node_id_left()
            self.state = 109
            self.edgeRHS()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 110
                self.attr_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeRHSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edgeop(self):
            return self.getTypedRuleContext(zmapParser.EdgeopContext,0)


        def node_id_right(self):
            return self.getTypedRuleContext(zmapParser.Node_id_rightContext,0)


        def unknown(self):
            return self.getTypedRuleContext(zmapParser.UnknownContext,0)


        def dark_unknown(self):
            return self.getTypedRuleContext(zmapParser.Dark_unknownContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_edgeRHS

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeRHS" ):
                listener.enterEdgeRHS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeRHS" ):
                listener.exitEdgeRHS(self)




    def edgeRHS(self):

        localctx = zmapParser.EdgeRHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_edgeRHS)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.edgeop()
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 21]:
                self.state = 114
                self.node_id_right()
                pass
            elif token in [10]:
                self.state = 115
                self.unknown()
                pass
            elif token in [11]:
                self.state = 116
                self.dark_unknown()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnknownContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return zmapParser.RULE_unknown

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnknown" ):
                listener.enterUnknown(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnknown" ):
                listener.exitUnknown(self)




    def unknown(self):

        localctx = zmapParser.UnknownContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unknown)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(zmapParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dark_unknownContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return zmapParser.RULE_dark_unknown

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDark_unknown" ):
                listener.enterDark_unknown(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDark_unknown" ):
                listener.exitDark_unknown(self)




    def dark_unknown(self):

        localctx = zmapParser.Dark_unknownContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dark_unknown)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(zmapParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EdgeopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return zmapParser.RULE_edgeop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdgeop" ):
                listener.enterEdgeop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdgeop" ):
                listener.exitEdgeop(self)




    def edgeop(self):

        localctx = zmapParser.EdgeopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_edgeop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Node_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node_id(self):
            return self.getTypedRuleContext(zmapParser.Node_idContext,0)


        def attr_list(self):
            return self.getTypedRuleContext(zmapParser.Attr_listContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_node_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode_stmt" ):
                listener.enterNode_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode_stmt" ):
                listener.exitNode_stmt(self)




    def node_stmt(self):

        localctx = zmapParser.Node_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_node_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.node_id()
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 126
                self.attr_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Node_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(zmapParser.Id_Context,0)


        def special(self):
            return self.getTypedRuleContext(zmapParser.SpecialContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_node_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode_id" ):
                listener.enterNode_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode_id" ):
                listener.exitNode_id(self)




    def node_id(self):

        localctx = zmapParser.Node_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_node_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.id_()
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 130
                self.special()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Node_id_leftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(zmapParser.Id_Context,0)


        def port_left(self):
            return self.getTypedRuleContext(zmapParser.Port_leftContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_node_id_left

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode_id_left" ):
                listener.enterNode_id_left(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode_id_left" ):
                listener.exitNode_id_left(self)




    def node_id_left(self):

        localctx = zmapParser.Node_id_leftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_node_id_left)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.id_()
            self.state = 134
            self.port_left()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Node_id_rightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(zmapParser.Id_Context,0)


        def port_right(self):
            return self.getTypedRuleContext(zmapParser.Port_rightContext,0)


        def special(self):
            return self.getTypedRuleContext(zmapParser.SpecialContext,0)


        def getRuleIndex(self):
            return zmapParser.RULE_node_id_right

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode_id_right" ):
                listener.enterNode_id_right(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode_id_right" ):
                listener.exitNode_id_right(self)




    def node_id_right(self):

        localctx = zmapParser.Node_id_rightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_node_id_right)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 136
                self.port_right()


            self.state = 139
            self.id_()
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 140
                self.special()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return zmapParser.RULE_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial" ):
                listener.enterSpecial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial" ):
                listener.exitSpecial(self)




    def special(self):

        localctx = zmapParser.SpecialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_special)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(zmapParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Port_leftContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(zmapParser.Id_Context,0)


        def getRuleIndex(self):
            return zmapParser.RULE_port_left

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort_left" ):
                listener.enterPort_left(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort_left" ):
                listener.exitPort_left(self)




    def port_left(self):

        localctx = zmapParser.Port_leftContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_port_left)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(zmapParser.T__14)
            self.state = 146
            self.id_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Port_rightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(zmapParser.Id_Context,0)


        def getRuleIndex(self):
            return zmapParser.RULE_port_right

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPort_right" ):
                listener.enterPort_right(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPort_right" ):
                listener.exitPort_right(self)




    def port_right(self):

        localctx = zmapParser.Port_rightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_port_right)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.id_()
            self.state = 149
            self.match(zmapParser.T__14)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(zmapParser.ID, 0)

        def STRING(self):
            return self.getToken(zmapParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(zmapParser.NUMBER, 0)

        def getRuleIndex(self):
            return zmapParser.RULE_id_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_" ):
                listener.enterId_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_" ):
                listener.exitId_(self)




    def id_(self):

        localctx = zmapParser.Id_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_id_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3670016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





