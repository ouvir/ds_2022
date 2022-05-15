# 일반(selection,bubble,insertion)
#1. 선택정렬 selectionSort
def selectionSort(A):
    for last in range(len(A)-1,0,-1):
        k= theLargest(A,last) # 큰 수 찾기
        A[k],A[last] = A[last],A[k] # 맨 마지막 고정

def theLargest(A, last :int) -> int:
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest =i
    return largest

#2. 버블정렬 bubbleSort
def bubbleSort(A):
    for numElements in range(len(A),0,-1):
        for i in range(numElements-1):
            if A[i] > A[i+1]:
                A[i],A[i+1] = A[i+1],A[i]

#3. 삽입정렬 insertionSort
def insertionSort(A):
    for i in range(1,len(A)):
        loc = i-1
        newItem = A[i]
        while loc >=0 and newItem < A[loc]:
            A[loc+1] = A[loc]
            loc -=1
        A[loc+1] = newItem

# 고급(merge,,heap)
#1. 병합정렬 mergeSort
def mergeSort(A, p:int,r:int):
    if p<r:
        q = (p+r) //2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p:int,q:int,r:int):
    i = p; j = q+1; t = 0
    tmp = [0 for i in range(len(A))]
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]; t+=1; i+=1
        else:
            tmp[t] = A[j]; t+=1; j+=1
    while i <= q:
        tmp[t] = A[i]; t+=1; i+=1
    while j <= r:
        tmp[t] = A[j]; t+=1; j+=1
    i = p; t = 0
    while i <= r:
        A[i] = tmp[t]; t += 1;i += 1

#2. 퀵 정렬 quickSort
def quickSort(A,p:int,r:int):
    if p<r:
        q = partition(A,p,r)    # 분할
        quickSort(A,p,q-1)      # 왼쪽 리스트
        quickSort(A,q+1,r)      # 오른쪽 리스트

def partition(A,p:int,r:int)->int:
    x = A[r] # 기준-> 맨 끝을 기준으로 둠
    i = p-1  # i는 1구역 끝지점
    for j in range(p,r): # j는 3구역 시작 지점
        if A[j] < x:
            i += 1
            A[i],A[j] = A[j],A[i]   # 교환
    A[i+1],A[r] = A[r],A[i+1]       # 기준 원소와 2구역 첫원소 교환
    return i+1
    
#3. 힙정렬 heapSort
def heapSort(A):
    buildHeap(A)
    for last in range(len(A)-1,0,-1):
        A[last],A[0] = A[0],A[last]
        percolateDown(A, 0, last-1)

def buildHeap(A):
    for i in range((len(A)-2)//2,-1,-1):
        percolateDown(A,i,len(A)-1)

def percolateDown(A,k:int,end:int):
    left = 2*k + 1 #왼쪽 자식 노드
    right = 2*k + 2#오른쪽 자식 노드
    if left <= end: 
    # 왼쪽 자식 인덱스가 리스트범위를 넘지 않을 때,
        if (right <=len(A)-1 and A[left] < A[right]):
        # 오른쪽 자식 인덱스가 리스트범위 안넘고,
        # 오른쪽이 왼쪽보다 클 때
            left = right 
            # 둘 중 더 큰 값의 인덱스를 i와 바꿀거야
        if A[k] < A[left]:
            A[k], A[left] = A[left], A[k]
            percolateDown(left) # 재귀
#4. 쉘 정렬 shellSort
#pass

# 특수
# 1. 계수 정렬 Counting Sort
def countingSort(A) -> list:
    k = max(A)
    C = [0 for _ in range(k+1)]
    for j in range(len(A)):
        C[A[j]] += 1 # 카운팅
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1] 
        # 카운팅 리스트 원소마다, 자신 이전 원소들의 합을 더해줌
    B = [0 for _ in range(len(A))] # 새 리스트 제작
    for j in range(len(A)-1,-1,-1):
        # 맨 뒤 원소부터, 원소가 들어갈 범위의 맨 뒤 위치로 들어감
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1 
        # 맨 뒤 위치 사용했으니, 그 다음 위치
    return B

# 2. 기수 정렬 Radix Sort
import math

def radixSort(A):
    maxValue = max(A)
    numDigits = math.ceil(math.log10(maxValue)) #자릿수 계산
    bucket = [[]for _ in range(10)] #0~9 까지의 공간 제작
    for i in range(numDigits):
        for x in A:
            y = (x//10**i)%10 # 이번 정렬 자릿수 y
            bucket[y].append(x) # 공간에 담아주기
        A.clear()
        for j in range(10):
            A.extend(bucket[j])
            bucket[j].clear()

# 3. 버킷 정렬 Bucket Sort
# pass
