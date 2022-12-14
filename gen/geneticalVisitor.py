from antlr4 import *

if __name__ is not None and "." in __name__:
    from .geneticalParser import geneticalParser
else:
    from geneticalParser import geneticalParser


# This class defines a complete generic visitor for a parse tree produced by geneticalParser.

class geneticalVisitor(ParseTreeVisitor):
    out_path = "out.py"

    def __init__(self, out_path="out.py"):
        self.out_path = out_path

    def __del__(self):
        self.output = autopep8.fix_code(self.output)
        with open(f'{self.out_path}', 'w') as file:
            file.write(self.output)

    output = ""
    indent = 0
    tab = "\t"

    def getIndent(self):
        return self.indent * self.tab

    def addNewLine(self):
        self.output += '\n'

    # Visit a parse tree produced by geneticalParser#file_.
    def visitFile_(self, ctx: geneticalParser.File_Context):
        self.visit(ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#blockseq.
    def visitBlockseq(self, ctx: geneticalParser.BlockseqContext):
        self.visit(ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#block.
    def visitBlock(self, ctx: geneticalParser.BlockContext):
        self.visit(ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#variableOperation.
    def visitVariableOperation(self, ctx: geneticalParser.VariableOperationContext):
        self.visit(ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#loopBlock.
    def visitLoopBlock(self, ctx: geneticalParser.LoopBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#ifBlock.
    def visitIfBlock(self, ctx: geneticalParser.IfBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#variableDefinition.
    def visitVariableDefinition(self, ctx: geneticalParser.VariableDefinitionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#logicalExp.
    def visitLogicalExp(self, ctx: geneticalParser.LogicalExpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#relopLogical.
    def visitRelopLogical(self, ctx: geneticalParser.RelopLogicalContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#equation.
    def visitEquation(self, ctx: geneticalParser.EquationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#expression.
    def visitExpression(self, ctx: geneticalParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#atom.
    def visitAtom(self, ctx: geneticalParser.AtomContext):
        print("jjjjjjjjjjj")
        self.output += f'{self.getIndent()}{ctx.NUMBER()}'
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#variable.
    def visitVariable(self, ctx: geneticalParser.VariableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by geneticalParser#relop.
    def visitRelop(self, ctx: geneticalParser.RelopContext):
        return self.visitChildren(ctx)


del geneticalParser
