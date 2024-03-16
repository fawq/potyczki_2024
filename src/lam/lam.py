from collections import deque
import sys
from typing import Literal

def solve(cannon_height: dict[int, dict[str, int]], cannon_width: dict[int, dict[str, int]], unique_color_cannons: deque[tuple[Literal["R", "K"], int, str]]) -> list[tuple[Literal["R", "K"], int, str]]:
    path: list[tuple[Literal["R", "K"], int, str]] = []
    while len(unique_color_cannons) > 0 and len(cannon_height) > 0 and len(cannon_width) > 0:
        direction, index, color = unique_color_cannons.popleft()
        if direction == "R":
            for cannon_index, cannon_colors in cannon_width.items():
                cannon_colors[color] -= 1
                if cannon_colors[color] == 0:
                    cannon_colors.pop(color)
                    if len(cannon_colors) == 1:
                        unique_color_cannons.append(("K", cannon_index, next(iter(cannon_colors.keys()))))
            cannon_height.pop(index)
        elif direction == "K":
            for cannon_index, cannon_colors in cannon_height.items():
                cannon_colors[color] -= 1
                if cannon_colors[color] == 0:
                    cannon_colors.pop(color)
                    if len(cannon_colors) == 1:
                        unique_color_cannons.append(("R", cannon_index, next(iter(cannon_colors.keys()))))
            cannon_width.pop(index)
        path.append((direction, index, color))
    return path

def main() -> None:
    tokens: list[str] = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped: break
        tokens += stripped.split()
    tokens_iter = iter(tokens)

    height: int = int(next(tokens_iter))
    width: int = int(next(tokens_iter))
    cannon_height: dict[int, dict[str, int]] = {index: {} for index in range(height)}
    cannon_width: dict[int, dict[str, int]] = {index: {} for index in range(width)}

    unique_color_cannons: deque[tuple[Literal["R", "K"], int, str]] = deque()

    for row_index in range(height):
        row_value: str = next(tokens_iter)
        for column_index, char in enumerate(row_value):
            if char in cannon_height[row_index]:
                cannon_height[row_index][char] += 1
            else:
                cannon_height[row_index][char] = 1

            if char in cannon_width[column_index]:
                cannon_width[column_index][char] += 1
            else:
                cannon_width[column_index][char] = 1
            
    for row_index in range(height):
        colors: dict[str, int] = cannon_height[row_index]
        if len(colors) == 1:
            unique_color_cannons.append(("R", row_index, next(iter(colors.keys()))))

    for column_index in range(width):
        colors: dict[str, int] = cannon_width[column_index]
        if len(colors) == 1:
            unique_color_cannons.append(("K", column_index, next(iter(colors.keys()))))

    path: list[tuple[Literal["R", "K"], int, str]] = solve(cannon_height, cannon_width, unique_color_cannons)
    print(len(path))
    for direction, index, color in reversed(path):
        print(f"{direction} {index + 1} {color}")

if __name__ == "__main__":
    main()