from datetime import datetime
from typing import List

from odmantic.bson import ObjectId
from pydantic import Field

from models.article import ArticleModel
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
    def from_article_instance(cls, article: ArticleModel):
        return cls(comments=article.comments)


class NewComment(BaseSchema):
    body: str


class ProfileResponse(BaseSchema):
    profile: Profile
