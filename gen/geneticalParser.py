# Generated from C:/Users/fudal/OneDrive/Desktop/AGH/ISI/Semestr 4/pythonProject\genetical.g4 by ANTLR 4.10.1
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
        4, 1, 27, 164, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        1, 0, 3, 0, 30, 8, 0, 1, 0, 1, 0, 1, 1, 4, 1, 35, 8, 1, 11, 1, 12, 1, 36, 1, 2, 1, 2, 1, 2, 1,
        2, 3, 2, 43, 8, 2, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 55, 8, 3,
        1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5,
        1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 1, 6, 3, 6, 83, 8, 6, 1, 7, 1, 7, 1, 7, 1,
        7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 5, 7, 99, 8, 7, 10, 7, 12, 7, 102,
        9, 7, 1, 7, 3, 7, 105, 8, 7, 1, 7, 1, 7, 1, 7, 1, 7, 5, 7, 111, 8, 7, 10, 7, 12, 7, 114, 9,
        7, 1, 8, 1, 8, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 1, 9, 3, 9, 126, 8, 9, 1, 10, 1, 10,
        1, 10, 1, 10, 1, 10, 1, 10, 5, 10, 134, 8, 10, 10, 10, 12, 10, 137, 9, 10, 1, 10, 3, 10,
        140, 8, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 5, 10, 151, 8,
        10, 10, 10, 12, 10, 154, 9, 10, 1, 11, 1, 11, 3, 11, 158, 8, 11, 1, 12, 1, 12, 1, 13, 1,
        13, 1, 13, 0, 2, 14, 20, 14, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 0, 4, 1,
        0, 12, 13, 3, 0, 16, 17, 19, 19, 23, 24, 1, 0, 14, 15, 1, 0, 16, 18, 168, 0, 29, 1, 0, 0,
        0, 2, 34, 1, 0, 0, 0, 4, 42, 1, 0, 0, 0, 6, 54, 1, 0, 0, 0, 8, 56, 1, 0, 0, 0, 10, 64, 1, 0,
        0, 0, 12, 82, 1, 0, 0, 0, 14, 104, 1, 0, 0, 0, 16, 115, 1, 0, 0, 0, 18, 125, 1, 0, 0, 0, 20,
        139, 1, 0, 0, 0, 22, 157, 1, 0, 0, 0, 24, 159, 1, 0, 0, 0, 26, 161, 1, 0, 0, 0, 28, 30, 3,
        2, 1, 0, 29, 28, 1, 0, 0, 0, 29, 30, 1, 0, 0, 0, 30, 31, 1, 0, 0, 0, 31, 32, 5, 0, 0, 1, 32,
        1, 1, 0, 0, 0, 33, 35, 3, 4, 2, 0, 34, 33, 1, 0, 0, 0, 35, 36, 1, 0, 0, 0, 36, 34, 1, 0, 0,
        0, 36, 37, 1, 0, 0, 0, 37, 3, 1, 0, 0, 0, 38, 43, 3, 12, 6, 0, 39, 43, 3, 6, 3, 0, 40, 43,
        3, 10, 5, 0, 41, 43, 3, 8, 4, 0, 42, 38, 1, 0, 0, 0, 42, 39, 1, 0, 0, 0, 42, 40, 1, 0, 0, 0,
        42, 41, 1, 0, 0, 0, 43, 5, 1, 0, 0, 0, 44, 45, 5, 2, 0, 0, 45, 46, 5, 18, 0, 0, 46, 47, 3,
        20, 10, 0, 47, 48, 5, 27, 0, 0, 48, 55, 1, 0, 0, 0, 49, 50, 5, 2, 0, 0, 50, 51, 5, 18, 0,
        0, 51, 52, 3, 14, 7, 0, 52, 53, 5, 27, 0, 0, 53, 55, 1, 0, 0, 0, 54, 44, 1, 0, 0, 0, 54, 49,
        1, 0, 0, 0, 55, 7, 1, 0, 0, 0, 56, 57, 5, 26, 0, 0, 57, 58, 5, 8, 0, 0, 58, 59, 3, 14, 7, 0,
        59, 60, 5, 9, 0, 0, 60, 61, 5, 10, 0, 0, 61, 62, 3, 2, 1, 0, 62, 63, 5, 11, 0, 0, 63, 9, 1,
        0, 0, 0, 64, 65, 5, 22, 0, 0, 65, 66, 5, 8, 0, 0, 66, 67, 3, 14, 7, 0, 67, 68, 5, 9, 0, 0,
        68, 69, 5, 10, 0, 0, 69, 70, 3, 2, 1, 0, 70, 71, 5, 11, 0, 0, 71, 11, 1, 0, 0, 0, 72, 73,
        3, 24, 12, 0, 73, 74, 5, 18, 0, 0, 74, 75, 5, 1, 0, 0, 75, 76, 5, 27, 0, 0, 76, 83, 1, 0,
        0, 0, 77, 78, 3, 24, 12, 0, 78, 79, 5, 18, 0, 0, 79, 80, 3, 18, 9, 0, 80, 81, 5, 27, 0, 0,
        81, 83, 1, 0, 0, 0, 82, 72, 1, 0, 0, 0, 82, 77, 1, 0, 0, 0, 83, 13, 1, 0, 0, 0, 84, 85, 6,
        7, -1, 0, 85, 86, 3, 20, 10, 0, 86, 87, 3, 16, 8, 0, 87, 88, 3, 14, 7, 4, 88, 105, 1, 0,
        0, 0, 89, 90, 3, 20, 10, 0, 90, 91, 3, 16, 8, 0, 91, 92, 3, 20, 10, 0, 92, 105, 1, 0, 0,
        0, 93, 94, 5, 8, 0, 0, 94, 95, 3, 20, 10, 0, 95, 96, 5, 9, 0, 0, 96, 105, 1, 0, 0, 0, 97,
        99, 7, 0, 0, 0, 98, 97, 1, 0, 0, 0, 99, 102, 1, 0, 0, 0, 100, 98, 1, 0, 0, 0, 100, 101, 1,
        0, 0, 0, 101, 103, 1, 0, 0, 0, 102, 100, 1, 0, 0, 0, 103, 105, 3, 22, 11, 0, 104, 84, 1,
        0, 0, 0, 104, 89, 1, 0, 0, 0, 104, 93, 1, 0, 0, 0, 104, 100, 1, 0, 0, 0, 105, 112, 1, 0,
        0, 0, 106, 107, 10, 5, 0, 0, 107, 108, 3, 16, 8, 0, 108, 109, 3, 14, 7, 6, 109, 111, 1,
        0, 0, 0, 110, 106, 1, 0, 0, 0, 111, 114, 1, 0, 0, 0, 112, 110, 1, 0, 0, 0, 112, 113, 1,
        0, 0, 0, 113, 15, 1, 0, 0, 0, 114, 112, 1, 0, 0, 0, 115, 116, 7, 1, 0, 0, 116, 17, 1, 0,
        0, 0, 117, 118, 3, 20, 10, 0, 118, 119, 3, 26, 13, 0, 119, 120, 3, 20, 10, 0, 120, 126,
        1, 0, 0, 0, 121, 122, 3, 20, 10, 0, 122, 123, 3, 16, 8, 0, 123, 124, 3, 20, 10, 0, 124,
        126, 1, 0, 0, 0, 125, 117, 1, 0, 0, 0, 125, 121, 1, 0, 0, 0, 126, 19, 1, 0, 0, 0, 127, 128,
        6, 10, -1, 0, 128, 129, 5, 8, 0, 0, 129, 130, 3, 20, 10, 0, 130, 131, 5, 9, 0, 0, 131,
        140, 1, 0, 0, 0, 132, 134, 7, 0, 0, 0, 133, 132, 1, 0, 0, 0, 134, 137, 1, 0, 0, 0, 135,
        133, 1, 0, 0, 0, 135, 136, 1, 0, 0, 0, 136, 138, 1, 0, 0, 0, 137, 135, 1, 0, 0, 0, 138,
        140, 3, 22, 11, 0, 139, 127, 1, 0, 0, 0, 139, 135, 1, 0, 0, 0, 140, 152, 1, 0, 0, 0, 141,
        142, 10, 5, 0, 0, 142, 143, 5, 21, 0, 0, 143, 151, 3, 20, 10, 6, 144, 145, 10, 4, 0, 0,
        145, 146, 7, 2, 0, 0, 146, 151, 3, 20, 10, 5, 147, 148, 10, 3, 0, 0, 148, 149, 7, 0, 0,
        0, 149, 151, 3, 20, 10, 4, 150, 141, 1, 0, 0, 0, 150, 144, 1, 0, 0, 0, 150, 147, 1, 0,
        0, 0, 151, 154, 1, 0, 0, 0, 152, 150, 1, 0, 0, 0, 152, 153, 1, 0, 0, 0, 153, 21, 1, 0, 0,
        0, 154, 152, 1, 0, 0, 0, 155, 158, 5, 1, 0, 0, 156, 158, 3, 24, 12, 0, 157, 155, 1, 0,
        0, 0, 157, 156, 1, 0, 0, 0, 158, 23, 1, 0, 0, 0, 159, 160, 5, 2, 0, 0, 160, 25, 1, 0, 0,
        0, 161, 162, 7, 3, 0, 0, 162, 27, 1, 0, 0, 0, 14, 29, 36, 42, 54, 82, 100, 104, 112, 125,
        135, 139, 150, 152, 157
    ]


class geneticalParser(Parser):
    grammarFileName = "genetical.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "'n_'", "'b_'", "<INVALID>", "'('", "')'",
                    "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'",
                    "'='", "'=='", "'.'", "'^'", "'if'", "' &'", "'|'",
                    "<INVALID>", "'while'", "';'"]

    symbolicNames = ["<INVALID>", "NUMBER", "VARIABLE", "BOOL_VARIABLE",
                     "NUM_VARIABLE", "NUM_NAME", "BOOL_NAME", "ID_NUM",
                     "LPAREN", "RPAREN", "LPARENCURLY", "RPARENCURLY",
                     "PLUS", "MINUS", "TIMES", "DIV", "GT", "LT", "EQ",
                     "EQ_LOGICAL", "POINT", "POW", "IF", "AND", "OR", "WS",
                     "WHILE", "ENDCHAR"]

    RULE_file_ = 0
    RULE_blockseq = 1
    RULE_block = 2
    RULE_variableOperation = 3
    RULE_loopBlock = 4
    RULE_ifBlock = 5
    RULE_variableDefinition = 6
    RULE_logicalExp = 7
    RULE_relopLogical = 8
    RULE_equation = 9
    RULE_expression = 10
    RULE_atom = 11
    RULE_variable = 12
    RULE_relop = 13

    ruleNames = ["file_", "blockseq", "block", "variableOperation", "loopBlock",
                 "ifBlock", "variableDefinition", "logicalExp", "relopLogical",
                 "equation", "expression", "atom", "variable", "relop"]

    EOF = Token.EOF
    NUMBER = 1
    VARIABLE = 2
    BOOL_VARIABLE = 3
    NUM_VARIABLE = 4
    NUM_NAME = 5
    BOOL_NAME = 6
    ID_NUM = 7
    LPAREN = 8
    RPAREN = 9
    LPARENCURLY = 10
    RPARENCURLY = 11
    PLUS = 12
    MINUS = 13
    TIMES = 14
    DIV = 15
    GT = 16
    LT = 17
    EQ = 18
    EQ_LOGICAL = 19
    POINT = 20
    POW = 21
    IF = 22
    AND = 23
    OR = 24
    WS = 25
    WHILE = 26
    ENDCHAR = 27

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class File_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(geneticalParser.EOF, 0)

        def blockseq(self):
            return self.getTypedRuleContext(geneticalParser.BlockseqContext, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_file_

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFile_"):
                listener.enterFile_(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFile_"):
                listener.exitFile_(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitFile_"):
                return visitor.visitFile_(self)
            else:
                return visitor.visitChildren(self)

    def file_(self):

        localctx = geneticalParser.File_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << geneticalParser.VARIABLE) | (1 << geneticalParser.IF) | (1 << geneticalParser.WHILE))) != 0):
                self.state = 28
                self.blockseq()

            self.state = 31
            self.match(geneticalParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockseqContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(geneticalParser.BlockContext)
            else:
                return self.getTypedRuleContext(geneticalParser.BlockContext, i)

        def getRuleIndex(self):
            return geneticalParser.RULE_blockseq

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBlockseq"):
                listener.enterBlockseq(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBlockseq"):
                listener.exitBlockseq(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBlockseq"):
                return visitor.visitBlockseq(self)
            else:
                return visitor.visitChildren(self)

    def blockseq(self):

        localctx = geneticalParser.BlockseqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_blockseq)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 33
                self.block()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                        (1 << geneticalParser.VARIABLE) | (1 << geneticalParser.IF) | (
                        1 << geneticalParser.WHILE))) != 0)):
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDefinition(self):
            return self.getTypedRuleContext(geneticalParser.VariableDefinitionContext, 0)

        def variableOperation(self):
            return self.getTypedRuleContext(geneticalParser.VariableOperationContext, 0)

        def ifBlock(self):
            return self.getTypedRuleContext(geneticalParser.IfBlockContext, 0)

        def loopBlock(self):
            return self.getTypedRuleContext(geneticalParser.LoopBlockContext, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_block

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBlock"):
                listener.enterBlock(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBlock"):
                listener.exitBlock(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBlock"):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)

    def block(self):

        localctx = geneticalParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.variableDefinition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.variableOperation()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.ifBlock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.loopBlock()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(geneticalParser.VARIABLE, 0)

        def EQ(self):
            return self.getToken(geneticalParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(geneticalParser.ExpressionContext, 0)

        def ENDCHAR(self):
            return self.getToken(geneticalParser.ENDCHAR, 0)

        def logicalExp(self):
            return self.getTypedRuleContext(geneticalParser.LogicalExpContext, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_variableOperation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariableOperation"):
                listener.enterVariableOperation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariableOperation"):
                listener.exitVariableOperation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVariableOperation"):
                return visitor.visitVariableOperation(self)
            else:
                return visitor.visitChildren(self)

    def variableOperation(self):

        localctx = geneticalParser.VariableOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableOperation)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(geneticalParser.VARIABLE)
                self.state = 45
                self.match(geneticalParser.EQ)
                self.state = 46
                self.expression(0)
                self.state = 47
                self.match(geneticalParser.ENDCHAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(geneticalParser.VARIABLE)
                self.state = 50
                self.match(geneticalParser.EQ)
                self.state = 51
                self.logicalExp(0)
                self.state = 52
                self.match(geneticalParser.ENDCHAR)
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

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(geneticalParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(geneticalParser.LPAREN, 0)

        def logicalExp(self):
            return self.getTypedRuleContext(geneticalParser.LogicalExpContext, 0)

        def RPAREN(self):
            return self.getToken(geneticalParser.RPAREN, 0)

        def LPARENCURLY(self):
            return self.getToken(geneticalParser.LPARENCURLY, 0)

        def blockseq(self):
            return self.getTypedRuleContext(geneticalParser.BlockseqContext, 0)

        def RPARENCURLY(self):
            return self.getToken(geneticalParser.RPARENCURLY, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_loopBlock

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLoopBlock"):
                listener.enterLoopBlock(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLoopBlock"):
                listener.exitLoopBlock(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLoopBlock"):
                return visitor.visitLoopBlock(self)
            else:
                return visitor.visitChildren(self)

    def loopBlock(self):

        localctx = geneticalParser.LoopBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_loopBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(geneticalParser.WHILE)
            self.state = 57
            self.match(geneticalParser.LPAREN)
            self.state = 58
            self.logicalExp(0)
            self.state = 59
            self.match(geneticalParser.RPAREN)
            self.state = 60
            self.match(geneticalParser.LPARENCURLY)
            self.state = 61
            self.blockseq()
            self.state = 62
            self.match(geneticalParser.RPARENCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(geneticalParser.IF, 0)

        def LPAREN(self):
            return self.getToken(geneticalParser.LPAREN, 0)

        def logicalExp(self):
            return self.getTypedRuleContext(geneticalParser.LogicalExpContext, 0)

        def RPAREN(self):
            return self.getToken(geneticalParser.RPAREN, 0)

        def LPARENCURLY(self):
            return self.getToken(geneticalParser.LPARENCURLY, 0)

        def blockseq(self):
            return self.getTypedRuleContext(geneticalParser.BlockseqContext, 0)

        def RPARENCURLY(self):
            return self.getToken(geneticalParser.RPARENCURLY, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_ifBlock

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIfBlock"):
                listener.enterIfBlock(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIfBlock"):
                listener.exitIfBlock(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIfBlock"):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)

    def ifBlock(self):

        localctx = geneticalParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(geneticalParser.IF)
            self.state = 65
            self.match(geneticalParser.LPAREN)
            self.state = 66
            self.logicalExp(0)
            self.state = 67
            self.match(geneticalParser.RPAREN)
            self.state = 68
            self.match(geneticalParser.LPARENCURLY)
            self.state = 69
            self.blockseq()
            self.state = 70
            self.match(geneticalParser.RPARENCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(geneticalParser.VariableContext, 0)

        def EQ(self):
            return self.getToken(geneticalParser.EQ, 0)

        def NUMBER(self):
            return self.getToken(geneticalParser.NUMBER, 0)

        def ENDCHAR(self):
            return self.getToken(geneticalParser.ENDCHAR, 0)

        def equation(self):
            return self.getTypedRuleContext(geneticalParser.EquationContext, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_variableDefinition

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariableDefinition"):
                listener.enterVariableDefinition(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariableDefinition"):
                listener.exitVariableDefinition(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVariableDefinition"):
                return visitor.visitVariableDefinition(self)
            else:
                return visitor.visitChildren(self)

    def variableDefinition(self):

        localctx = geneticalParser.VariableDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDefinition)
        try:
            self.state = 82
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.variable()
                self.state = 73
                self.match(geneticalParser.EQ)
                self.state = 74
                self.match(geneticalParser.NUMBER)
                self.state = 75
                self.match(geneticalParser.ENDCHAR)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.variable()
                self.state = 78
                self.match(geneticalParser.EQ)
                self.state = 79
                self.equation()
                self.state = 80
                self.match(geneticalParser.ENDCHAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LogicalExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(geneticalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(geneticalParser.ExpressionContext, i)

        def relopLogical(self):
            return self.getTypedRuleContext(geneticalParser.RelopLogicalContext, 0)

        def logicalExp(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(geneticalParser.LogicalExpContext)
            else:
                return self.getTypedRuleContext(geneticalParser.LogicalExpContext, i)

        def LPAREN(self):
            return self.getToken(geneticalParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(geneticalParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(geneticalParser.AtomContext, 0)

        def PLUS(self, i: int = None):
            if i is None:
                return self.getTokens(geneticalParser.PLUS)
            else:
                return self.getToken(geneticalParser.PLUS, i)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(geneticalParser.MINUS)
            else:
                return self.getToken(geneticalParser.MINUS, i)

        def getRuleIndex(self):
            return geneticalParser.RULE_logicalExp

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLogicalExp"):
                listener.enterLogicalExp(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLogicalExp"):
                listener.exitLogicalExp(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLogicalExp"):
                return visitor.visitLogicalExp(self)
            else:
                return visitor.visitChildren(self)

    def logicalExp(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = geneticalParser.LogicalExpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_logicalExp, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 6, self._ctx)
            if la_ == 1:
                self.state = 85
                self.expression(0)
                self.state = 86
                self.relopLogical()
                self.state = 87
                self.logicalExp(4)
                pass

            elif la_ == 2:
                self.state = 89
                self.expression(0)
                self.state = 90
                self.relopLogical()
                self.state = 91
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 93
                self.match(geneticalParser.LPAREN)
                self.state = 94
                self.expression(0)
                self.state = 95
                self.match(geneticalParser.RPAREN)
                pass

            elif la_ == 4:
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == geneticalParser.PLUS or _la == geneticalParser.MINUS:
                    self.state = 97
                    _la = self._input.LA(1)
                    if not (_la == geneticalParser.PLUS or _la == geneticalParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 103
                self.atom()
                pass

            self._ctx.stop = self._input.LT(-1)
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = geneticalParser.LogicalExpContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalExp)
                    self.state = 106
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 107
                    self.relopLogical()
                    self.state = 108
                    self.logicalExp(6)
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class RelopLogicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ_LOGICAL(self):
            return self.getToken(geneticalParser.EQ_LOGICAL, 0)

        def GT(self):
            return self.getToken(geneticalParser.GT, 0)

        def LT(self):
            return self.getToken(geneticalParser.LT, 0)

        def AND(self):
            return self.getToken(geneticalParser.AND, 0)

        def OR(self):
            return self.getToken(geneticalParser.OR, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_relopLogical

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRelopLogical"):
                listener.enterRelopLogical(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRelopLogical"):
                listener.exitRelopLogical(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRelopLogical"):
                return visitor.visitRelopLogical(self)
            else:
                return visitor.visitChildren(self)

    def relopLogical(self):

        localctx = geneticalParser.RelopLogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_relopLogical)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << geneticalParser.GT) | (1 << geneticalParser.LT) | (1 << geneticalParser.EQ_LOGICAL) | (
                    1 << geneticalParser.AND) | (1 << geneticalParser.OR))) != 0)):
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

    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(geneticalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(geneticalParser.ExpressionContext, i)

        def relop(self):
            return self.getTypedRuleContext(geneticalParser.RelopContext, 0)

        def relopLogical(self):
            return self.getTypedRuleContext(geneticalParser.RelopLogicalContext, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_equation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEquation"):
                listener.enterEquation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEquation"):
                listener.exitEquation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEquation"):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)

    def equation(self):

        localctx = geneticalParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_equation)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.expression(0)
                self.state = 118
                self.relop()
                self.state = 119
                self.expression(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.expression(0)
                self.state = 122
                self.relopLogical()
                self.state = 123
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(geneticalParser.LPAREN, 0)

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(geneticalParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(geneticalParser.ExpressionContext, i)

        def RPAREN(self):
            return self.getToken(geneticalParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(geneticalParser.AtomContext, 0)

        def PLUS(self, i: int = None):
            if i is None:
                return self.getTokens(geneticalParser.PLUS)
            else:
                return self.getToken(geneticalParser.PLUS, i)

        def MINUS(self, i: int = None):
            if i is None:
                return self.getTokens(geneticalParser.MINUS)
            else:
                return self.getToken(geneticalParser.MINUS, i)

        def POW(self):
            return self.getToken(geneticalParser.POW, 0)

        def TIMES(self):
            return self.getToken(geneticalParser.TIMES, 0)

        def DIV(self):
            return self.getToken(geneticalParser.DIV, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpression"):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)

    def expression(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = geneticalParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [geneticalParser.LPAREN]:
                self.state = 128
                self.match(geneticalParser.LPAREN)
                self.state = 129
                self.expression(0)
                self.state = 130
                self.match(geneticalParser.RPAREN)
                pass
            elif token in [geneticalParser.NUMBER, geneticalParser.VARIABLE, geneticalParser.PLUS,
                           geneticalParser.MINUS]:
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == geneticalParser.PLUS or _la == geneticalParser.MINUS:
                    self.state = 132
                    _la = self._input.LA(1)
                    if not (_la == geneticalParser.PLUS or _la == geneticalParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 138
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 12, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 150
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 11, self._ctx)
                    if la_ == 1:
                        localctx = geneticalParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 141
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 142
                        self.match(geneticalParser.POW)
                        self.state = 143
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = geneticalParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 144
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 145
                        _la = self._input.LA(1)
                        if not (_la == geneticalParser.TIMES or _la == geneticalParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 146
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = geneticalParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 147
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 148
                        _la = self._input.LA(1)
                        if not (_la == geneticalParser.PLUS or _la == geneticalParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 149
                        self.expression(4)
                        pass

                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 12, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(geneticalParser.NUMBER, 0)

        def variable(self):
            return self.getTypedRuleContext(geneticalParser.VariableContext, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_atom

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAtom"):
                listener.enterAtom(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAtom"):
                listener.exitAtom(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAtom"):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)

    def atom(self):

        localctx = geneticalParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atom)
        try:
            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [geneticalParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.match(geneticalParser.NUMBER)
                pass
            elif token in [geneticalParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.variable()
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

    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(geneticalParser.VARIABLE, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_variable

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariable"):
                listener.enterVariable(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariable"):
                listener.exitVariable(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVariable"):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)

    def variable(self):

        localctx = geneticalParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(geneticalParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RelopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(geneticalParser.EQ, 0)

        def GT(self):
            return self.getToken(geneticalParser.GT, 0)

        def LT(self):
            return self.getToken(geneticalParser.LT, 0)

        def getRuleIndex(self):
            return geneticalParser.RULE_relop

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRelop"):
                listener.enterRelop(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRelop"):
                listener.exitRelop(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRelop"):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)

    def relop(self):

        localctx = geneticalParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_relop)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & (
                    (1 << geneticalParser.GT) | (1 << geneticalParser.LT) | (1 << geneticalParser.EQ))) != 0)):
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

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.logicalExp_sempred
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def logicalExp_sempred(self, localctx: LogicalExpContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 5)

    def expression_sempred(self, localctx: ExpressionContext, predIndex: int):
        if predIndex == 1:
            return self.precpred(self._ctx, 5)

        if predIndex == 2:
            return self.precpred(self._ctx, 4)

        if predIndex == 3:
            return self.precpred(self._ctx, 3)
