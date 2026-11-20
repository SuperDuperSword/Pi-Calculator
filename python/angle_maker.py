import math  # Only sqrt, no trig or pi
from vector_2 import Vector2

SUBDIVISIONS = 16  # I think this value strikes a good balance between fast and accurate.

points: list[Vector2] = [Vector2(0, 1), Vector2(1, 0)]
curve_length = math.sqrt(2)  # For a diagonal line


def subdivide() -> None:
    extra_points: list[Vector2] = []
    for i in range(len(points) - 1):
        l_point = points[i]
        r_point = points[i + 1]
        new_point = Vector2.average(l_point, r_point).normalized()
        extra_points.append(new_point)

    index = 1
    for point in extra_points:
        points.insert(index, point)
        index += 2


def recalculate(subdiv_count=SUBDIVISIONS) -> None:
    """
    This isn't called when the 'module' is imported. You need to call it yourself.
    :param subdiv_count:
    :return:
    """

    global points
    points = [Vector2(0, 1), Vector2(1, 0)]

    for i in range(subdiv_count):
        subdivide()

    update_curve_length()


def update_curve_length() -> None:
    global curve_length
    curve_length = 0
    for i in range(len(points) - 1):
        left = points[i]
        right = points[i + 1]
        distance = left.distance(right)
        curve_length += distance


def main() -> None:
    recalculate(SUBDIVISIONS)
    distances = []
    for i in range(len(points) - 1):
        left = points[i]
        right = points[i + 1]
        distance = left.distance(right)
        print(distance)
        distances.append(distance)
    print()
    print(f"Margin of error = {max(distances) - min(distances)}")
    print(f"Curve length = {curve_length}")


if __name__ == "__main__":
    main()
