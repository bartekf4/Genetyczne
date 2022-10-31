from antlr4 import *
import io
from gen.geneticalParser import geneticalParser
from gen.geneticalVisitor import geneticalVisitor
from gen.geneticalLexer import geneticalLexer
from gen.geneticalListener import geneticalListener

def main():
    lexer = geneticalLexer(FileStream('example.txt'))
    stream = CommonTokenStream(lexer)
    parser = geneticalParser(stream)

    ctx = parser.file_()

    listener = geneticalListener()
    visitor = geneticalVisitor()
    visitor.visit(ctx)


if __name__ == '__main__':
    main()

