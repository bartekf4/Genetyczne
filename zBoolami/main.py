from antlr4 import *

from bezBoolowLexer import bezBoolowLexer
from bezBoolowParser import bezBoolowParser
from bezBoolowVisitor import bezBoolowVisitor
from bezBoolowListener import bezBoolowListener


def translate(filename: str):
    file_stream = FileStream(fileName=filename)
    lexer = bezBoolowLexer(file_stream)
    stream = CommonTokenStream(lexer)
    parser = bezBoolowParser(stream)
    tree = parser.file_()

    printer = bezBoolowListener()
    visitor = bezBoolowVisitor()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    visitor.visit(tree)


if __name__ == '__main__':
    translate("test.txt")