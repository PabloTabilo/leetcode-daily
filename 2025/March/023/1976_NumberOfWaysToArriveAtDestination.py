import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for r in roads:
            u : int = r[0]
            v : int = r[1]
            t : int = r[2]
            adj[u].append((v, t))
            adj[v].append((u, t))
        
        INF = int(1e9 * 300)
        MOD = int(1e9 + 7)
        mn = INF
        dist = [INF] * n
        vis = [False] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        h = [(0,0)]
        heapq.heapify(h)
        while h:
            cost, node = heapq.heappop(h)
            #print(f"node, cost = {node}, {cost}")
            if(cost > dist[node]):
                continue
            for x in adj[node]:
                neigh, w = x
                if(dist[neigh] > (w + cost)):
                    dist[neigh] = w + cost
                    ways[neigh] = ways[node] % MOD
                    heapq.heappush(h, (dist[neigh], neigh))
                elif dist[neigh] == (w + cost):
                    ways[neigh] = (ways[neigh] % MOD + ways[node] % MOD) % MOD
            #print(f"dist = {dist}")
            #print(f"ways = {ways}")
        return ways[n-1]