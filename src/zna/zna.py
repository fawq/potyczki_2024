import sys

def get_number_of_stamples(samples_per_city_values: list[int], number_of_people: int) -> int:
    number_of_stamples_per_person: int = 0
    for samples_in_city in samples_per_city_values:
        if samples_in_city >= number_of_people:
            number_of_stamples_per_person += (samples_in_city // number_of_people)
        else:
            break
    return number_of_stamples_per_person * number_of_people

def main() -> None:
    tokens: list[str] = []
    for line in sys.stdin:
        stripped = line.strip()
        if not stripped: break
        tokens += stripped.split()
    tokens_iter = iter(tokens)

    number_of_stamples: int = int(next(tokens_iter))
    samples_per_city: dict[int, int] = {}
    maximum_value_of_samples_per_city: int = 0

    for _ in range(number_of_stamples):
        token: int = int(next(tokens_iter))
        if token not in samples_per_city:
            samples_per_city[token] = 1
        else:
            samples_per_city[token] += 1
        
        maximum_value_of_samples_per_city = max(maximum_value_of_samples_per_city, samples_per_city[token])

    samples_per_city_values: list[int] = list(samples_per_city.values())
    samples_per_city_values.sort(reverse=True)

    for number_of_people in range(1, number_of_stamples + 1):
        if number_of_people > maximum_value_of_samples_per_city:
            print(" ".join(["0"] * (number_of_stamples - number_of_people + 1)))
            break
        else:
            print(get_number_of_stamples(samples_per_city_values, number_of_people), end=" ")

if __name__ == "__main__":
    main()