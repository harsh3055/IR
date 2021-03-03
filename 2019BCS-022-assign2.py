import math


def compute_transform(X, Y):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result


def compute_point(X, Y):
    result = [0, 0, 0]
    for i in range(len(X)):
        for j in range(len(Y)):
            result[i] += X[i][j] * Y[j]
    return result


def transform():
    coord = list(
        map(
            int,
            input("Enter the point in x y z coordinates: ").strip().split(),
        )
    )[:3]
    theta = list(
        map(
            int,
            input(
                "Enter the angles of rotation about the x y z coordinates in degrees: "
            )
            .strip()
            .split(),
        )
    )[:3]

    rotation_X = [
        [1, 0, 0],
        [0, math.cos(math.radians(theta[0])), -math.sin(math.radians(theta[0]))],
        [0, math.sin(math.radians(theta[0])), math.cos(math.radians(theta[0]))],
    ]

    rotation_Y = [
        [math.cos(math.radians(theta[1])), 0, math.sin(math.radians(theta[1]))],
        [0, 1, 0],
        [-math.sin(math.radians(theta[1])), 0, math.cos(math.radians(theta[1]))],
    ]

    rotation_Z = [
        [math.cos(math.radians(theta[2])), -math.sin(math.radians(theta[2])), 0],
        [math.sin(math.radians(theta[2])), math.cos(math.radians(theta[2])), 0],
        [0, 0, 1],
    ]

    transformation = compute_transform(rotation_X, rotation_Y)
    transformation = compute_transform(transformation, rotation_Z)
    final_result = compute_point(transformation, coord)

    print(
        f"Coordinates of Point {coord[0], coord[1], coord[2]} with respect to original frame is {round(final_result[0], 5), round(final_result[1], 5), round(final_result[2], 5)}"
    )
    input("Press Enter to exit...")


if __name__ == "__main__":
    transform()