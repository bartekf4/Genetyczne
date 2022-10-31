# Generated from C:/Users/fudal/OneDrive/Desktop/AGH/ISI/Semestr 4/pythonProject\genetical.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .geneticalParser import geneticalParser
else:
    from geneticalParser import geneticalParser

# This class defines a complete listener for a parse tree produced by geneticalParser.
class geneticalListener(ParseTreeListener):

    # Enter a parse tree produced by geneticalParser#file_.
    def enterFile_(self, ctx:geneticalParser.File_Context):
        print("start")
        pass

    # Exit a parse tree produced by geneticalParser#file_.
    def exitFile_(self, ctx:geneticalParser.File_Context):
        pass


    # Enter a parse tree produced by geneticalParser#blockseq.
    def enterBlockseq(self, ctx:geneticalParser.BlockseqContext):
        pass

    # Exit a parse tree produced by geneticalParser#blockseq.
    def exitBlockseq(self, ctx:geneticalParser.BlockseqContext):
        pass


    # Enter a parse tree produced by geneticalParser#block.
    def enterBlock(self, ctx:geneticalParser.BlockContext):
        pass

    # Exit a parse tree produced by geneticalParser#block.
    def exitBlock(self, ctx:geneticalParser.BlockContext):
        pass


    # Enter a parse tree produced by geneticalParser#variableOperation.
    def enterVariableOperation(self, ctx:geneticalParser.VariableOperationContext):
        pass

    # Exit a parse tree produced by geneticalParser#variableOperation.
    def exitVariableOperation(self, ctx:geneticalParser.VariableOperationContext):
        pass


    # Enter a parse tree produced by geneticalParser#loopBlock.
    def enterLoopBlock(self, ctx:geneticalParser.LoopBlockContext):
        pass

    # Exit a parse tree produced by geneticalParser#loopBlock.
    def exitLoopBlock(self, ctx:geneticalParser.LoopBlockContext):
        pass


    # Enter a parse tree produced by geneticalParser#ifBlock.
    def enterIfBlock(self, ctx:geneticalParser.IfBlockContext):
        pass

    # Exit a parse tree produced by geneticalParser#ifBlock.
    def exitIfBlock(self, ctx:geneticalParser.IfBlockContext):
        pass


    # Enter a parse tree produced by geneticalParser#variableDefinition.
    def enterVariableDefinition(self, ctx:geneticalParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by geneticalParser#variableDefinition.
    def exitVariableDefinition(self, ctx:geneticalParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by geneticalParser#logicalExp.
    def enterLogicalExp(self, ctx:geneticalParser.LogicalExpContext):
        pass

    # Exit a parse tree produced by geneticalParser#logicalExp.
    def exitLogicalExp(self, ctx:geneticalParser.LogicalExpContext):
        pass


    # Enter a parse tree produced by geneticalParser#relopLogical.
    def enterRelopLogical(self, ctx:geneticalParser.RelopLogicalContext):
        pass

    # Exit a parse tree produced by geneticalParser#relopLogical.
    def exitRelopLogical(self, ctx:geneticalParser.RelopLogicalContext):
        pass


    # Enter a parse tree produced by geneticalParser#equation.
    def enterEquation(self, ctx:geneticalParser.EquationContext):
        pass

    # Exit a parse tree produced by geneticalParser#equation.
    def exitEquation(self, ctx:geneticalParser.EquationContext):
        pass


    # Enter a parse tree produced by geneticalParser#expression.
    def enterExpression(self, ctx:geneticalParser.ExpressionContext):
        pass

    # Exit a parse tree produced by geneticalParser#expression.
    def exitExpression(self, ctx:geneticalParser.ExpressionContext):
        pass


    # Enter a parse tree produced by geneticalParser#atom.
    def enterAtom(self, ctx:geneticalParser.AtomContext):
        pass

    # Exit a parse tree produced by geneticalParser#atom.
    def exitAtom(self, ctx:geneticalParser.AtomContext):
        pass


    # Enter a parse tree produced by geneticalParser#variable.
    def enterVariable(self, ctx:geneticalParser.VariableContext):
        pass

    # Exit a parse tree produced by geneticalParser#variable.
    def exitVariable(self, ctx:geneticalParser.VariableContext):
        pass


    # Enter a parse tree produced by geneticalParser#relop.
    def enterRelop(self, ctx:geneticalParser.RelopContext):
        pass

    # Exit a parse tree produced by geneticalParser#relop.
    def exitRelop(self, ctx:geneticalParser.RelopContext):
        pass



del geneticalParser