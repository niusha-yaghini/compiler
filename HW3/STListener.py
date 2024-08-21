from gen.STGrammarListener import STGrammarListener
import sqlite3

# This class defines a complete listener for a parse tree produced by STGrammarParser.
class STGrammarListener(STGrammarListener):
    def __init__(self):
        self.result = []
        self.id_counter = 1
        self.name = ''
        self.current_type = ''
        self.current_value = 0
        self.all_inputs = []
        self.stack_values = []
        self.stack_types = []
        self.db_connection = sqlite3.connect('symbol_table.db')
        self.db_cursor = self.db_connection.cursor()

    def write_in_text_file(self):
        with open("output.txt", "w") as file:
            file.write("ID Name Type Value\n")
            for entry in self.all_inputs:
                file.write(" ".join(map(str, entry)) + "\n")

    def write_in_sqlite_file(self):
        # make table
        # self.db_cursor.execute('''CREATE TABLE IF NOT EXISTS symbol_table
        #                          (ID INTEGER PRIMARY KEY,
        #                             Name TEXT,
        #                             Type TEXT,
        #                             Value TEXT)''')

        # Insert symbol table data into the database
        try:
            for entry in self.all_inputs:
                self.db_cursor.execute('''INSERT INTO symbol_table (ID, Name, Type, Value)
                                            VALUES (?, ?, ?, ?)''', entry)

            self.db_connection.commit()
        except:
            print()

        print("Entry added successfully in sqlite.")

        # Commit changes and close the database connection
        # self.db_connection.commit()
        self.db_connection.close()


    # Exit a parse tree produced by STGrammarParser#start.
    def exitStart(self, ctx):
        # print("exitStart")
        # print(ctx.getChild(0))

        print("ID Name Type Value")
        for i in range(len(self.all_inputs)):
            for j in range(len(self.all_inputs[i])):
                print(self.all_inputs[i][j], end=' ')
            print()

        #text file part (writing to output.txt)
        self.write_in_text_file()

        #sqlite part (Create a table to store the symbol table data)
        self.write_in_sqlite_file()

        # self.print_symbol_table_data()

        pass

    # Exit a parse tree produced by STGrammarParser#assigns.
    def exitAssigns(self, ctx):
        pass

    # Exit a parse tree produced by STGrammarParser#assign.
    def exitAssign(self, ctx):
        self.name = ctx.getChild(0)

        if(self.current_value != None):
            repetition_flag = False
            for i in self.all_inputs:
                if (i[1].getText() == self.name.getText()):
                    i[2] = self.current_type
                    i[3] = self.current_value
                    repetition_flag = True

            if(repetition_flag == False):
                self.all_inputs.append([self.id_counter, self.name, self.current_type, self.current_value])
                self.id_counter += 1
        pass

    # Exit a parse tree produced by STGrammarParser#expr.
    def exitExpr(self, ctx):
        if ctx.getChildCount() == 3:  # Check if it's a binary operation
            operator = ctx.getChild(1).getText()  # Get the operator
            operand1_value = self.stack_values.pop()
            operand1_type = self.stack_types.pop()
            operand2_value = self.stack_values.pop()
            operand2_type = self.stack_types.pop()
            type_check = self.Expr_errorChecker(operand1_type, operand2_type, operator)

            if(type_check != 'Type Error!'):
                if(operand1_type=='Integer'): operand1_value = int(operand1_value)
                elif(operand1_type=='Float'): operand1_value = float(operand1_value)
                else: operand1_value = operand1_value[1:]

                if(operand2_type=='Integer'): operand2_value = int(operand2_value)
                elif(operand2_type=='Float'): operand2_value = float(operand2_value)
                else: operand2_value = operand2_value[:-1]

                if operator == "-":
                    self.current_value = operand2_value - operand1_value
                    self.stack_values.append(self.current_value)
                    self.current_type = type_check
                    self.stack_types.append(self.current_type)
                elif operator == "+":
                    self.current_value = operand2_value + operand1_value
                    self.stack_values.append(self.current_value)
                    self.current_type = type_check
                    self.stack_types.append(self.current_type)
            else:
                print(type_check)
                self.current_value = None
        pass

    # Exit a parse tree produced by STGrammarParser#term.
    def exitTerm(self, ctx):
        if ctx.getChildCount() == 3:  # Check if it's a binary operation
            operator = ctx.getChild(1).getText()  # Get the operator

            operand1_value = self.stack_values.pop()
            operand1_type = self.stack_types.pop()
            operand2_value = self.stack_values.pop()
            operand2_type = self.stack_types.pop()
            type_check = self.Term_errorChecker(operand1_type, operand2_type, operator)

            if (type_check != 'Type Error!'):
                if (operand1_type == 'Integer'):
                    operand1_value = int(operand1_value)
                elif (operand1_type == 'Float'):
                    operand1_value = float(operand1_value)

                if (operand2_type == 'Integer'):
                    operand2_value = int(operand2_value)
                elif (operand2_type == 'Float'):
                    operand2_value = float(operand2_value)

                if operator == "/":
                    self.current_value = operand2_value / operand1_value
                    self.stack_values.append(self.current_value)
                    self.current_type = type_check
                    self.stack_types.append(self.current_type)
                elif operator == "*":
                    self.current_value = operand2_value * operand1_value
                    self.stack_values.append(self.current_value)
                    self.current_type = type_check
                    self.stack_types.append(self.current_type)
            else:
                print(type_check)
                self.current_value = None
    pass

    # Exit a parse tree produced by STGrammarParser#factor_is_string.
    def exitFactor_is_string(self, ctx):
        self.current_value = ctx.getChild(0).getText()
        self.current_type = 'String'
        self.stack_values.append(self.current_value)
        self.stack_types.append(self.current_type)
        # print("stack_values: ", self.stack_values)
        # print("stack_types: ", self.stack_types)
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_integer.
    def exitFactor_is_integer(self, ctx):
        # print("exitFactor_is_integer")

        # ctx.getChildCount()>1 means we have sign number
        if(ctx.getChildCount()>1):
            # print("child count: ", ctx.getChildCount())
            # print("child[1]: ", ctx.getChild(1))
            self.current_value = int(ctx.getChild(1).getText())*self.current_value
            # print("current value: ", self.current_value)
        else:
            # print("child[0]: ", ctx.getChild(0))
            self.current_value = ctx.getChild(0).getText()
            # print("current value: ", self.current_value)

        self.current_type = 'Integer'
        self.stack_values.append(self.current_value)
        self.stack_types.append(self.current_type)
        # print("stack_values: ", self.stack_values)
        # print("stack_types: ", self.stack_types)
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_float.
    def exitFactor_is_float(self, ctx):
        # print("exitFactor_is_float")

        # ctx.getChildCount()>1 means we have sign number
        if(ctx.getChildCount()>1):
            self.current_value = float(ctx.getChild(1).getText())*self.current_value
        else:
            self.current_value = ctx.getChild(0).getText()

        self.current_type = 'Float'
        self.stack_values.append(self.current_value)
        self.stack_types.append(self.current_type)
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_expression.
    def exitFactor_is_expression(self, ctx):
        pass

    # Exit a parse tree produced by STGrammarParser#factor_is_id.
    def exitFactor_is_id(self, ctx):
        # print("exitFactor_id")
        # print(ctx.getChild(0))
        my_id = ctx.getChild(0)
        valid_id_flag = False
        for i in self.all_inputs:
            if(i[1].getText() == my_id.getText()):
                self.current_type = i[2]
                self.current_value = i[3]
                valid_id_flag = True
                self.stack_values.append(self.current_value)
                self.stack_types.append(self.current_type)
                # print("stack_values: ", self.stack_values)
                # print("stack_types: ", self.stack_types)

        if(valid_id_flag==False):
            print("This id =>", my_id, "does not exist.")
            self.current_value = None
        pass

    # Exit a parse tree produced by STGrammarParser#sign.
    def exitSign(self, ctx):
        # print("exitSign")
        # print(ctx.getChild(0))

        if(ctx.getChild(0).getText()=="+"):
            self.current_value = 1
        elif(ctx.getChild(0).getText()=="-"):
            self.current_value = -1
        # print("current value: ", self.current_value)

        pass

    def Expr_errorChecker(self, type1, type2, operator):
        if(type1=='Integer' and type2=='Integer'):
            return 'Integer'
        elif(type1=='Integer' and type2=='Float'):
            return 'Float'
        elif(type1=='Float' and type2=='Integer'):
            return 'Float'
        elif(type1=='Float' and type2=='Float'):
            return 'Float'
        elif(type1=='String' and type2=='String' and operator=='+'):
            return 'String'
        else:
            return 'Type Error!'

    def Term_errorChecker(self, type1, type2, operator):
        if(type1=='Integer' and type2=='Integer' and operator=='*'):
            return 'Integer'
        elif(type1=='Integer' and type2=='Integer' and operator=='/'):
            return 'Float'
        elif(type1=='Integer' and type2=='Float'):
            return 'Float'
        elif(type1=='Float' and type2=='Integer'):
            return 'Float'
        elif(type1=='Float' and type2=='Float'):
            return 'Float'
        else:
            return 'Type Error!'
