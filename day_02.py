from pathlib import Path


def get_factors_of_number_length(number: int) -> list[int]:
    factors: list[int] = []

    number_length: int = len(str(number))

    for i in range(1, number_length):
        if number_length % i == 0:
            factors.append(i)

    return factors


def is_repeating(subgroup_lengths: list[int], id_as_str: str) -> bool:
    for subgroup_length in subgroup_lengths:
        substring: str = id_as_str[:subgroup_length]

        if id_as_str.count(substring) == len(id_as_str) / subgroup_length:
            return True

    return False


def main(
    instructions: Path = Path("data/day02test.txt"),
):
    # load the instructions which are one line
    with open(instructions, "r") as f:
        instruction_line: str = f.read()

    # unpack the instructions into tuple pairs
    id_ranges: list[tuple[int, int]] = [
        (int(x.split("-")[0]), int(x.split("-")[1]))
        for x in instruction_line.split(",")
    ]

    # part 1 var
    sum_invalid_ids: int = 0

    # part 2 var
    sum_invalid_ids_p2: int = 0

    for id_range in id_ranges:
        for id in range(id_range[0], id_range[1] + 1):
            id_as_str: str = str(id)
            num_digits: int = len(id_as_str)

            # an uneven number of digits cannot have a sequence repeated exactly twice
            if num_digits % 2 != 0:
                continue

            substring: str = id_as_str[: num_digits // 2]

            if id_as_str.count(substring) == 2:
                sum_invalid_ids += id

        for id in range(id_range[0], id_range[1] + 1):
            id_as_str: str = str(id)
            num_digits: int = len(id_as_str)

            # if there is only one digit, we cannot have any repetitions
            if num_digits == 1:
                continue

            distinct_chars: set[str] = set(id_as_str)

            # if there is only one distinct char we've hit the trivial case
            if len(distinct_chars) == 1:
                sum_invalid_ids_p2 += id
                continue

            # check how many subgroups of digits are possible for the number
            subgroup_lengths: list[int] = get_factors_of_number_length(id)

            # if the length of the number is prime, no subgroups are possible and we've already tested the case of
            # repeating digits
            if len(subgroup_lengths) == 1:
                continue

            # we might have multiple repeating subgroups, in which case we just want to count the first instance of it
            if is_repeating(subgroup_lengths, id_as_str):
                sum_invalid_ids_p2 += id

    print(f"Day 2 - Part 1: {sum_invalid_ids}")
    print(f"Day 2 - Part 2: {sum_invalid_ids_p2}")


if __name__ == "__main__":
    main()
    main(instructions=Path("data/day02prod.txt"))
