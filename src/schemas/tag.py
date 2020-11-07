from typing import List

from .base import BaseSchema


class TagsResponse(BaseSchema):
    tags: List[str]
