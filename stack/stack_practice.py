#연습문제 2번-> 리스트 맨앞이 top이 되게 구현
class ListStack_2:
    def __init__(self):
        self.__stack =[]

    def push(self, x):
        self.__stack.insert(0,x)

    def pop(self):
        return self.__stack.pop(0)

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.__stack[0]

    def isEmpty(self):
        return not bool(self.__stack)

    def popAll(self):
        self.__stack.clear()
    
    def printStack(self):
        print("Stack:", end=' ')
        for i in range(len(self.__stack)):
            print("stack[",i,"]:",self.__stack[i])

#연습문제 3번-LinkedStack을 사용
from LinkedStack import *
    
#연습문제 5번-괄호 좌우균형?
# -> 1. (로 시작해서 )로 닫혀야함.
from ListStack import *
def parenBalance(s:str)->bool:
    stack = ListStack()
    for str in s:
        if str == '(': 
            stack.push(str)
        elif str == ')':
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    return stack.isEmpty() 
    # 마지막에 stack이 비어있으면 true, 채워져있으면 false


