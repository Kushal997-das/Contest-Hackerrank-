class DisjSet:
    def __init__(self, n):
        # Constructor to create and
        # initialize sets of n items
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        self.t=0

        # Finds set of given item x

    def find(self, x):

        # Finds the representative of the set
        # that x is an element of
        if (self.parent[x] != x):
            # if x is not the parent of itself
            # Then x is not the representative of
            # its set,
            self.parent[x] = self.find(self.parent[x])

            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set

        return self.parent[x]

        # Do union of two sets represented

    # by x and y.
    def Union(self, x, y):

        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            self.t+=1
            return

        self.parent[xset]=yset


n=int(input())
ar=[int(i)-1 for i in input().strip().split(" ")]
d=DisjSet(n)
for i in range(n):
    if ar[i]!=i:
        d.Union(i,ar[i])
k=d.parent
c=0
for i in range(len(k)):
    if k[i]==i:
        c+=1
if d.t==c:
    print(c)
else:
    print(c-1)
