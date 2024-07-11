class DisjointSet:
    def __init__(self, size) -> None:
        self.parent = [idx for idx in range(size)]
        self.rank = [0]*size

    def find(self, idx):
        tdx = idx
        while self.parent[tdx] != tdx:
            tdx = self.parent[tdx]
        while idx != tdx:
            self.parent[idx], idx = tdx, self.parent[idx]
        return tdx

    def union(self, idx, jdx):
        iparent, jparent = self.find(idx), self.find(jdx)
        if self.rank[iparent] > self.rank[jparent]:
            self.parent[jparent] = iparent
        elif self.rank[iparent] < self.rank[jparent]:
            self.parent[iparent] = jparent
        else:
            self.parent[jparent] = iparent
            self.rank[iparent] += 1


if __name__ == '__main__':
    ds = DisjointSet(10)
    print('union(0,6)'), ds.union(0, 6)
    print('union(3,6)'), ds.union(3, 6)
    print('union(3,8)'), ds.union(3, 8)
    print('union(0,4)'), ds.union(0, 4)
    print('parent(6)', ds.find(6))
    print('parent(4)', ds.find(4))
    print('parent(9)', ds.find(9))
    print('disjoint-set(parents)', ds.parent)

