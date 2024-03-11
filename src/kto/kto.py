import sys

NUMBER_OF_TASK: int = 18
NUMBER_OF_POINTS: int = 11

def get_winner(algosia_points: list[int], algosia_sum: int, bajtek_points: list[int], bajtek_sum: int) -> str:
    algosia_name: str = "Algosia"
    bajtek_name: str = "Bajtek"

    if algosia_sum == bajtek_sum:
        for algosia_point, bajtek_point in zip(algosia_points, bajtek_points):
            if algosia_point > bajtek_point:
                return algosia_name
            elif algosia_point < bajtek_point:
                return bajtek_name
        else:
            return "remis"
    return algosia_name if algosia_sum > bajtek_sum else bajtek_name

def main() -> None:
    algosia_points: list[int] = [0] * NUMBER_OF_POINTS
    bajtek_points: list[int] = [0] * NUMBER_OF_POINTS
    algosia_sum: int = 0
    bajtek_sum: int = 0

    tokens: list[str] = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped: break
        tokens += stripped.split()
    tokens_iter = iter(tokens)

    for _ in range(NUMBER_OF_TASK):
        points: int = int(next(tokens_iter))
        algosia_sum += points
        algosia_points[NUMBER_OF_POINTS - points - 1] += 1

    for _ in range(NUMBER_OF_TASK):
        points: int = int(next(tokens_iter))
        bajtek_sum += points
        bajtek_points[NUMBER_OF_POINTS - points - 1] += 1

    print(get_winner(algosia_points, algosia_sum, bajtek_points, bajtek_sum))

if __name__ == "__main__":
    main()