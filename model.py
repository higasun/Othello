dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

class Disk:
    def __init__(self, color) -> None:
        self.color = color

class Board:
    def __init__(self) -> None:
        self.grid = [[0]*8 for _ in range(8)]

    def can_put(self, x: int, y: int, color: int) -> bool:
        if self.grid[x][y] != 0:
            return False
        
        res = False
        for dir in range(8):
            if self._dfs_check(x, y, dir, color):
                return True
        return False

        
    def _dfs_check(self, x: int, y: int, dir: int, color: int, cnt=0) -> bool:
        if self.grid[x][y] != color:
            cnt += 1
            color *= -1
        if cnt >= 2:
            return True
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx <= 7 and 0 <= ny <= 7 and self.grid != 0:
            self._dfs_check(nx, ny, dir, color, cnt)
        return False