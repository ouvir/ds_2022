def mergeSort(A, p:int,r:int):
    if p<r:
        q = (p+r) //2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p:int,q:int,r:int):
    i = p; j = q+1; t = 0
    tmp = [0 for i in range(len(A))]
    tmp2 = [0 for i in range(len(A))]
    while i <= q and j <= r:
        if A[i][1] > A[j][1]: 
        # >= 기호를  > 로 바꿔 줌!
            tmp[t] = A[i][1]
            tmp2[t] = A[i][0]; t+=1; i+=1
        else:
        # 비교 값이 같을 때, 인덱스가 뒤인 값을 먼저 넣는다 
        # -> 처음 key 값들은 내림차순으로 정렬되어있음.
        # -> key 값이 내림차순 정렬됨.
            tmp[t] = A[j][1]
            tmp2[t] = A[j][0]; t+=1; j+=1
    while i <= q:
        tmp[t] = A[i][1]
        tmp2[t] = A[i][0]; t+=1; i+=1
    while j <= r:
        tmp[t] = A[j][1]
        tmp2[t] = A[j][0]; t+=1; j+=1
    i = p; t = 0
    while i <= r:
        A[i][1] = tmp[t]
        A[i][0] = tmp2[t]; t += 1;i += 1

def page_sort_count(input_file):
    
    data_file = open(input_file)
    A = dict()
    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn in A.keys():
            A[lpn] += 1
        else:
            A[lpn] = 1
    
    for i in range(10):
        print(list(A.keys())[i])
    print()
    
    # 방법 1. sorted 사용
    B = sorted(A.items(), key=(lambda x: (x[1],x[0])), reverse= True)
    # sorted에 key를 lambda함수로 인자 2개를 준다
    # -> 먼저 x[1] 인 value 값(호출 횟수)로 정렬,
    # -> 그 뒤에 서로 같은 value 값 끼리는 x[0](페이지 넘버)로 정렬
    # -> reverse로 뒤집으면, 호출횟수가 클수록 앞에 정렬,
    #    같은 호출 횟수 일땐, 페이지 넘버가 클 수록 앞에 정렬 됨. 

    # 방법 2. mergeSort 사용
    C = [[int(i[0]),i[1]] for i in A.items()] 
    # 사전 처리로 [[key,value],...]형태의 2차원 배열 생성
    mergeSort(C,0,len(A)-1)

    print("방법1")
    for i in range(10):
        print(B[i][0],B[i][1])
    print()

    print("방법2")
    for i in range(10):        
        print(C[i][0],C[i][1])
    print()
    
    
if __name__ == "__main__" :
    page_sort_count("linkbench_short.trc")
    
