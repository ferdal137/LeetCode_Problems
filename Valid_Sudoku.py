class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        a = []
        b = []
        c = []
        txt = []
        bol = True
        count = 0
        c3 = 0

        #Check the rows
        '''for row in board:
            for cell in row:
                if cell == ".":
                    pass
                else:
                    a.append(cell)
            print(a)
            if len(a)!=len(set(a)):
                bol = False
            a = []'''

        #Check the columns
        '''for i in range(len(board[0])):
            for row in board:
                if row[count] == ".":
                    pass
                else:
                    b.append(row[count])
            count += 1
            if len(b)!=len(set(b)):
                bol = False
            b = []'''

        #Check the 3x3 squares
        #for i in range(9):
        for row in board:
            

        return bol
