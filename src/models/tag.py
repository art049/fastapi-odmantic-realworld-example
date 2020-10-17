from odmantic import Model
from odmantic.field import Field


class TagModel(Model):
    name: str = Field(primary_field=True)
