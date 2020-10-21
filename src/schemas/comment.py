from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from schemas.user import Profile


class Comment(BaseModel):
    id: int
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    body: str
    author: Profile


class SingleCommentResponse(BaseModel):
    comment: Comment


class MultipleCommentsResponse(BaseModel):
    comments: List[Comment]


class NewComment(BaseModel):
    body: str


class NewCommentRequest(BaseModel):
    comment: NewComment


class TagsResponse(BaseModel):
    tags: List[str]


class ProfileResponse(BaseModel):
    profile: Profile
