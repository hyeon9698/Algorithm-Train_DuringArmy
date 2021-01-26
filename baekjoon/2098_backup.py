# dp[i][j] = 이미 방문한 도시들의 집합이 i이고 현재 있는 도시가 j 일때, 방문하지 않은 나머지 도시들을 모두 방문한 뒤 출발 도시로 돌아올 때 드는 최소 비용
def tsp(dists):
    N = len(dists)
    VISITED_ALL = (1 << N) - 1
    cache = [[None] * (1 << N) for _ in range(N)]
    INF = float('inf')
    
    def find_path(last, visited):
        if visited == VISITED_ALL:
            return dists[last][0] or INF

        if cache[last][visited] is not None:
            return cache[last][visited]
            
        tmp = INF        
        for city in range(N):
            if visited & (1 << city) == 0 and dists[last][city] != 0:
                tmp = min(tmp,
		 	  find_path(city, visited | (1 << city)) + dists[last][city])
        cache[last][visited] = tmp
        return tmp
                
    return find_path(0, 1 << 0)