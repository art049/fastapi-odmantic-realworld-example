from datetime import datetime
from typing import List, Tuple

from odmantic.bson import ObjectId
from pydantic import Field

from models.article import CommentModel
from models.user import UserModel
from schemas.user import Profile

from .base import BaseSchema


class Comment(BaseSchema):
    id: ObjectId
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    body: str
    author: Profile


class SingleCommentResponse(BaseSchema):
    comment: Comment


class MultipleCommentsResponse(BaseSchema):
    comments: List[Comment]

    @classmethod
    def from_comments_and_authors(cls, data: List[Tuple[CommentModel, UserModel]]):
        return cls(
            comments=[{**comment.dict(), "author": author} for comment, author in data]
        )


class NewComment(BaseSchema):
    body: str


class ProfileResponse(BaseSchema):
    profile: Profile
