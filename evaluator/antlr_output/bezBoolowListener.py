# Generated from C:/Users/fudal/OneDrive/Dokumenty/GitHub/Genetyczne/evaluator\bezBoolow.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .bezBoolowParser import bezBoolowParser
else:
    from bezBoolowParser import bezBoolowParser

# This class defines a complete listener for a parse tree produced by bezBoolowParser.
class bezBoolowListener(ParseTreeListener):

    # Enter a parse tree produced by bezBoolowParser#file_.
    def enterFile_(self, ctx:bezBoolowParser.File_Context):
        pass

    # Exit a parse tree produced by bezBoolowParser#file_.
    def exitFile_(self, ctx:bezBoolowParser.File_Context):
        pass


    # Enter a parse tree produced by bezBoolowParser#blockseq.
    def enterBlockseq(self, ctx:bezBoolowParser.BlockseqContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#blockseq.
    def exitBlockseq(self, ctx:bezBoolowParser.BlockseqContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#block.
    def enterBlock(self, ctx:bezBoolowParser.BlockContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#block.
    def exitBlock(self, ctx:bezBoolowParser.BlockContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#printBlock.
    def enterPrintBlock(self, ctx:bezBoolowParser.PrintBlockContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#printBlock.
    def exitPrintBlock(self, ctx:bezBoolowParser.PrintBlockContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#inputBlock.
    def enterInputBlock(self, ctx:bezBoolowParser.InputBlockContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#inputBlock.
    def exitInputBlock(self, ctx:bezBoolowParser.InputBlockContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#variableDefinition.
    def enterVariableDefinition(self, ctx:bezBoolowParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#variableDefinition.
    def exitVariableDefinition(self, ctx:bezBoolowParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#loopBlock.
    def enterLoopBlock(self, ctx:bezBoolowParser.LoopBlockContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#loopBlock.
    def exitLoopBlock(self, ctx:bezBoolowParser.LoopBlockContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#ifBlock.
    def enterIfBlock(self, ctx:bezBoolowParser.IfBlockContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#ifBlock.
    def exitIfBlock(self, ctx:bezBoolowParser.IfBlockContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#expression.
    def enterExpression(self, ctx:bezBoolowParser.ExpressionContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#expression.
    def exitExpression(self, ctx:bezBoolowParser.ExpressionContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#equation.
    def enterEquation(self, ctx:bezBoolowParser.EquationContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#equation.
    def exitEquation(self, ctx:bezBoolowParser.EquationContext):
        pass


    # Enter a parse tree produced by bezBoolowParser#atom.
    def enterAtom(self, ctx:bezBoolowParser.AtomContext):
        pass

    # Exit a parse tree produced by bezBoolowParser#atom.
    def exitAtom(self, ctx:bezBoolowParser.AtomContext):
        pass



del bezBoolowParser