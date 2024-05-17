import math


class Tire:
    def __init__(
        self, static_friction_coeff: float = 1.0, kinetic_friction_coeff: float = 0.7
    ):
        self.static_friction_coeff = static_friction_coeff
        self.kinetic_friction_coeff = kinetic_friction_coeff

    def get_grip(
        self,
        normal_load: float = 0.0,
        longitudinal_load: float = 0.0,
        lateral_load: float = 0.0,
    ) -> float:
        total_load = math.sqrt(longitudinal_load**2 + lateral_load**2)
        max_static_grip = normal_load * self.static_friction_coeff
        if total_load <= max_static_grip:
            return total_load

        max_kinetic_grip = normal_load * self.kinetic_friction_coeff
        return max_kinetic_grip
