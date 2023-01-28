from tire_model import Tire


class Car:
    def __init__(
            self,
            cg_height: float = 0.0,
            cg_location: tuple = (0.5, 0.5),
            track_width: float = 1,
            wheelbase: float = 1,
            mass: float = 1,
            max_power: float = 1,
            drivetrain: str = "rwd"
    ):
        """
        Define major parameters of the car.  All parameters should be provided in SI units.
        :param cg_height: height of center of gravity (CG) of car from ground
        :param cg_location: location of center of gravity (CG) of car from front-left tire; positive direction towards
        right and rear
        :param track_width: distance between left and right tires
        :param wheelbase: distance between front and rear tires
        :param mass: total mass of car
        :param max_power: maximum power output of car
        :param drivetrain: specify FWD, RWD, or AWD (all assumed to use locked differentials)
        """
        self.cg_height = cg_height
        self.cg_location = cg_location
        self.track_width = track_width
        self.wheelbase = wheelbase
        self.mass = mass
        self.max_power = max_power
        self.drivetrain = drivetrain
        self.tire = None

    def set_tire(self, tire: Tire = None):
        self.tire = tire
