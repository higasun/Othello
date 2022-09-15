dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

GRID_LEN = 8
DISK2COLOR = {'Dark': 1, 'Light': -1}

class Player:
    def __init__(self, disk: str) -> None:
        self.count = 0
        self.disk = disk
        self.color = DISK2COLOR[disk]

class Board:
    def __init__(self) -> None:
        self.grid = [[0]*GRID_LEN for _ in range(GRID_LEN)]

        self.grid[GRID_LEN//2 - 1][GRID_LEN//2 - 1] = -1
        self.grid[GRID_LEN//2][GRID_LEN//2] = -1
        self.grid[GRID_LEN//2 - 1][GRID_LEN//2] = 1
        self.grid[GRID_LEN//2][GRID_LEN//2 - 1] = 1

    def place(self, x, y, color): # 返り値を「ひっくり返って増えた枚数」としても良いかも
        if self.can_place(x, y, color):
            self.grid[x][y] = color
            self.reverse()
            return True
        else:
            return False

    def can_place(self, x: int, y: int, color: int) -> bool:
        if not(0 <= x < GRID_LEN) or not (0 <= y < GRID_LEN) \
            or self.grid[x][y] != 0:
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

    def reverse(self, x, y, color):
        pass


class Game:
    def __init__(self) -> None:
        self.dark_player = Player('Dark')
        self.light_player = Player('Light')
        self.board = Board()

        self.player = self.dark_player
        self.next_player = self.light_player

    def play(self):
        self.show()
        while True:
            x, y = map(int, input("{}'s Turn: ".format(game.player.disk)).split())
            self.place(x, y)
            self.show()
    
    def place(self, x, y) -> None:
        if self.board.place(x, y, self.player.color):
            self.player, self.next_player = self.next_player, self.player
        else:
            print('You cannot place a disk there.')
            
    def show(self):
        label = {-1: 'o', 0: '-', 1: 'x'}
        for i in range(GRID_LEN):
            l = [label[x] for x in self.board.grid[i]]
            print(''.join(l))
        print('\n')

    def end(self):
        if self.dark_player.count > self.light_player.count:
            return 'Dark WIN ---- Light LOSE'
        elif self.dark_player.count < self.light_player.count:
            return 'Dark LOSE ---- Light WIN'
        else:
            return 'DRAW'

game = Game()
game.play()