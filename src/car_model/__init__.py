from src.tire_model import Tire
import matplotlib.pyplot as plt


class Car:
    def __init__(
            self,
            cg_height: float = 0.45,
            cg_location: tuple = (0.85, 1.15),
            track_width: float = 1.7,
            wheelbase: float = 2.3,
            mass: float = 0.96,
            max_power: float = 85000,
            drivetrain: str = "rwd",
            tire: Tire = Tire()
    ):
        """
        Define major parameters of the car.  All parameters should be provided in SI units.
        :param cg_height: height of center of gravity (CG) of car from ground [m]
        :param cg_location: location of center of gravity (CG) of car from front-left tire; positive direction towards
        right and rear [m, m]
        :param track_width: distance between left and right tires [m]
        :param wheelbase: distance between front and rear tires [m]
        :param mass: total mass of car [kg]
        :param max_power: maximum power output of car [W]
        :param drivetrain: specify FWD, RWD, or AWD (all assumed to use locked differentials)
        """
        self.cg_height = cg_height
        self.cg_location = cg_location
        self.track_width = track_width
        self.wheelbase = wheelbase
        self.mass = mass
        self.max_power = max_power
        self.drivetrain = drivetrain
        self.tire = tire
        self.location = (0, 0)
        self.velocity = (0, 0)
        self.power_output = 0.0

    # def set_tire(self, tire: Tire = None):
    #     self.tire = tire

    def set_location(self, loc: tuple = (0, 0)):
        self.location = loc
