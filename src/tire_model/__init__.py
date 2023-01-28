import math


class Tire:
    def __init__(self, static_friction_coeff, dynamic_friction_coeff):
        self.static_friction_coeff = static_friction_coeff
        self.dynamic_friction_coeff = dynamic_friction_coeff

    def get_grip(
            self,
            normal_load: float = 0.0,
            longitudinal_load: float = 0.0,
            lateral_load: float = 0.0
    ) -> float:
        total_load = math.sqrt(longitudinal_load**2 + lateral_load**2)
        max_static_grip = normal_load * self.static_friction_coeff
        if total_load <= max_static_grip:
            return total_load

        max_dynamic_grip = normal_load * self.dynamic_friction_coeff
        return max_dynamic_grip
