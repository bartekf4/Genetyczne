# Generated from C:/Users/fudal/OneDrive/Dokumenty/GitHub/Genetyczne/evaluator\bezBoolow.g4 by ANTLR 4.11.1
import autopep8
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .bezBoolowParser import bezBoolowParser
else:
    from bezBoolowParser import bezBoolowParser


# This class defines a complete generic visitor for a parse tree produced by bezBoolowParser.

class bezBoolowVisitor(ParseTreeVisitor):
    out_path = "out.py"

    def __init__(self, out_path):
        self.variables = []
        self.out_path = out_path.split(".")[0] + ".py"

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

    # Visit a parse tree produced by bezBoolowParser#file_.
    def visitFile_(self, ctx: bezBoolowParser.File_Context):
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
        self.output += f'{self.getIndent()}print({self.visitEquation(ctx.equation())})\n'

    # Visit a parse tree produced by bezBoolowParser#inputBlock.
    def visitInputBlock(self, ctx: bezBoolowParser.InputBlockContext):
        self.output += f'{self.getIndent()}{ctx.VARIABLE()} = float(input())\n'
        return self.visitChildren(ctx)
    #     VARIABLE EQ equation ENDCHAR|
    #     VARIABLE EQ expression ENDCHAR;
    # Visit a parse tree produced by bezBoolowParser#variableDefinition.
    def visitVariableDefinition(self, ctx: bezBoolowParser.VariableDefinitionContext):
        self.variables.append(ctx.VARIABLE())
        if ctx.equation() is not None:
            self.output += f'{self.getIndent()}{ctx.VARIABLE()}{ctx.EQ()}{self.visitEquation(ctx.equation())}\n'
        if ctx.expression() is not None:
            self.output += f'{self.getIndent()}{ctx.VARIABLE()}{ctx.EQ()}{self.visitExpression(ctx.expression())}\n'

        # self.visitEquation(ctx.equation())

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
        if ctx.OR() is not None:
            return f'{self.visitExpression(ctx.expression(0))} or {self.visitExpression(ctx.expression(1))}'
        if ctx.AND() is not None:
            return f'{self.visitExpression(ctx.expression(0))} and {self.visitExpression(ctx.expression(1))}'
        if ctx.GT() is not None:
            return f'{self.visitExpression(ctx.expression(0))} > {self.visitExpression(ctx.expression(1))}'
        if ctx.LT() is not None:
            return f'{self.visitExpression(ctx.expression(0))} < {self.visitExpression(ctx.expression(1))}'
        if ctx.EQ_LOGICAL() is not None:
            return f'{self.visitExpression(ctx.expression(0))} == {self.visitExpression(ctx.expression(1))}'
        if ctx.NOT_EQ_LOGICAL() is not None:
            return f'{self.visitExpression(ctx.expression(0))} != {self.visitExpression(ctx.expression(1))}'
        if ctx.LPAREN() and ctx.RPAREN() is not None:
            return f'({self.visitExpression(ctx.expression(0))})'
        if ctx.equation() is not None:
            return self.visitEquation(ctx.equation())

    # Visit a parse tree produced by bezBoolowParser#equation.
    def visitEquation(self, ctx: bezBoolowParser.EquationContext):
        if ctx is None:
            return
        if ctx.atom() is not None and ctx.MINUS() is not None:
            return f'-{self.visitAtom(ctx.atom())}'
        if ctx.atom() is not None:
            return f'{self.visitAtom(ctx.atom())}'

        if ctx.TIMES() is not None:
            return f'{self.visitEquation(ctx.equation(0))} * {self.visitEquation(ctx.equation(1))}'
        if ctx.DIV() is not None:
            return f'{self.visitEquation(ctx.equation(0))} / {self.visitEquation(ctx.equation(1))}'
        if ctx.PLUS() is not None:
            return f'{self.visitEquation(ctx.equation(0))} + {self.visitEquation(ctx.equation(1))}'
        if ctx.MINUS() is not None:
            return f'{self.visitEquation(ctx.equation(0))} - {self.visitEquation(ctx.equation(1))}'
        if ctx.LPAREN() is not None:
            return f'({self.visitEquation(ctx.equation(0))})'




    # Visit a parse tree produced by bezBoolowParser#atom.
    def visitAtom(self, ctx: bezBoolowParser.AtomContext):


        if ctx.VARIABLE() is not None:
            if ctx.VARIABLE() in self.variables:
                return ctx.VARIABLE()
            else:
                return 0
        if ctx.NUM() is not None:
            return ctx.NUM()
        if ctx.FLOAT() is not None:
            return ctx.FLOAT()




del bezBoolowParser
