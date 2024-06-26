from datetime import datetime, timezone
import time
from typing import Any, ClassVar, Dict, Mapping, Optional, Sequence
from typing_extensions import Self
from viam.components.sensor import Sensor
from viam.logging import getLogger
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily


LOGGER = getLogger(__name__)

class MySensor(Sensor):
    MODEL: ClassVar[Model] = Model(ModelFamily("bill", "time"), "sensor")
    
    def __init__(self, name: str):
        super().__init__(name)

    @classmethod
    def new(
        cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]
    ) -> Self:
        # Create a new instance of MySensor and configure it
        sensor = cls(config.name)
        sensor.reconfigure(config, dependencies)
        return sensor

    @classmethod
    def validate_config(cls, config: Dict[str, Any]) -> Sequence[str]:
        return []

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        pass

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        current_utc_time = {}
        current_utc_time = str(datetime.now(timezone.utc))
        return {"Current UTC time:": current_utc_time}

