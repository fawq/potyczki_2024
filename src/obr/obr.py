import sys

def pack_max(height: int, width: int, paints_size: list[int]) -> int:
    biggest_paint_size: int = paints_size[-1]
    height_fit: int = height // biggest_paint_size
    width_fit: int = width // biggest_paint_size

    count_max: int = height_fit * width_fit
    height_not_filled: int = height - height_fit * biggest_paint_size
    width_not_filled: int = width - width_fit * biggest_paint_size

    if height_not_filled > 0 and width_not_filled == 0:
        count_max += pack_max(height_not_filled, width, paints_size[:-1])
    elif height_not_filled == 0 and width_not_filled > 0:
        count_max += pack_max(height, width_not_filled, paints_size[:-1])
    elif height_not_filled > 0 and width_not_filled > 0:
        count_max += pack_max(height, width_not_filled, paints_size[:-1])
        count_max += pack_max(height_not_filled, width - width_not_filled, paints_size[:-1])
    return count_max

def main() -> None:
    tokens: list[str] = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped: break
        tokens += stripped.split()
    tokens_iter = iter(tokens)

    height: int = int(next(tokens_iter))
    width: int = int(next(tokens_iter))
    number_of_paints: int = int(next(tokens_iter))
    paints_size: list[int] = []
    for _ in range(number_of_paints):
        paints_size.append(int(next(tokens_iter)))

    if height % paints_size[0] != 0 or width % paints_size[0] != 0:
        print(-1)
    else:
        print(pack_max(height, width, paints_size))

if __name__ == "__main__":
    main()