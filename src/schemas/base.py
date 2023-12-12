from datetime import datetime

from odmantic.bson import BSON_TYPES_ENCODERS
from pydantic.main import BaseModel


class BaseSchema(BaseModel):
    model_config = {
        "populate_by_name": True,
        "json_encoders": {
            datetime: lambda d: d.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            **BSON_TYPES_ENCODERS,
        },
        "from_attributes": True,
    }
