# Generated from C:/Users/fudal/OneDrive/Dokumenty/GitHub/Genetyczne/evaluator\bezBoolow.g4 by ANTLR 4.11.1
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
        4,1,30,125,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,1,1,4,1,27,8,1,11,
        1,12,1,28,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,61,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,3,8,85,8,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,5,8,96,8,8,10,8,12,8,99,9,8,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,107,8,9,1,9,3,9,110,8,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,
        118,8,9,10,9,12,9,121,9,9,1,10,1,10,1,10,0,2,16,18,11,0,2,4,6,8,
        10,12,14,16,18,20,0,6,1,0,22,23,1,0,14,15,1,0,17,18,1,0,12,13,1,
        0,10,11,1,0,1,3,127,0,22,1,0,0,0,2,26,1,0,0,0,4,35,1,0,0,0,6,37,
        1,0,0,0,8,43,1,0,0,0,10,60,1,0,0,0,12,62,1,0,0,0,14,70,1,0,0,0,16,
        84,1,0,0,0,18,109,1,0,0,0,20,122,1,0,0,0,22,23,3,2,1,0,23,24,5,0,
        0,1,24,1,1,0,0,0,25,27,3,4,2,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,
        1,0,0,0,28,29,1,0,0,0,29,3,1,0,0,0,30,36,3,10,5,0,31,36,3,14,7,0,
        32,36,3,12,6,0,33,36,3,6,3,0,34,36,3,8,4,0,35,30,1,0,0,0,35,31,1,
        0,0,0,35,32,1,0,0,0,35,33,1,0,0,0,35,34,1,0,0,0,36,5,1,0,0,0,37,
        38,5,28,0,0,38,39,5,6,0,0,39,40,3,18,9,0,40,41,5,7,0,0,41,42,5,26,
        0,0,42,7,1,0,0,0,43,44,5,3,0,0,44,45,5,16,0,0,45,46,5,29,0,0,46,
        47,5,6,0,0,47,48,5,7,0,0,48,49,5,26,0,0,49,9,1,0,0,0,50,51,5,3,0,
        0,51,52,5,16,0,0,52,53,3,18,9,0,53,54,5,26,0,0,54,61,1,0,0,0,55,
        56,5,3,0,0,56,57,5,16,0,0,57,58,3,16,8,0,58,59,5,26,0,0,59,61,1,
        0,0,0,60,50,1,0,0,0,60,55,1,0,0,0,61,11,1,0,0,0,62,63,5,25,0,0,63,
        64,5,6,0,0,64,65,3,16,8,0,65,66,5,7,0,0,66,67,5,8,0,0,67,68,3,2,
        1,0,68,69,5,9,0,0,69,13,1,0,0,0,70,71,5,21,0,0,71,72,5,6,0,0,72,
        73,3,16,8,0,73,74,5,7,0,0,74,75,5,8,0,0,75,76,3,2,1,0,76,77,5,9,
        0,0,77,15,1,0,0,0,78,79,6,8,-1,0,79,80,5,6,0,0,80,81,3,16,8,0,81,
        82,5,7,0,0,82,85,1,0,0,0,83,85,3,18,9,0,84,78,1,0,0,0,84,83,1,0,
        0,0,85,97,1,0,0,0,86,87,10,5,0,0,87,88,7,0,0,0,88,96,3,16,8,6,89,
        90,10,4,0,0,90,91,7,1,0,0,91,96,3,16,8,5,92,93,10,3,0,0,93,94,7,
        2,0,0,94,96,3,16,8,4,95,86,1,0,0,0,95,89,1,0,0,0,95,92,1,0,0,0,96,
        99,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,17,1,0,0,0,99,97,1,0,0,
        0,100,101,6,9,-1,0,101,102,5,6,0,0,102,103,3,18,9,0,103,104,5,7,
        0,0,104,110,1,0,0,0,105,107,5,11,0,0,106,105,1,0,0,0,106,107,1,0,
        0,0,107,108,1,0,0,0,108,110,3,20,10,0,109,100,1,0,0,0,109,106,1,
        0,0,0,110,119,1,0,0,0,111,112,10,4,0,0,112,113,7,3,0,0,113,118,3,
        18,9,5,114,115,10,3,0,0,115,116,7,4,0,0,116,118,3,18,9,4,117,111,
        1,0,0,0,117,114,1,0,0,0,118,121,1,0,0,0,119,117,1,0,0,0,119,120,
        1,0,0,0,120,19,1,0,0,0,121,119,1,0,0,0,122,123,7,5,0,0,123,21,1,
        0,0,0,10,28,35,60,84,95,97,106,109,117,119
    ]

class bezBoolowParser ( Parser ):

    grammarFileName = "bezBoolow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'v_'", "<INVALID>", "'('", "')'", "'{'", "'}'", "'+'", 
                     "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "'=='", "'!='", 
                     "'\"'", "'^'", "'if'", "' &'", "'|'", "<INVALID>", 
                     "'while'", "';'", "'!'", "'print'", "'input'" ]

    symbolicNames = [ "<INVALID>", "NUM", "FLOAT", "VARIABLE", "VAR_NAME", 
                      "ID_VAR", "LPAREN", "RPAREN", "LPARENCURLY", "RPARENCURLY", 
                      "PLUS", "MINUS", "TIMES", "DIV", "GT", "LT", "EQ", 
                      "EQ_LOGICAL", "NOT_EQ_LOGICAL", "QUOTATION", "POW", 
                      "IF", "AND", "OR", "WS", "WHILE", "ENDCHAR", "NOT", 
                      "PRINT", "INPUT", "FILENAME" ]

    RULE_file_ = 0
    RULE_blockseq = 1
    RULE_block = 2
    RULE_printBlock = 3
    RULE_inputBlock = 4
    RULE_variableDefinition = 5
    RULE_loopBlock = 6
    RULE_ifBlock = 7
    RULE_expression = 8
    RULE_equation = 9
    RULE_atom = 10

    ruleNames =  [ "file_", "blockseq", "block", "printBlock", "inputBlock", 
                   "variableDefinition", "loopBlock", "ifBlock", "expression", 
                   "equation", "atom" ]

    EOF = Token.EOF
    NUM=1
    FLOAT=2
    VARIABLE=3
    VAR_NAME=4
    ID_VAR=5
    LPAREN=6
    RPAREN=7
    LPARENCURLY=8
    RPARENCURLY=9
    PLUS=10
    MINUS=11
    TIMES=12
    DIV=13
    GT=14
    LT=15
    EQ=16
    EQ_LOGICAL=17
    NOT_EQ_LOGICAL=18
    QUOTATION=19
    POW=20
    IF=21
    AND=22
    OR=23
    WS=24
    WHILE=25
    ENDCHAR=26
    NOT=27
    PRINT=28
    INPUT=29
    FILENAME=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockseq(self):
            return self.getTypedRuleContext(bezBoolowParser.BlockseqContext,0)


        def EOF(self):
            return self.getToken(bezBoolowParser.EOF, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_file_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_" ):
                listener.enterFile_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_" ):
                listener.exitFile_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_" ):
                return visitor.visitFile_(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = bezBoolowParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.blockseq()
            self.state = 23
            self.match(bezBoolowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockseqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bezBoolowParser.BlockContext)
            else:
                return self.getTypedRuleContext(bezBoolowParser.BlockContext,i)


        def getRuleIndex(self):
            return bezBoolowParser.RULE_blockseq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockseq" ):
                listener.enterBlockseq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockseq" ):
                listener.exitBlockseq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockseq" ):
                return visitor.visitBlockseq(self)
            else:
                return visitor.visitChildren(self)




    def blockseq(self):

        localctx = bezBoolowParser.BlockseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_blockseq)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.block()
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 304087048) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(bezBoolowParser.VariableDefinitionContext,0)


        def ifBlock(self):
            return self.getTypedRuleContext(bezBoolowParser.IfBlockContext,0)


        def loopBlock(self):
            return self.getTypedRuleContext(bezBoolowParser.LoopBlockContext,0)


        def printBlock(self):
            return self.getTypedRuleContext(bezBoolowParser.PrintBlockContext,0)


        def inputBlock(self):
            return self.getTypedRuleContext(bezBoolowParser.InputBlockContext,0)


        def getRuleIndex(self):
            return bezBoolowParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = bezBoolowParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.variableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.ifBlock()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.loopBlock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.printBlock()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.inputBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(bezBoolowParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(bezBoolowParser.LPAREN, 0)

        def equation(self):
            return self.getTypedRuleContext(bezBoolowParser.EquationContext,0)


        def RPAREN(self):
            return self.getToken(bezBoolowParser.RPAREN, 0)

        def ENDCHAR(self):
            return self.getToken(bezBoolowParser.ENDCHAR, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_printBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintBlock" ):
                listener.enterPrintBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintBlock" ):
                listener.exitPrintBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintBlock" ):
                return visitor.visitPrintBlock(self)
            else:
                return visitor.visitChildren(self)




    def printBlock(self):

        localctx = bezBoolowParser.PrintBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(bezBoolowParser.PRINT)
            self.state = 38
            self.match(bezBoolowParser.LPAREN)
            self.state = 39
            self.equation(0)
            self.state = 40
            self.match(bezBoolowParser.RPAREN)
            self.state = 41
            self.match(bezBoolowParser.ENDCHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(bezBoolowParser.VARIABLE, 0)

        def EQ(self):
            return self.getToken(bezBoolowParser.EQ, 0)

        def INPUT(self):
            return self.getToken(bezBoolowParser.INPUT, 0)

        def LPAREN(self):
            return self.getToken(bezBoolowParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(bezBoolowParser.RPAREN, 0)

        def ENDCHAR(self):
            return self.getToken(bezBoolowParser.ENDCHAR, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_inputBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputBlock" ):
                listener.enterInputBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputBlock" ):
                listener.exitInputBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputBlock" ):
                return visitor.visitInputBlock(self)
            else:
                return visitor.visitChildren(self)




    def inputBlock(self):

        localctx = bezBoolowParser.InputBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_inputBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(bezBoolowParser.VARIABLE)
            self.state = 44
            self.match(bezBoolowParser.EQ)
            self.state = 45
            self.match(bezBoolowParser.INPUT)
            self.state = 46
            self.match(bezBoolowParser.LPAREN)
            self.state = 47
            self.match(bezBoolowParser.RPAREN)
            self.state = 48
            self.match(bezBoolowParser.ENDCHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(bezBoolowParser.VARIABLE, 0)

        def EQ(self):
            return self.getToken(bezBoolowParser.EQ, 0)

        def equation(self):
            return self.getTypedRuleContext(bezBoolowParser.EquationContext,0)


        def ENDCHAR(self):
            return self.getToken(bezBoolowParser.ENDCHAR, 0)

        def expression(self):
            return self.getTypedRuleContext(bezBoolowParser.ExpressionContext,0)


        def getRuleIndex(self):
            return bezBoolowParser.RULE_variableDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDefinition" ):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDefinition" ):
                listener.exitVariableDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDefinition" ):
                return visitor.visitVariableDefinition(self)
            else:
                return visitor.visitChildren(self)




    def variableDefinition(self):

        localctx = bezBoolowParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDefinition)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(bezBoolowParser.VARIABLE)
                self.state = 51
                self.match(bezBoolowParser.EQ)
                self.state = 52
                self.equation(0)
                self.state = 53
                self.match(bezBoolowParser.ENDCHAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(bezBoolowParser.VARIABLE)
                self.state = 56
                self.match(bezBoolowParser.EQ)
                self.state = 57
                self.expression(0)
                self.state = 58
                self.match(bezBoolowParser.ENDCHAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoopBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(bezBoolowParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(bezBoolowParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(bezBoolowParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(bezBoolowParser.RPAREN, 0)

        def LPARENCURLY(self):
            return self.getToken(bezBoolowParser.LPARENCURLY, 0)

        def blockseq(self):
            return self.getTypedRuleContext(bezBoolowParser.BlockseqContext,0)


        def RPARENCURLY(self):
            return self.getToken(bezBoolowParser.RPARENCURLY, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_loopBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopBlock" ):
                listener.enterLoopBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopBlock" ):
                listener.exitLoopBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopBlock" ):
                return visitor.visitLoopBlock(self)
            else:
                return visitor.visitChildren(self)




    def loopBlock(self):

        localctx = bezBoolowParser.LoopBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_loopBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(bezBoolowParser.WHILE)
            self.state = 63
            self.match(bezBoolowParser.LPAREN)
            self.state = 64
            self.expression(0)
            self.state = 65
            self.match(bezBoolowParser.RPAREN)
            self.state = 66
            self.match(bezBoolowParser.LPARENCURLY)
            self.state = 67
            self.blockseq()
            self.state = 68
            self.match(bezBoolowParser.RPARENCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(bezBoolowParser.IF, 0)

        def LPAREN(self):
            return self.getToken(bezBoolowParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(bezBoolowParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(bezBoolowParser.RPAREN, 0)

        def LPARENCURLY(self):
            return self.getToken(bezBoolowParser.LPARENCURLY, 0)

        def blockseq(self):
            return self.getTypedRuleContext(bezBoolowParser.BlockseqContext,0)


        def RPARENCURLY(self):
            return self.getToken(bezBoolowParser.RPARENCURLY, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = bezBoolowParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(bezBoolowParser.IF)
            self.state = 71
            self.match(bezBoolowParser.LPAREN)
            self.state = 72
            self.expression(0)
            self.state = 73
            self.match(bezBoolowParser.RPAREN)
            self.state = 74
            self.match(bezBoolowParser.LPARENCURLY)
            self.state = 75
            self.blockseq()
            self.state = 76
            self.match(bezBoolowParser.RPARENCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(bezBoolowParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bezBoolowParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(bezBoolowParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(bezBoolowParser.RPAREN, 0)

        def equation(self):
            return self.getTypedRuleContext(bezBoolowParser.EquationContext,0)


        def OR(self):
            return self.getToken(bezBoolowParser.OR, 0)

        def AND(self):
            return self.getToken(bezBoolowParser.AND, 0)

        def GT(self):
            return self.getToken(bezBoolowParser.GT, 0)

        def LT(self):
            return self.getToken(bezBoolowParser.LT, 0)

        def EQ_LOGICAL(self):
            return self.getToken(bezBoolowParser.EQ_LOGICAL, 0)

        def NOT_EQ_LOGICAL(self):
            return self.getToken(bezBoolowParser.NOT_EQ_LOGICAL, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = bezBoolowParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(bezBoolowParser.LPAREN)
                self.state = 80
                self.expression(0)
                self.state = 81
                self.match(bezBoolowParser.RPAREN)
                pass

            elif la_ == 2:
                self.state = 83
                self.equation(0)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 97
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 95
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = bezBoolowParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 87
                        _la = self._input.LA(1)
                        if not(_la==22 or _la==23):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = bezBoolowParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 89
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 90
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 91
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = bezBoolowParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 93
                        _la = self._input.LA(1)
                        if not(_la==17 or _la==18):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 94
                        self.expression(4)
                        pass

             
                self.state = 99
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(bezBoolowParser.LPAREN, 0)

        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(bezBoolowParser.EquationContext)
            else:
                return self.getTypedRuleContext(bezBoolowParser.EquationContext,i)


        def RPAREN(self):
            return self.getToken(bezBoolowParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(bezBoolowParser.AtomContext,0)


        def MINUS(self):
            return self.getToken(bezBoolowParser.MINUS, 0)

        def TIMES(self):
            return self.getToken(bezBoolowParser.TIMES, 0)

        def DIV(self):
            return self.getToken(bezBoolowParser.DIV, 0)

        def PLUS(self):
            return self.getToken(bezBoolowParser.PLUS, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquation" ):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)



    def equation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = bezBoolowParser.EquationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_equation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 101
                self.match(bezBoolowParser.LPAREN)
                self.state = 102
                self.equation(0)
                self.state = 103
                self.match(bezBoolowParser.RPAREN)
                pass
            elif token in [1, 2, 3, 11]:
                self.state = 106
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==11:
                    self.state = 105
                    self.match(bezBoolowParser.MINUS)


                self.state = 108
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 119
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 117
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = bezBoolowParser.EquationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equation)
                        self.state = 111
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 112
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 113
                        self.equation(5)
                        pass

                    elif la_ == 2:
                        localctx = bezBoolowParser.EquationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_equation)
                        self.state = 114
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 115
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 116
                        self.equation(4)
                        pass

             
                self.state = 121
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(bezBoolowParser.NUM, 0)

        def FLOAT(self):
            return self.getToken(bezBoolowParser.FLOAT, 0)

        def VARIABLE(self):
            return self.getToken(bezBoolowParser.VARIABLE, 0)

        def getRuleIndex(self):
            return bezBoolowParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = bezBoolowParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expression_sempred
        self._predicates[9] = self.equation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

    def equation_sempred(self, localctx:EquationContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




