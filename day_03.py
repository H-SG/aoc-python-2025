from pathlib import Path


def get_max_num_recursively(batteries: str, num_digits: int = 12) -> None | str:
    unique_digits: set[str] = set(batteries)
    sorted_unique_digits: list[str] = sorted(unique_digits)
    sorted_unique_digits.reverse()

    # iterate through digits from largest to smallest
    for unique_digit in sorted_unique_digits:
        # this is our last number, so whatever is biggest we immediately return
        if num_digits == 1:
            return unique_digit

        # get first instance of the current digit
        first_index: int = batteries.index(unique_digit)

        # get remaining batteries after the current digit and their count
        remaining_batteries: str = batteries[first_index + 1 :]
        num_remaining_batteries: int = len(remaining_batteries)

        # if the number of batteries is less than the remaining digits then this is not a valid path
        if num_remaining_batteries < num_digits - 1:
            continue

        next_digits: None | str = get_max_num_recursively(
            remaining_batteries, num_digits - 1
        )

        # not a valid path
        if next_digits is None:
            continue

        return f"{unique_digit}{next_digits}"

    return None


# first go, which was built into recursive version
# def get_max_pair(batteries: str) -> int:
#     unique_digits: set[str] = set(batteries.strip())
#     sorted_unique_digits: list[int] = [int(x) for x in sorted(unique_digits)]
#     sorted_unique_digits.reverse()

#     for unique_digit in sorted_unique_digits:
#         first_index: int = batteries.index(str(unique_digit))

#         remaining_digits: set[str] = set(batteries[first_index + 1 :].strip())
#         if len(remaining_digits) > 0:
#             return int(f"{unique_digit}{max([int(x) for x in remaining_digits])}")


def main(
    instructions: Path = Path("data/day03test.txt"),
):
    # load the instructions which are one line
    with open(instructions, "r") as f:
        instruction_lines: list[str] = f.readlines()

    p1_sum: int = 0
    p2_sum: int = 0

    for instruction in instruction_lines:
        biggest_bat_p1: str | None = get_max_num_recursively(instruction.strip(), 2)
        biggest_bat_p2: str | None = get_max_num_recursively(instruction.strip(), 12)

        if biggest_bat_p1 is None:
            raise ValueError

        if biggest_bat_p2 is None:
            raise ValueError

        p1_sum += int(biggest_bat_p1)
        p2_sum += int(biggest_bat_p2)

    print(f"Day 2 - Part 1: {p1_sum}")
    print(f"Day 2 - Part 2: {p2_sum}")


if __name__ == "__main__":
    main()
    main(instructions=Path("data/day03prod.txt"))
