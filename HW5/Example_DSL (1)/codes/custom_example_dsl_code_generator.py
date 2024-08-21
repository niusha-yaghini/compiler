class CustomExampleDSLCodeGenerator:
    def __init__(self):
        self.non_operands = ['program', 'initiate_game',
                             'bomb_location', 'output',
                             'bomb_placements', 'begin_scope_operator',
                             'end_scope_operator', 'hint']

        self.hint = False
        self.operand_stack = []
        self.code_stack = []

    def is_operand(self, item):
        if item in self.non_operands:
            return False
        else:
            return True

    def generate_code(self, post_order_array):
        for item in post_order_array:
            if not self.is_operand(item["label"]):
                self.generate_code_based_on_non_operand(item["label"])
            else:
                self.operand_stack.append(item["label"])

        result = ''
        for code_string in self.code_stack:
            if code_string is not None:
                result += code_string
        return result

    def generate_code_based_on_non_operand(self, item):
        if item == "program":
            self.generate_program()

        elif item == "output":
            self.set_output_type()

        elif item == "initiate_game":
            self.generate_initiate_game()

        elif item == "bomb_location":
            self.generate_bomb()

        elif item == "bomb_placements":
            self.generate_bomb_placements()

        elif item == "hint":
            self.generate_hint()

        elif item == "begin_scope_operator":
            self.generate_begin_scope_operator()

        elif item == "end_scope_operator":
            self.generate_end_scope_operator()

    def generate_program(self):
        placements_code = self.code_stack.pop()
        initiate_code = self.code_stack.pop()
        output_type = 'console'
        hint_code = 'hint = False\n'

        if len(self.code_stack) > 0:
            temp_code = self.code_stack.pop()
            if temp_code.startswith('##COMPILER_PARAM:::output_type:::'):
                output_type = temp_code.replace('##COMPILER_PARAM:::output_type:::', '')
            else:
                self.code_stack.append(temp_code)
                hint_code = temp_code

        if output_type == 'console':
            program_code = (initiate_code + placements_code + hint_code +
                            "if(hint):\n" +
                            "\tfor row in range(len(bombs)):\n" +
                            "\t\tfor column in range(len(bombs[0])):\n" +
                            "\t\t\tif(bombs[row][column]==-1 and hint):\n" +
                            "\t\t\t\tfor x in range(row-1, row+2):\n" +
                            "\t\t\t\t\tfor y in range(column-1, column+2):\n" +
                            "\t\t\t\t\t\tif(0<=x<len(bombs) and 0<=y<len(bombs[0])):\n" +
                            "\t\t\t\t\t\t\tif(bombs[x][y]!=-1):\n" +
                            "\t\t\t\t\t\t\t\tbombs[x][y]+=1\n" +
                            "for i in bombs:\n" +
                            "\tfor j in i:\n" +
                            "\t\tif(j == -1):\n" +
                            "\t\t\tprint('*', end='')\n" +
                            "\t\telif (j == 0):\n" +
                            "\t\t\tprint('#', end='')\n" +
                            "\t\telse:\n" +
                            "\t\t\tprint(j, end='')\n" +
                            "\tprint()\n"
                            )
            self.code_stack.append(program_code)

    def generate_initiate_game(self):
        height = int(self.operand_stack.pop())
        width = int(self.operand_stack.pop())
        code_string = f"bombs = [[0 for y in range({height})] for x in range({width})]\n"
        self.code_stack.append(code_string)

    def generate_bomb(self):
        y = int(self.operand_stack.pop())
        x = int(self.operand_stack.pop())
        code_string = f"bombs[{x - 1}][{y - 1}] = -1\n"
        self.code_stack.append(code_string)

    def generate_hint(self):
        hint = self.operand_stack.pop()
        if hint == 'True':
            self.hint = True

    def set_output_type(self):
        self.code_stack.append(f"##COMPILER_PARAM:::output_type:::{self.operand_stack.pop()}")

    def generate_bomb_placements(self):
        temp_block_stack = []
        current_code = self.code_stack.pop()
        if current_code != '##COMPILER_PARAM:::scope:::end_scope_operator':
            self.code_stack.append(current_code)
            return
        while current_code != '##COMPILER_PARAM:::scope:::begin_scope_operator':
            current_code = self.code_stack.pop()
            temp_block_stack.append(current_code)
        temp_block_stack.pop()
        result = ''
        while len(temp_block_stack) != 0:
            result = result + temp_block_stack.pop()
        self.code_stack.append(result)

    def generate_begin_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::begin_scope_operator")

    def generate_end_scope_operator(self):
        self.code_stack.append("##COMPILER_PARAM:::scope:::end_scope_operator")


