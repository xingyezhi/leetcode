# coding=utf-8
__author__ = 'lenovo'
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board = [[board[i][j] for j in xrange(9)] for i in xrange(9)]
        a = [0] * 27
        b = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        c = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
        for i in xrange(9):
            for k in xrange(9):
                j = board[i][k]
                if j == '.':
                    b[i][k] = 0
                    continue
                a[i] |= 1<<int(j)
            for k in xrange(9):
                j = board[k][i]
                if j == '.':
                    continue
                a[9+i] |= 1<<int(j)
            for k in xrange(9):
                j = board[i/3*3+k/3][i%3*3+k%3]
                if j == '.':
                    continue
                a[18+i] |= 1<<int(j)
        def f(x, y, k):
                        for i in xrange(0, 9):
                            if b[x][i] == 0:
                                r = s(x, i)
                                if r is True:
                                    return r
                                else:
                                    return False
                        for i in xrange(0, 9):
                            if b[i][y] == 0:
                                r = s(i, y)
                                if r is True:
                                    return r
                                else:
                                    return False
        def s(x, y):
            for k in xrange(0,9):
                if a[x] & (2<<k) == 0 and a[9+y] & (2<<k) == 0 and a[18+x/3%3+y/3] & (2<<k) == 0:
                    board[x][y] = str(k+1)
                    a[x] |= 2<<k
                    a[9+y] |= 2<<k
                    a[18+x/3%3+y/3] |= 2<<k
                    b[x][y] = 1
                    if b == c:
                        return True
                    if f(x, y, k) is True:
                        return True
                    a[x] &=~ 2<<k
                    a[9+y] &=~ 2<<k
                    a[18+x/3%3+y/3] &=~ 2<<k
                    b[x][y] = 0
            return False
        print s(0,0)


if __name__ == '__main__':
    a=7
    b=2
    print a+b
    print a|b
    # s = Solution()
    # s.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])