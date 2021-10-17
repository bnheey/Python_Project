
class Bfs:
    graph = [
        # component 1
        [1, 2],
        [0],
        [0],

        # component 2
        [4],
        [3],

        # component 3
        [7],
        [7],
        [5, 6, 8],
        [7, 9],
        [8]
    ]

    flag = [False] * len(graph)

    def bfs(self, s, flag):
        queue = []

        flag[s] = True
        queue.append(s)

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for i in self.graph[v]:
                if not flag[i]:
                    queue.append(i)
                    flag[i] = True
        print()


    def connected(self):
        i = 1
        flag1 = self.flag
        for idx in flag1:
            flag1[idx] = False
        for idx in range(0, len(flag1)):
            if(flag1[idx] == False):
                print("Component %d :" %i , end=' ')
                i += 1
                self.bfs(idx, flag1)


if __name__ == "__main__":
    bfs = Bfs()
    bfs.connected()
