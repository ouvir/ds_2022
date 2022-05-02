from List_node import ListNode
class LinkedListBasicPlus:
    # python 에서는 구조체 반납 안해도 자동으로 해줌
    def __init__(self):
        self.__head = None
        self.__numItems = 0
    def __getNode(self, i:int):
        #연결리스트의 i번 노드 알려주기
        curr = self.__head # 0번 노드 시작
        for index in range(i):
            curr = curr.next
        return curr
    def __findNode(self, x):
        #연결리스트에서 x값의 위치 알려주기
        prev = self.__head # prev = 0번 노드
        curr = prev.next   # curr = 1번 노드
        if prev.item == x:
            return(None,prev)
        while curr != None:
            if curr.item == x:
                return (prev,curr)
            else:
                prev = curr
                curr = curr.next
        return (None,None)

# 연결 리스트에 원소 삽입하기(더미 헤드를 두는 대표 버전)
    def insert(self, i:int , newItem):
        if i == 0:
            newNode = ListNode(newItem,self.__head)
            self.__head = newNode
            self.__numItems += 1
        elif i > 0 and i<=self.__numItems:
            prev = self.__getNode(i-1)
            newNode = ListNode(newItem,prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index",i,": out of bound in insert()")
            #에러 처리
    def append(self,newItem):
        if self.__numItems == 0:
            newNode = ListNode(newItem , None)
            self.__head = newNode
            self.__numItems += 1

        else:
            prev = self.__getNode(self.__numItems -1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
# 연결 리스트의 원소 삭제하기
    def pop(self, i:int):
        if i==0:
            curr = self.__head
            self.__head = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        elif (i>0 and i <= self.__numItems-1):
            prev = self.__getNode(i-1)
            curr = prev.next
            prev.next = curr.next
            retItem = curr.item
            self.__numItems -= 1
            return retItem
        else:
            return None
    def remove(self, x):
        (prev, curr) = self.__findNode(x)
        if curr != None:
            if prev == None:
                self.__head = curr.next
                self.__numItems -= 1
                return x
            else:
                prev.next = curr.next
                self.__numItems -= 1
                return x
        else:
            return None
# 조회
    def get(self, i:int):
        if self.isEmpty():
            return None
        if (i>=0 and i <= self.__numItems-1):
            return self.__getNode(i).item
        else:
            return None
    def index(self,x):
        curr = self.__head #0번 노드 지정
        for index in range(self.__numItems):
            if curr.item == x: return index
            else: curr = curr.next
        return None
# 기타
    def isEmpty(self): # bools
        return self.__numItems == 0   
    def size(self):
        return self.__numItems
    def clear(self):
        self.__head = None
        self.__numItems = 0
    def count(self,x):
        cnt = 0
        curr = self.__head # 0번 노드
        while curr != None:
            if curr.item == x:
                cnt+=1
            curr = curr.next
        return cnt
    def extend(self,a): #a는 self와 같은 타입
        for index in range(a.size()):
            self.append(a.get(index))
    def copy(self):
        a = LinkedListBasicPlus()
        for index in range(self.__numItems):
            a.append(self.get(index))
        return a
    def reverse(self):
        a = LinkedListBasicPlus()
        for index in range(self.__numItems):
            a.insert(0, self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))
    def sort(self):
        a= []
        for index in range(self.__numItems):
            a.append(self.get(index))
        a.sort()
        self.clear()
        for index in range(len(a)):
            self.append(a(index))
    def printList(self):
        curr = self.__head #0번 노드
        while curr != None:
            print(curr.item, end = ' ')
            curr = curr.next
        print()