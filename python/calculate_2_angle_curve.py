import math  # Only for comparison with math.pi
import time

import angle_maker


def main() -> None:
    print()
    print("This program will calculate pi to any arbitrary precision.")
    print("math.pi is always greater than the calculation due to how it's calculated.")
    print("If you want, you can change the precision to whatever you want.")
    print(f"The default is {angle_maker.SUBDIVISIONS}, and the computation time grows exponentially with that number.")
    subd_string = input("If you don't enter anything, it will use that default. Please enter your desired precision: ")

    subd_count: int

    if subd_string.isdecimal():
        subd_count = int(subd_string)
    else:
        subd_count = angle_maker.SUBDIVISIONS

    original_time = time.monotonic()

    angle_maker.recalculate(subd_count)

    operation_time = time.monotonic() - original_time

    print()

    print(f"pi is calculated to be {angle_maker.curve_length * 2} with subdivision count of {subd_count}")
    print(f"math.pi = {math.pi}")
    print(f"The difference between the two is {math.pi - angle_maker.curve_length * 2}.")
    print(f"The operation took {round(operation_time * 1000)} milliseconds.")


if __name__ == "__main__":
    main()

# This is so much faster than the first method. And more accurate! That one seems biased to lower numbers.
