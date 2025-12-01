from pathlib import Path


def main(
    dial_position: int = 50,
    instructions: Path = Path("data/day01test.txt"),
    num_dial_values: int = 100,
):
    # part 1 solution var
    zero_instances: int = 0

    # part 2 solution var
    zero_passing_instances: int = 0

    # load instructions
    with open(instructions, "r") as f:
        instruction_lines: list[str] = f.readlines()

    # parse instructions
    for instruction_line in instruction_lines:
        direction: str = instruction_line[0]
        distance: int = int(instruction_line[1:])

        # each whole full rotation of the dial can be ignored and only tracked for zero passings, then we only need to
        # consider the remaining distance
        zero_passing_instances += distance // num_dial_values
        remaining_distance: int = distance % num_dial_values

        remaining_distance = (
            -remaining_distance if direction == "L" else remaining_distance
        )

        old_position: int = dial_position
        dial_position = (dial_position + remaining_distance) % num_dial_values

        # if the dial position is on zero, then we've moved exactly to zero without doing crossings, we track this
        # separately and don't want to consider this case in zero crossing conditions
        if dial_position != 0:
            # if we have a positive rotation, and the new dial position is smaller than the prior dial position, we've
            # had a zero crossing
            if remaining_distance > 0:
                if dial_position < old_position:
                    zero_passing_instances += 1

            # if we have a negative rotation, and the new dial position is larger than the prior dial position, we've
            # had a zero crossing, however, we need to have a special case here for if the old position was zero,
            # otherwise we will be counting zero crossings where none existed
            if remaining_distance < 0:
                if (dial_position > old_position) and (old_position != 0):
                    zero_passing_instances += 1

        # finally, count stopping on zero
        if dial_position == 0:
            zero_instances += 1

    print(f"Day 1 - Part 1: {zero_instances}")
    print(f"Day 1 - Part 2: {zero_passing_instances + zero_instances}")


if __name__ == "__main__":
    main()
    main(instructions=Path("data/day01prod.txt"))
