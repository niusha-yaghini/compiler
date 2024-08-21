from antlr4 import *

from STListener import STGrammarListener
from gen.STGrammarLexer import STGrammarLexer
from gen.STGrammarParser import STGrammarParser

print("Enter an arithmetic expression (or type 'exit' to quit): ")
all_inputs = []

while True:
    new_input = input()

    # Check if the user wants to exit
    if new_input.lower() == 'exit':
        break

    all_inputs.append(new_input)

seperator = '\n'
input_expression = seperator.join(all_inputs)

# Parse and evaluate the expression
lexer = STGrammarLexer(InputStream(input_expression))
token_stream = CommonTokenStream(lexer)
parser = STGrammarParser(token_stream)
parse_tree = parser.start()
listener = STGrammarListener()
walker = ParseTreeWalker()
walker.walk(listener, parse_tree)
result = listener.result
print("Result :", result)
