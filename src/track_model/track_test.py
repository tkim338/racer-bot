from src.track_model import Track
import math
import numpy as np


def generate_track():
    # create rounded square track
    track_coor = [(i + 10.0, 0.0) for i in range(80)] + \
                 [(90 + 10 * math.cos(angle), 10 + 10 * math.sin(angle))
                  for angle in np.linspace(math.pi * 3 / 2, math.pi * 2, 10)] + \
                 [(100, i + 10) for i in range(80)] + \
                 [(90 + 10 * math.cos(angle), 90 + 10 * math.sin(angle))
                  for angle in np.linspace(0, math.pi / 2, 10)] + \
                 [(90 - i, 100) for i in range(80)] + \
                 [(10 + 10 * math.cos(angle), 90 + 10 * math.sin(angle))
                  for angle in np.linspace(math.pi / 2, math.pi, 10)] + \
                 [(0, 90 - i) for i in range(80)] + \
                 [(10 + 10 * math.cos(angle), 10 + 10 * math.sin(angle))
                  for angle in np.linspace(math.pi, math.pi * 3 / 2, 10)]
    width = 10

    t = Track(track_coordinates=track_coor, track_width=width)
    return t


def test_on_track():
    track = generate_track()
    assert track.is_within_track((50, 0)) is True


def test_outside_track():
    track = generate_track()
    assert track.is_within_track((-10, -10)) is False


def test_inside_track():
    track = generate_track()
    assert track.is_within_track((50, 50)) is False
