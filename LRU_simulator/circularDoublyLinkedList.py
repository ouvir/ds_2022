from bidirectNode import BidirectNode

class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    
#삽입
    def insert(self, i:int , newItem) -> None:
        if i>=0 and i<=self.__numItems:
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else: # 에러 처리
            print("index",i,": out of bound in insert()")
    def append(self, newItem) -> None:
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, prev.next)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1
        
# 삭제
    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        if (i>=0 and i <= self.__numItems -1):
            curr = self.getNode(i)
            retItem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return retItem
        else:
            return None
    def remove(self, x):
        curr = self.__findNode(x)
        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -=1
            return x
        else:
            return None

# 조회
    def get(self, *args):
        if self.isEmpty(): return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        if (i>=0 and i <= self.__numItems-1):
            return self.getNode(i).item
        else:
            return None
    def index(self,x) -> int:
        cnt = 0
        for element in self:
            if element == x: return cnt
            cnt += 1
        return -12345

# 기타
    def isEmpty(self) -> bool: # bools
        return self.__numItems == 0  
    def size(self) -> int:
        return self.__numItems
    def clear(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
    def count(self,x) -> int:
        cnt = 0
        for element in self:
            if element ==x:
                cnt += 1
        return cnt
    def extend(self,a): #a는 소화가능한 모든 객체
        for element in a:
            self.append(element)
    def copy(self) -> "CircularDoublyLinkedList":
        a = CircularDoublyLinkedList()
        for element in self:
            a.append(element)
        return a
    def reverse(self):
        prev=self.__head; curr=prev.next; next=curr.next
        self.__head.next=prev.prev;self.__head.prev=curr
        for i in range(self.__numItems):
            curr.next = prev; curr.prev = next
            prev = curr; curr = next; next = next.next
    def sort(self):
        a= []
        for element in self:
            a.append(element)
        a.sort()
        self.clear()
        for element in a:
            self.append(element)
    def __findNode(self, x) -> BidirectNode:
        curr = self.__head.next #0번노드
        while curr != self.__head:
            if curr.item == x: return curr
            else: curr = curr.next
        return None 
    def getNode(self, i:int) -> BidirectNode:
        #연결리스트의 i번 노드 알려주기
        curr = self.__head # 더미 헤드, index = -1
        for index in range(i+1):
            curr = curr.next
        return curr    
    def printList(self) -> None:
        for element in self:
            print(element, end = " ")
        print()
    def __iter__(self): # generating iterator and return
        return CircularDoublyLinkedListIterator(self)

class CircularDoublyLinkedListIterator:
    def __init__(self,alist):
        self.__head = alist.getNode(-1) #더미 헤드
        self.iterPosition = self.__head.next #0번 노드
    def __next__(self):
        if self.iterPosition == self.__head: #순환 끝
            raise StopIteration
        else: #현재원소 리턴하며 다음원소 이동
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item