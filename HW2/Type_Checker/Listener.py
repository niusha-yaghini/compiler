# from gen.TypeCheckerListener import TypeCheckerListener
from gen.TypeCheckerListener import TypeCheckerListener
class TypeCheckerListener(TypeCheckerListener):
    def __init__(self):
        self.result = 0
        self.stack = []
        self.error = 'no'

    # Exit a parse tree produced by TypeCheckerParser#start.
    def exitStart(self, ctx):
        print("start")
        pass

    # Exit a parse tree produced by TypeCheckerParser#expr3.
    def exitExpr3(self, ctx):
        print("Expr3")
        pass

    # Exit a parse tree produced by TypeCheckerParser#expr2.
    def exitExpr2(self, ctx):
        print("Expr2")

        if (self.error == "no"):
            second_operator = self.stack.pop()
            first_operator = self.stack.pop()

            if (first_operator == "String"):
                self.error = "yes"
                self.result = "Type error: String cannot be subtracted"
            elif (first_operator == "Integer"):
                if (second_operator == "Integer"):
                    self.result = "Integer"
                    self.stack.append(self.result)
                elif (second_operator == "Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be subtracted"
            elif (first_operator == "Float"):
                if (second_operator == "Integer" or second_operator == "Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be subtracted"

        print("result = ", self.result)
        print("stack = ", self.stack)
        pass

    # Exit a parse tree produced by TypeCheckerParser#expr1.
    def exitExpr1(self, ctx):
        print("Expr1")

        if (self.error == "no"):
            second_operator = self.stack.pop()
            first_operator = self.stack.pop()

            if (first_operator == "String"):
                self.result = "String"
                self.stack.append(self.result)
            elif (first_operator == "Integer"):
                if (second_operator == "Integer"):
                    self.result = "Integer"
                    self.stack.append(self.result)
                elif (second_operator == "Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be concatenated to an Integer"
            elif (first_operator == "Float"):
                if (second_operator == "Integer" or second_operator == "Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be concatenated to an Float"

        print("result = ", self.result)
        print("stack = ", self.stack)
        pass

    # Exit a parse tree produced by TypeCheckerParser#term2.
    def exitTerm2(self, ctx):
        print("Term2")

        if(self.error=="no"):
            second_operator = self.stack.pop()
            first_operator = self.stack.pop()

            if(first_operator=="String"):
                self.error = "yes"
                self.result = "Type error: String cannot be divided"
            elif(first_operator=="Integer"):
                if(second_operator=="Integer" or second_operator=="Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be divided"
            elif(first_operator=="Float"):
                if (second_operator == "Integer" or second_operator == "Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be divided"

        print("result = ", self.result)
        print("stack = ", self.stack)
        pass

    # Exit a parse tree produced by TypeCheckerParser#term3.
    def exitTerm3(self, ctx):
        print("Term3")
        pass

    # Exit a parse tree produced by TypeCheckerParser#term1.
    def exitTerm1(self, ctx):
        print("Term1")

        if(self.error=="no"):
            second_operator = self.stack.pop()
            first_operator = self.stack.pop()

            if(first_operator=="String"):
                self.error = "yes"
                self.result = "Type error: String cannot be multiplied"
            elif(first_operator=="Integer"):
                if(second_operator=="Integer"):
                    self.result = "Integer"
                    self.stack.append(self.result)
                elif(second_operator=="Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be multiplied"
            elif(first_operator=="Float"):
                if (second_operator == "Integer" or second_operator == "Float"):
                    self.result = "Float"
                    self.stack.append(self.result)
                else:
                    self.error = "yes"
                    self.result = "Type error: String cannot be multiplied"

        print("result = ", self.result)
        print("stack = ", self.stack)
        pass

    # Exit a parse tree produced by TypeCheckerParser#factString.
    def exitFactString(self, ctx):
        print("FactString")
        self.result = "String"
        print("result = ", self.result)
        print("answer = ", ctx.getChild(0))
        self.stack.append(self.result)
        print("stack = ", self.stack)
        pass

    # Exit a parse tree produced by TypeCheckerParser#factInteger.
    def exitFactInteger(self, ctx):
        print("FactInteger")
        self.result = "Integer"
        print("result = ", self.result)
        print("answer = ", ctx.getChild(0))
        self.stack.append(self.result)
        print("stack = ", self.stack)
        pass

    # Exit a parse tree produced by TypeCheckerParser#factFloat.
    def exitFactFloat(self, ctx):
        print("FactFloat")
        self.result = "Float"
        print("result = ", self.result)
        print("answer = ", ctx.getChild(0))
        self.stack.append(self.result)
        print("stack = ", self.stack)
        pass

    # Exit a parse tree produced by TypeCheckerParser#factExpr.
    def exitFactExpr(self, ctx):
        print("FactExpr")
        pass
