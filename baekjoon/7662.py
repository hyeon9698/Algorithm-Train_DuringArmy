import sys
import heapq
sys.stdin = open('input.txt', 'r')
for _ in range(int(input())):
    max_heap = []
    min_heap = []
    for _ in range(int(input())):
        val, num = input()
        if val == 'I':
            heapq.heappush(max_heap, num)
            heapq.heappush(min_heap, -num)
        elif val == 'D' and num > 0:
            try:
                heapq.heappop(max_heap)
            except:
                pass
        else:
            try:
                heapq.heappop(min_heap)
            except:
                pass