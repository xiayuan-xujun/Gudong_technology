class Bomb:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def distance(bomb1, bomb2):
    """计算两个炸弹之间的欧几里得距离"""
    return ((bomb1.x - bomb2.x) ** 2 + (bomb1.y - bomb2.y) ** 2) ** 0.5

def dfs(bomb, bombs, visited):
    """深度优先搜索，找出一个炸弹能引爆的最大数量"""
    count = 1  # 当前炸弹也算在内
    visited[bomb] = True  # 标记当前炸弹为已访问
    for b in bombs:
        if not visited[b] and distance(bomb, b) <= bomb.r:
            count += dfs(b, bombs, visited)
    return count

def max_bombs_exploded(bomb_list):
    """返回最多能引爆的炸弹数目"""
    max_count = 0
    bombs = {i: Bomb(x, y, r) for i, (x, y, r) in enumerate(bomb_list)}
    visited = {bomb: False for bomb in bombs.values()}
    
    for bomb in bombs.values():
        if not visited[bomb]:
            max_count = max(max_count, dfs(bomb, bombs.values(), visited))
    
    return max_count

# 示例
bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
print(max_bombs_exploded(bombs))  # 输出应为最多能引爆的炸弹数目