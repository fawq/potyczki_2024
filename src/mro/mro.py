def get_index_of_change(lp_chain: str) -> int:
    number_of_ls: int = 0
    for char in lp_chain:
        if char == 'L':
            number_of_ls += 1
    return number_of_ls

def count_first_part(p_sum_prefix: list[int], lp_chain: str, index_of_change: int, result: list[int]) -> None:
    for index, char in enumerate(lp_chain[0 : index_of_change]):
        if index == 0:
            p_sum_prefix[index] = 1 if char == 'P' else 0
        else:
            p_sum_prefix[index] = p_sum_prefix[index - 1] + (1 if char == 'P' else 0)
        result[index] = 2 * p_sum_prefix[index] if char == 'L' else 2 * p_sum_prefix[index] - 1

def count_second_part(l_sum_prefix: list[int], lp_chain: str, index_of_change: int, size: int, result: list[int]) -> None:
    for index, char in enumerate(reversed(lp_chain[index_of_change : size])):
        if index == 0:
            l_sum_prefix[index] = 1 if char == 'L' else 0
        else:
            l_sum_prefix[index] = l_sum_prefix[index - 1] + (1 if char == 'L' else 0)
        result[size - index - 1] = 2 * l_sum_prefix[index] if char == 'P' else 2 * l_sum_prefix[index] - 1

def main() -> None:
    size: int = int(input())
    lp_chain: str = input()
    
    index_of_change: int = get_index_of_change(lp_chain)
    p_sum_prefix_first_part: list[int] = [0] * index_of_change
    l_sum_prefix_second_part: list[int] = [0] * (size - index_of_change)

    result: list[int] = [0] * size
    count_first_part(p_sum_prefix_first_part, lp_chain, index_of_change, result)
    count_second_part(l_sum_prefix_second_part, lp_chain, index_of_change, size, result)

    for number in result:
        print(number, end=" ")

if __name__ == "__main__":
    main()
