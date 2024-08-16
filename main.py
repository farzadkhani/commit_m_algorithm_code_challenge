def is_within_bounds(grid, x, y):
    """
    Check if the given indices are within the bounds of the grid.
    """
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def build_batch(x, y, grid):
    """
    Build a batch of apartments in the grid.
    """
    if is_within_bounds(grid, x, y):
        grid[x][y] = "b"
    else:
        return grid
    if is_within_bounds(grid, x + 1, y + 1):
        grid[x + 1][y + 1] = "r"
        grid[x][y] = "x"
        grid[x][y] = "g"
    else:
        if is_within_bounds(grid, x, y + 1):
            grid[x][y + 1] = "r"
            grid[x][y] = "x"
            grid[x][y] = "g"
        else:
            if is_within_bounds(grid, x + 1, y):
                grid[x + 1][y] = "r"
                grid[x][y] = "x"
                grid[x][y] = "g"
            else:
                grid[x][y] = "x"
                grid[x][y] = "r"
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if is_within_bounds(grid, i, j) and grid[i][j] == "0":
                grid[i][j] = "g"
    return grid


def build_apartments(m, n):
    """
    # Algorithm Challenge

    ## Problem

    We are presented with m * n grid which we have to build apartments in.
    We want to house the most number of residents possible in the grid.
    Actions are destroying and building one apartment and their conditions are as follows:

    - blue apartment which can only have one resident.
    - red apartment which can have 5 residents but at least one blue apartment must be present in it's neighboring squares during it's construction.
    - green apartment which can have 10 residents but at least one red apartment must be present in it's neighboring squares during it's construction.
    - destroying an apartment only needs an apartment to be present in the square.

    ## Input

    m and n separated by space.

    ```math

    0 < m < 10^5
    0 < n < 10^5
    ```

    ## Output

    series of actions and finalized grid

    ```
    x y b # for building blue at x y
    x y r # for building red at x y
    x y g # for building green at x y
    x y x # for destroying existing building at x y
    -- # separate instructions from finalized grid
    ```

    ## Example

    input:

    ```
    3 3
    ```

    output:

    ```
    0 0 b
    1 1 r
    0 0 x
    0 0 g
    0 1 g
    0 2 g
    1 0 g
    1 2 g
    2 0 g
    2 1 g
    2 2 g
    --
    g g g
    g r g
    g g g
    ```

    ## Scoring

    each instruction decrease score.
    invalid instruction or not matching the final grid will automatically set score to 0.
    each resident in grid increasing the score
    ALgorithm.md
    Displaying ALgorithm.md.
    """

    # Generate a grid with all zeros
    grid = [["0" for _ in range(n)] for _ in range(m)]

    # Build apartments in the grid with batch of 3
    for item in range(0, n, 3):
        for i in range(0, m, 3):
            grid = build_batch(i, item, grid)

    for item in grid:
        print(" ".join(item))


if __name__ == "__main__":
    build_apartments(5, 7)
