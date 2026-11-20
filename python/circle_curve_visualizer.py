import matplotlib.pyplot as plt
import angle_maker

IGNORE_45_DEGREE_ANGLE = True
SHOW_ONLY_FINAL = True
SHOW_CIRCLE = True


def main() -> None:
	global IGNORE_45_DEGREE_ANGLE
	global SHOW_ONLY_FINAL
	global SHOW_CIRCLE

	print("This program will show a circle in various degrees of precision.")
	print("You may change that precision or hide some of the 'unwanted' precisions.")
	IGNORE_45_DEGREE_ANGLE = True if input("Do you want to hide the lowest degree of precision (the 45 degree angle)? (y/n) ") == "y" else False
	SHOW_ONLY_FINAL = True if input("Do you want to only show the smoothest degree of precision? (y/n) ") == "y" else False

	subd_string = input(f"How smooth should that degree be? The default is {angle_maker.SUBDIVISIONS}, and the computation time grows exponentially with that number: ")

	if subd_string.isdecimal():
		subd_count = int(subd_string)
	else:
		subd_count = angle_maker.SUBDIVISIONS

	SHOW_CIRCLE = False if input("Do you want to show an entire circle (only an angle curve otherwise)? (y/n) ") == "n" else True

	xs = []
	ys = []
	for i in range(subd_count):
		x = [vec.x for vec in angle_maker.points]
		y = [vec.y for vec in angle_maker.points]
		#plt.plot(x,y)
		xs.append(x)
		ys.append(y)
		angle_maker.subdivide()

	angle_maker.update_curve_length()

	xs.reverse()
	ys.reverse()
	for i in range(subd_count):
		if len(xs[i]) == 2 and IGNORE_45_DEGREE_ANGLE:
			continue

		plt.plot(xs[i], ys[i])

		if SHOW_CIRCLE:
			plt.plot([-x for x in xs[i]], ys[i])
			plt.plot(xs[i], [-y for y in ys[i]])
			plt.plot([-x for x in xs[i]], [-y for y in ys[i]])

		if SHOW_ONLY_FINAL:
			break

	plt.title("Polygonal Circle" if SHOW_CIRCLE else "Angle Curve")
	plt.axis("equal")  # ensures x and y scales are equal
	plt.grid(True)
	plt.show()


if __name__ == "__main__":
	main()
