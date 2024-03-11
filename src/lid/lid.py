import sys

def get_number_of_leaders(sorted_occurences: list[tuple[int, int]], occurences_size: int) -> int:
    min_number_of_leaders: int = 1
    leader_index: int = 0

    while True:
        leader: tuple[int, int] = sorted_occurences[leader_index]
        leader_occurences: int = leader[1]
        if occurences_size // 2 < leader_occurences:
            return min_number_of_leaders
        else:
            # Deleting of anty leaders
            partial_count: int = 0
            while partial_count < leader_occurences:
                left: int = leader_occurences - partial_count - 1
                anty_leader: tuple[int, int] = sorted_occurences[-1]
                anty_leader_occurences: int = sorted_occurences[-1][1]
                if anty_leader_occurences <= left:
                    partial_count += anty_leader_occurences
                    sorted_occurences.pop()
                    occurences_size -= anty_leader_occurences
                else:
                    sorted_occurences[-1] = (anty_leader[0], anty_leader_occurences - left)
                    occurences_size -= left
                    break
            
            # Deleting of leader
            occurences_size -= leader_occurences
            leader_index += 1
            min_number_of_leaders += 1

def main() -> None:
    occuernces: dict[int, int] = {}

    tokens: list[str] = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped: break
        tokens += stripped.split()
    tokens_iter = iter(tokens)

    occurences_size: int = int(next(tokens_iter))
    for _ in range(occurences_size):
        number = int(next(tokens_iter))
        if number in occuernces:
            occuernces[number] += 1
        else:
            occuernces[number] = 1
    
    sorted_occuernces = sorted(occuernces.items(), key=lambda item: item[1], reverse=True)
    print(get_number_of_leaders(sorted_occuernces, occurences_size))

if __name__ == "__main__":
    main()