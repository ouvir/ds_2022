def quickSort(A,p:int,r:int):
    if p < r:
        q = partition(A,p,r)    # 분할
        quickSort(A,p,q-1)      # 왼쪽 리스트
        quickSort(A,q+1,r)      # 오른쪽 리스트
        
def partition(A,p:int,r:int)->int:
    A_item = list(A.values())
    print(A_item)
    x = A_item[r] # 기준-> 맨 끝을 기준으로 둠
    i = p-1  # i는 1구역 끝지점
    for j in range(p,r): # j는 3구역 시작 지점
        if A_item[j] < x:
            i += 1
            A_item[i],A_item[j] = A_item[j],A_item[i]        
    A_item[i+1],A_item[r] = A_item[r],A_item[i+1]       # 기준 원소와 2구역 첫원소 교환
    A = dict(A_item)
    return i+1

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
    
    quickSort(A,0,len(A)-1)
    
    for i in range(10):
        print(list(A.keys())[i])
    print()
    
    
if __name__ == "__main__" :
    page_sort_count("linkbench_short.trc")
       