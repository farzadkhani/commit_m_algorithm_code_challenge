# commit-m Algorithm code challenge


# Algorithm Challenge

## Problem

We are presented with m * n grid which we have to build apartments in.
We want to house the most number of residents possibe in the grid.
Actions are destroying and building one apartment and their conditions are as follows:

- blue apartment which can only have one resident.
- red apartment which can have 5 residents but at least one blue apartment must be present in it's neighboring squares during it's construction.
- green apartment which can have 10 residents but at least one red apartment must be present in it's neighboring squares during it's construction.
- destroying an apartment only needs an apartment to be present in the square.

## Input

m and n seperated by space.

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
-- # seperate instructions from finalized grid
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

# Run

python -m main
