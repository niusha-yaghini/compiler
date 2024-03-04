# Generated from D:/1402 - 2/compiler/assignments/HW1/First_excercise/Simple-Calculator/grammar/ArithmeticExpression.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,94,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,1,1,5,1,24,8,1,10,1,12,1,27,9,
        1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,
        1,3,1,3,1,3,3,3,45,8,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,53,8,3,10,3,12,
        3,56,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,67,8,4,10,4,12,
        4,70,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,80,8,5,1,6,1,6,1,7,
        5,7,85,8,7,10,7,12,7,88,9,7,1,7,1,7,1,8,1,8,1,8,0,2,6,8,9,0,2,4,
        6,8,10,12,14,16,0,2,1,0,13,14,1,0,3,4,97,0,18,1,0,0,0,2,35,1,0,0,
        0,4,37,1,0,0,0,6,44,1,0,0,0,8,57,1,0,0,0,10,79,1,0,0,0,12,81,1,0,
        0,0,14,86,1,0,0,0,16,91,1,0,0,0,18,19,3,2,1,0,19,20,5,0,0,1,20,1,
        1,0,0,0,21,25,3,4,2,0,22,24,5,11,0,0,23,22,1,0,0,0,24,27,1,0,0,0,
        25,23,1,0,0,0,25,26,1,0,0,0,26,31,1,0,0,0,27,25,1,0,0,0,28,30,3,
        2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,
        36,1,0,0,0,33,31,1,0,0,0,34,36,3,4,2,0,35,21,1,0,0,0,35,34,1,0,0,
        0,36,3,1,0,0,0,37,38,5,12,0,0,38,39,5,1,0,0,39,40,3,6,3,0,40,5,1,
        0,0,0,41,42,6,3,-1,0,42,45,3,8,4,0,43,45,5,10,0,0,44,41,1,0,0,0,
        44,43,1,0,0,0,45,54,1,0,0,0,46,47,10,4,0,0,47,48,5,3,0,0,48,53,3,
        8,4,0,49,50,10,3,0,0,50,51,5,4,0,0,51,53,3,8,4,0,52,46,1,0,0,0,52,
        49,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,7,1,0,0,
        0,56,54,1,0,0,0,57,58,6,4,-1,0,58,59,3,10,5,0,59,68,1,0,0,0,60,61,
        10,3,0,0,61,62,5,5,0,0,62,67,3,10,5,0,63,64,10,2,0,0,64,65,5,6,0,
        0,65,67,3,10,5,0,66,60,1,0,0,0,66,63,1,0,0,0,67,70,1,0,0,0,68,66,
        1,0,0,0,68,69,1,0,0,0,69,9,1,0,0,0,70,68,1,0,0,0,71,80,3,12,6,0,
        72,80,3,14,7,0,73,74,5,7,0,0,74,75,3,6,3,0,75,76,5,8,0,0,76,80,1,
        0,0,0,77,80,5,9,0,0,78,80,5,12,0,0,79,71,1,0,0,0,79,72,1,0,0,0,79,
        73,1,0,0,0,79,77,1,0,0,0,79,78,1,0,0,0,80,11,1,0,0,0,81,82,7,0,0,
        0,82,13,1,0,0,0,83,85,3,16,8,0,84,83,1,0,0,0,85,88,1,0,0,0,86,84,
        1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,90,3,12,6,0,
        90,15,1,0,0,0,91,92,7,1,0,0,92,17,1,0,0,0,10,25,31,35,44,52,54,66,
        68,79,86
    ]

class ArithmeticExpressionParser ( Parser ):

    grammarFileName = "ArithmeticExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "')'", "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "SIGN", "ADD", "SUB", "MUL", 
                      "DIV", "LPAREN", "RPAREN", "STRING", "WS", "NEWLINE", 
                      "ID", "FLOAT", "INTEGER" ]

    RULE_start = 0
    RULE_assigns = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_term = 4
    RULE_factor = 5
    RULE_number = 6
    RULE_signednum = 7
    RULE_sign = 8

    ruleNames =  [ "start", "assigns", "assign", "expr", "term", "factor", 
                   "number", "signednum", "sign" ]

    EOF = Token.EOF
    T__0=1
    SIGN=2
    ADD=3
    SUB=4
    MUL=5
    DIV=6
    LPAREN=7
    RPAREN=8
    STRING=9
    WS=10
    NEWLINE=11
    ID=12
    FLOAT=13
    INTEGER=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigns(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.AssignsContext,0)


        def EOF(self):
            return self.getToken(ArithmeticExpressionParser.EOF, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = ArithmeticExpressionParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.assigns()
            self.state = 19
            self.match(ArithmeticExpressionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.AssignContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ArithmeticExpressionParser.NEWLINE)
            else:
                return self.getToken(ArithmeticExpressionParser.NEWLINE, i)

        def assigns(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.AssignsContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.AssignsContext,i)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_assigns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigns" ):
                listener.enterAssigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigns" ):
                listener.exitAssigns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigns" ):
                return visitor.visitAssigns(self)
            else:
                return visitor.visitChildren(self)




    def assigns(self):

        localctx = ArithmeticExpressionParser.AssignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assigns)
        self._la = 0 # Token type
        try:
            self.state = 35
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.assign()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 22
                    self.match(ArithmeticExpressionParser.NEWLINE)
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 28
                        self.assigns() 
                    self.state = 33
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ArithmeticExpressionParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ArithmeticExpressionParser.ID)
            self.state = 38
            self.match(ArithmeticExpressionParser.T__0)
            self.state = 39
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.TermContext,0)


        def WS(self):
            return self.getToken(ArithmeticExpressionParser.WS, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def ADD(self):
            return self.getToken(ArithmeticExpressionParser.ADD, 0)

        def SUB(self):
            return self.getToken(ArithmeticExpressionParser.SUB, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExpressionParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 7, 9, 12, 13, 14]:
                self.state = 42
                self.term(0)
                pass
            elif token in [10]:
                self.state = 43
                self.match(ArithmeticExpressionParser.WS)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 52
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExpressionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 47
                        self.match(ArithmeticExpressionParser.ADD)
                        self.state = 48
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExpressionParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 49
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 50
                        self.match(ArithmeticExpressionParser.SUB)
                        self.state = 51
                        self.term(0)
                        pass

             
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.TermContext,0)


        def MUL(self):
            return self.getToken(ArithmeticExpressionParser.MUL, 0)

        def DIV(self):
            return self.getToken(ArithmeticExpressionParser.DIV, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ArithmeticExpressionParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ArithmeticExpressionParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 60
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 61
                        self.match(ArithmeticExpressionParser.MUL)
                        self.state = 62
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = ArithmeticExpressionParser.TermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 63
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 64
                        self.match(ArithmeticExpressionParser.DIV)
                        self.state = 65
                        self.factor()
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.NumberContext,0)


        def signednum(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.SignednumContext,0)


        def LPAREN(self):
            return self.getToken(ArithmeticExpressionParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ArithmeticExpressionParser.RPAREN, 0)

        def STRING(self):
            return self.getToken(ArithmeticExpressionParser.STRING, 0)

        def ID(self):
            return self.getToken(ArithmeticExpressionParser.ID, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = ArithmeticExpressionParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.signednum()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 73
                self.match(ArithmeticExpressionParser.LPAREN)
                self.state = 74
                self.expr(0)
                self.state = 75
                self.match(ArithmeticExpressionParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.match(ArithmeticExpressionParser.STRING)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 78
                self.match(ArithmeticExpressionParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(ArithmeticExpressionParser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(ArithmeticExpressionParser.INTEGER, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = ArithmeticExpressionParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignednumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def number(self):
            return self.getTypedRuleContext(ArithmeticExpressionParser.NumberContext,0)


        def sign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithmeticExpressionParser.SignContext)
            else:
                return self.getTypedRuleContext(ArithmeticExpressionParser.SignContext,i)


        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_signednum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignednum" ):
                listener.enterSignednum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignednum" ):
                listener.exitSignednum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignednum" ):
                return visitor.visitSignednum(self)
            else:
                return visitor.visitChildren(self)




    def signednum(self):

        localctx = ArithmeticExpressionParser.SignednumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_signednum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 83
                self.sign()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(ArithmeticExpressionParser.ADD, 0)

        def SUB(self):
            return self.getToken(ArithmeticExpressionParser.SUB, 0)

        def getRuleIndex(self):
            return ArithmeticExpressionParser.RULE_sign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSign" ):
                listener.enterSign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSign" ):
                listener.exitSign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign" ):
                return visitor.visitSign(self)
            else:
                return visitor.visitChildren(self)




    def sign(self):

        localctx = ArithmeticExpressionParser.SignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_sign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        self._predicates[4] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




