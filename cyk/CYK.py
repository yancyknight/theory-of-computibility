class CYK:

    G = {
        'S': ['D1 C'],
        'B': ['Cb Cb', 'b'],
        'C': ['B D1', 'c'],
        'A': ['a'],
        'Cb': ['b'],
        'Cc': ['c'],
        'D1': ['A B'],
    }

    def isInRHS(self, x):
        retVal = []
        for lhs, rhs in self.G.iteritems():
            for v in rhs:
                if x == v:
                    retVal.append(lhs)
        return retVal

    def isInCFL(self, x):
        n = len(x)
        D = [[[] for _ in xrange(n)] for _ in xrange(n)]

        for i, l in enumerate(x):
            D[0][i] = self.isInRHS(l)

        for l in xrange(2, n + 1):
            for s in xrange(1, n - l + 2):
                for k in xrange(1, l):
                    B = D[k - 1][s - 1]
                    C = D[l - k - 1][s + k - 1]
                    if B != [] and C != []:
                        for bb in B:
                            for cc in C:
                                D[l - 1][s - 1] += self.isInRHS(bb + ' ' + cc)
                    elif B != []:
                        for bb in B:
                            D[l - 1][s - 1] += self.isInRHS(bb)
                    elif C != []:
                        for cc in C:
                            D[l - 1][s - 1] += self.isInRHS(cc)
        return 'S' in D[n - 1][0]
