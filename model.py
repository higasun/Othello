dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

GRID_LEN = 8
COLOR_ID = {'dark': 1, 'light': -1}

class Player:
    def __init__(self, color: str) -> None:
        self.count = 0
        self.color = COLOR_ID[color]

class Board:
    def __init__(self) -> None:
        self.grid = [[0]*GRID_LEN for _ in range(GRID_LEN)]

        self.grid[GRID_LEN//2 - 1][GRID_LEN//2 - 1] = -1
        self.grid[GRID_LEN//2][GRID_LEN//2] = -1
        self.grid[GRID_LEN//2 - 1][GRID_LEN//2] = 1
        self.grid[GRID_LEN//2][GRID_LEN//2 - 1] = 1

    def can_put(self, x: int, y: int, color: int) -> bool:
        if self.grid[x][y] != 0:
            return False
        
        res = False
        for dir in range(8):
            if self._dfs_check(x, y, dir, color):
                return True
        return False

        
    def _dfs_check(self, x: int, y: int, dir: int, color: int, cnt=0) -> bool:
        if self.grid[x][y] != 0 and self.grid[x][y] != color:
            cnt += 1
            color *= -1
        if cnt >= 2:
            return True

        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < GRID_LEN and 0 <= ny < GRID_LEN and self.grid[nx][ny] != 0:
            if self._dfs_check(nx, ny, dir, color, cnt):
                return True
        return False

    def show(self):
        label = {-1: 'o', 0: '-', 1: 'x'}
        for i in range(GRID_LEN):
            l = [label[x] for x in self.grid[i]]
            print(''.join(l))


class Game:
    def __init__(self, you: Player, com: Player) -> None:
        self.you = you
        self.com = com

        if you.color == 1:
            self.player = you
            self.next_player = com
        else:
            self.player = com
            self.next_player = you
        
        self.board = Board()
    
    def place(self):
        self.player, self.next_player = self.next_player, self.player

    def end(self):
        if self.you.count > self.com.count:
            return 'WIN'
        elif self.you.count < self.com.count:
            return 'LOSE'
        else:
            return 'DRAW'


board = Board()
board.show()
print(board.can_put(4, 5, 1))