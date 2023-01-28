from src.tire_model import Tire


def test_get_grip_zero():
    tire = Tire(static_friction_coeff=0, dynamic_friction_coeff=0)
    assert tire.get_grip(normal_load=0, longitudinal_load=0, lateral_load=0) == 0


def test_get_grip_static():
    tire = Tire(static_friction_coeff=1, dynamic_friction_coeff=0)
    assert tire.get_grip(normal_load=1, longitudinal_load=1, lateral_load=0) == 1


def test_get_grip_dynamic():
    tire = Tire(static_friction_coeff=0, dynamic_friction_coeff=0.5)
    assert tire.get_grip(normal_load=1, longitudinal_load=1, lateral_load=0) == 0.5
