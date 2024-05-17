import gymnasium
from src.car_model import Car
from src.tire_model import Tire
from src.track_model import Track


class RaceEnv(gymnasium.Env):
    def __init__(self, car: Car, tire: Tire, track: Track):
        self.car = car
        self.tire = tire
        self.track = track

    def step(
        self, action: gymnasium.core.ActType
    ) -> tuple[
        gymnasium.core.ObsType,
        gymnasium.core.SupportsFloat,
        bool,
        bool,
        dict[str, gymnasium.core.Any],
    ]:
        return

    def reset(
        self,
        *,
        seed: int | None = None,
        options: dict[str, gymnasium.core.Any] | None = None
    ) -> tuple[gymnasium.core.ObsType, dict[str, gymnasium.core.Any]]:
        self.car = Car()
        self.tire = Tire()
        self.track = Track()

        self.car.set_tire(self.tire)
        self.car.set_location((0, 0))

        return

    def render(self) -> None:
        return

    def close(self) -> None:
        return
