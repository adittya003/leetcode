class Solution:
    def checkrow(self, l1: list[str], i) -> bool:
        seen = set()
        for val in l1:
            if val != '.':
                if val in seen:
                    return False
                seen.add(val)
        return True

    def checkcoloumn(self, l2: list[str], i) -> bool:
        seen = set()
        for val in l2:
            if val != '.':
                if val in seen:
                    return False
                seen.add(val)
        return True

    def checksquare(self, l3: list[str]) -> bool:
        seen = set()
        for val in l3:
            if val != '.':
                if val in seen:
                    return False
                seen.add(val)
        return True

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            l1 = []
            for j in range(9):
                l1.append(board[i][j])
            X = self.checkrow(l1, i)
            if X == False:
                return X
            
        for i in range(9):
            l2 = []
            for j in range(9):
                l2.append(board[j][i])
            X = self.checkcoloumn(l2, i)
            if X == False:
                return X 

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.checksquare(subgrid):
                    return False
        
        return True
