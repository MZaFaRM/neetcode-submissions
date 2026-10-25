class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check_list = [[set() for i in range(9)] for i in range(3)]
        # check_list[0] vertical
        # check_list[1] horizontal
        # check_list[2] grid
        for i, r in enumerate(board):
            for j, v in enumerate(r):
                if v == ".":
                    continue

                v_grp = j
                if v in check_list[0][v_grp]:
                    return False
                else:
                    check_list[0][v_grp].add(v)

                h_grp = i
                if v in check_list[1][h_grp]:
                    return False
                else:
                    check_list[1][h_grp].add(v)
                    
                g_grp = (i // 3) * 3 + (j // 3)
                if v in check_list[2][g_grp]:
                    return False
                else:
                    check_list[2][g_grp].add(v)
        return True
                 

        