#!/usr/bin/python3
"""The Function."""


def cell_nbr_water(grid, row, col):
    """The number for surround water"""
    water_num = 0

    if row <= 0 or not grid[row - 1][col]:
        water_num += 1
    if row >= len(grid) - 1 or not grid[row + 1][col]:
        water_num += 1
    if col <= 0 or not grid[row][col - 1]:
        water_num += 1
    if col >= len(grid[row]) - 1 or not grid[row][col + 1]:
        water_num += 1

    return water_num


def island_perimeter(grid):
    """Perimeter for island described."""
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                perimeter += cell_nbr_water(grid, row, col)

    return perimeter

