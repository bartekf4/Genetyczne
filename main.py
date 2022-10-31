from antlr4 import *
import io
from gen.geneticalParser import geneticalParser
from gen.geneticalVisitor import geneticalVisitor
from gen.geneticalLexer import geneticalLexer
from gen.geneticalListener import geneticalListener
import argparse


def main(filename_: str):
    lexer = geneticalLexer(FileStream(filename_))
    stream = CommonTokenStream(lexer)
    parser = geneticalParser(stream)
    parser.buildParseTrees()
    ctx = parser.file_()

    listener = geneticalListener()
    visitor = geneticalVisitor()
    visitor.visit(ctx)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Paser of a language with the grammar stored in genetical.g4 file')
    # parser.add_argument('f', metavar="filename", required=True, type=str)
    # args = parser.parse_args()
    # filename = args.f
    filename = 'example.txt'
    main(filename)
