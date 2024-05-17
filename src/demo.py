from track_model import Track
from car_model import Car


def main():
    my_track = Track(
        track_coordinates=[(0,0), (100,0), (100,100), (0,100)],
        track_width=10
    )

    my_car = Car(
        cg_height=0.5,
        cg_location=(0.85, 1.15),
        track_width=1.7,
        wheelbase=2.3,
        mass=0.96,
        max_power=85000,
        drivetrain="rwd"
    )

    my_car.set_location((0,0))

    my_track.print_track()

    within_track = my_track.is_within_track(
        my_car.location
    )

    print(within_track)


if __name__ == '__main__':
    main()
