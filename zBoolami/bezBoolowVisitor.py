# Generated from C:/Users/fudal/OneDrive/Dokumenty/GitHub/Genetyczne\bezBoolow.g4 by ANTLR 4.11.1
from antlr4 import *
import autopep8

if __name__ is not None and "." in __name__:
    from .bezBoolowParser import bezBoolowParser
else:
    from bezBoolowParser import bezBoolowParser


# This class defines a complete generic visitor for a parse tree produced by bezBoolowParser.

class bezBoolowVisitor(ParseTreeVisitor):
    out_path = "out.py"

    def __init__(self, out_path="out.py"):
        self.out_path = out_path

    def __del__(self):
        self.output = autopep8.fix_code(self.output)
        print(self.output)
        with open(f'{self.out_path}', 'w') as file:
            file.write(self.output)

    output = ""
    indent = 0
    tab = "\t"

    def getIndent(self):
        return self.indent * self.tab

    def addNewLine(self):
        self.output += '\n'

    # Visit a parse tree produced by bezBoolowParser#file_.
    def visitFile_(self, ctx: bezBoolowParser.File_Context):
        self.visitInputBlock(ctx.inputBlock())
        self.visitBlockseq(ctx.blockseq())

    # Visit a parse tree produced by bezBoolowParser#blockseq.
    def visitBlockseq(self, ctx: bezBoolowParser.BlockseqContext):
        for block in ctx.children:
            self.visitBlock(block)

    # Visit a parse tree produced by bezBoolowParser#block.
    def visitBlock(self, ctx: bezBoolowParser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by bezBoolowParser#printBlock.
    def visitPrintBlock(self, ctx: bezBoolowParser.PrintBlockContext):
        self.output += f'{self.getIndent()}{self.visitPrintSeq(ctx)}\n'

    # Visit a parse tree produced by bezBoolowParser#printSeq.
    def visitPrintSeq(self, ctx: bezBoolowParser.PrintSeqContext):
        return ctx.getText()

    # Visit a parse tree produced by bezBoolowParser#inputBlock.
    def visitInputBlock(self, ctx: bezBoolowParser.InputBlockContext):
        self.output += f'input = input({self.visitInputSeq(ctx.inputSeq())})\n'
        return self.visitChildren(ctx)

    # Visit a parse tree produced by bezBoolowParser#inputSeq.
    def visitInputSeq(self, ctx: bezBoolowParser.InputSeqContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by bezBoolowParser#filename.
    def visitFilename(self, ctx: bezBoolowParser.FilenameContext):
        return ctx.getText()

    # Visit a parse tree produced by bezBoolowParser#variableDefinition.
    def visitVariableDefinition(self, ctx: bezBoolowParser.VariableDefinitionContext):
        self.output += f'{self.getIndent()}{ctx.VARIABLE()}{ctx.EQ()}{self.visitEquation(ctx.equation())}\n'
        self.visitEquation(ctx.equation())
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by bezBoolowParser#loopBlock.
    def visitLoopBlock(self, ctx: bezBoolowParser.LoopBlockContext):
        self.output += f'{self.getIndent()}{ctx.WHILE()} {self.visitExpression(ctx.expression())}: \n'
        self.indent += 1
        # self.visitExpression(ctx)
        self.visitBlockseq(ctx.blockseq())
        self.indent -= 1

    # Visit a parse tree produced by bezBoolowParser#ifBlock.
    def visitIfBlock(self, ctx: bezBoolowParser.IfBlockContext):
        self.output += f'{self.getIndent()}{ctx.IF()} {self.visitExpression(ctx.expression())}: \n'
        self.indent += 1
        self.visitBlockseq(ctx.blockseq())
        self.indent -= 1

    # Visit a parse tree produced by bezBoolowParser#expression.
    def visitExpression(self, ctx: bezBoolowParser.ExpressionContext):
        return ctx.getText()
        pass

    # expression
    # :   expression(OR | AND)
    # expression
    # | expression(GT | LT)
    # expression
    # | expression(EQ_LOGICAL | NOT_EQ_LOGICAL)
    # expression
    # | LPAREN
    # expression
    # RPAREN
    # | NOT
    # expression
    # | equation;

    # Visit a parse tree produced by bezBoolowParser#equation.
    def visitEquation(self, ctx: bezBoolowParser.EquationContext):
        # self.output += f'{ctx.getText()}'
        return ctx.getText()
        # return self.visitChildren(ctx)

    # Visit a parse tree produced by bezBoolowParser#atom.
    def visitAtom(self, ctx: bezBoolowParser.AtomContext):
        print(ctx.getText(), "aaaaaaaa")
        return self.visitChildren(ctx)


del bezBoolowParser
