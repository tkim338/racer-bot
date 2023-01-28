import matplotlib.pyplot as plt
from matplotlib.path import Path
import math


def distance(point_a: tuple, point_b: tuple) -> float:
    return math.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)


def get_track_edges(points: list, width: float) -> list:
    x = points[1][0]
    y = points[1][1]

    x_delta = points[0][0] - points[2][0]
    y_delta = points[0][1] - points[2][1]

    if x_delta != 0:
        track_angle = math.atan(y_delta / x_delta)
    else:
        track_angle = math.pi / 2 if y_delta >= 0 else -math.pi / 2
    normal_angle = math.pi / 2 - track_angle

    return [
        (x - width / 2 * math.cos(normal_angle), y + width / 2 * math.sin(normal_angle)),
        (x + width / 2 * math.cos(normal_angle), y - width / 2 * math.sin(normal_angle))
    ]


class Track:
    def __init__(self, track_coordinates: list = None, track_width: float = 1) -> None:
        loop_a = list()
        loop_b = list()

        track_edges = get_track_edges([track_coordinates[-1]] + track_coordinates[:2], track_width)
        loop_a.append(track_edges[0])
        loop_b.append(track_edges[1])

        track_coordinates.append(track_coordinates[0])

        for i in range(1, len(track_coordinates) - 1):
            track_edges = get_track_edges(track_coordinates[i - 1:i + 2], track_width)

            for edge_point in track_edges:
                distance_a = distance(edge_point, loop_a[-1])
                distance_b = distance(edge_point, loop_b[-1])

                if distance_a < distance_b:
                    loop_a.append(edge_point)
                else:
                    loop_b.append(edge_point)

        loop_a.append(loop_a[0])
        loop_b.append(loop_b[0])

        self.path_a = Path(loop_a)
        self.path_b = Path(loop_b)

    def print_track(self) -> None:
        plt.plot(self.path_a.vertices[:, 0], self.path_a.vertices[:, 1])
        plt.plot(self.path_b.vertices[:, 0], self.path_b.vertices[:, 1])
        return None

    def is_within_track(self, point: tuple) -> bool:
        return self.path_a.contains_point(point) != self.path_b.contains_point(point)
