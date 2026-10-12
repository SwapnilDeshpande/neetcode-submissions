class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        qu = collections.deque()
        fresh = 0
        time = 0

        # Traverse the grid and get the count of fresh oranges as well as positions of the rotten ones
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If I encounter a fresh orange increment the count of `fresh` by 1
                if grid[row][col] == 1:
                    fresh += 1
                # If I encounter a rotten orange log it's co-ordinates in `qu`
                if grid[row][col] == 2:
                    qu.append((row, col))
        
        # Traverse the graph via multi-source BFS while the `qu` is not empty and
        # while we have fresh oranges
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while qu and fresh > 0:
            
            # Pop the co-ords of rotten orange from the qu
            # for each co-ord in co-ords, traverse its adjecent nodes
            # if the adjecent nodes are within bounds of grid fresh, mark them as rotten, add them into qu
            # at the end of the while loop, increment the time

            for coord in range(len(qu)):
                row, col = qu.popleft()
                for dr, dc in directions:
                    adjRow = row + dr
                    adjCol = col + dc
                    if (adjRow in range(len(grid)) and  adjCol in range(len(grid[0])) and grid[adjRow][adjCol]== 1):
                        grid[adjRow][adjCol] = 2
                        qu.append((adjRow, adjCol))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

