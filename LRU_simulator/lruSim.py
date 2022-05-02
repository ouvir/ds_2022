#20192889 김경훈
from circularDoublyLinkedList import *
def do_sim(cache_slots):
    memory = CircularDoublyLinkedList() #연결리스트 생성
    cache_hit = 0
    tot_cnt = 0

    data_file = open("C:\\Users\\kilhy\\projects\\ds_2022-main\\linkbench_short.trc")

    for line in data_file.readlines():
        lpn = line.split()[0] #lpn -> workload

        tot_cnt += 1 # 불러온 workload 수
        lpn_index = memory.index(lpn)
        if lpn_index < 0: 
        # memory 안에 lpn 없음 -> miss
            memory.insert(0,lpn)
            if memory.size() > cache_slots:# memory 초과
                memory.pop()# 마지막 값 삭제
        else: 
        # memory 안에 lpn 존재-> hit
            cache_hit += 1
            memory.insert(0,memory.pop(lpn_index))
            #lpn 인덱스확인후 삭제후 0번째에 다시 넣어줌.
    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)
if __name__ == "__main__":

    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)
