from ast import arg
from turtle import right


class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A=[]

    def __percolateUp(self, i:int):
        parent = (i-1)//2
        if i>0 and self.__A[i] > self.__A[parent]:
            # i가 root노드가 아니고, i의 부모요소보다 값이 클 때
            self.__A[i],self.__A[parent] = self.__A[parent], self.__A[i]
            # 부모 노드와 자식노드 값 교환
            self.__percolateUp(parent) #재귀

    def __percolateDown(self, i:int):
        left = 2*i + 1 #왼쪽 자식 노드
        right = 2*i + 1#오른쪽 자식 노드
        if (left <= len(self.__A)-1): 
        # 왼쪽 자식 인덱스가 리스트범위를 넘지 않을 때,
            if (right <=len(self.__A)-1 and self.__A[left] < self.__A[right]):
            # 오른쪽 자식 인덱스가 리스트범위 안넘고,
            # 오른쪽이 왼쪽보다 클 때
                left = right 
                # 둘 중 더 큰 값의 인덱스를 i와 바꿀거야
            if self.__A[i] < self.__A[left]:
                self.__A[i], self.__A[left] = self.__A[left], self.__A[i]
                self.__percolateDown(left) # 재귀

    def insert(self,x):
        self.__A.append(x) # 맨끝에 요소 넣고 
        self.__percolateUp(len(self.__A)-1) #스며올리기

    def deleteMax(self):
        if(not self.isEmpty()):
            max = self.__A[0] # 마지막요소 저장
            self.__A[0] = self.__A.pop() #마지막요소를 맨 위에 넣기
            self.__percolateDown(0)
            return max
        else:
            return None

    def max(self):
        return self.__A[0]
    
    def buildHeap(self):
        for i in range((len(self.__A)-2)//2,-1,-1):
            # 리프 노드의 부모노드 부터 루트까지 교환
            self.__percolateDown(i)

    def isEmpty(self) -> bool:
        return (len(self.__A) == 0)

    def clear(self):
        self.__A = []

    def size(self) ->int:
        return len(self.__A)
    
