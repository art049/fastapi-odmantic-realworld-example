from __future__ import annotations

from datetime import datetime
from typing import Any, List, Optional

from pydantic import BaseModel, Field, SecretStr


class Article(BaseModel):
    slug: str
    title: str
    description: str
    body: str
    tag_list: List[str] = Field(..., alias="tagList")
    created_at: datetime = Field(..., alias="createdAt")
    updated_at: datetime = Field(..., alias="updatedAt")
    favorited: bool
    favorites_count: int = Field(..., alias="favoritesCount")
    author: Profile


class SingleArticleResponse(BaseModel):
    article: Article


class MultipleArticlesResponse(BaseModel):
    articles: List[Article]
    articles_count: int = Field(..., alias="articlesCount")


class NewArticle(BaseModel):
    title: str
    description: str
    body: str
    tag_list: Optional[List[str]] = Field(None, alias="tagList")


class NewArticleRequest(BaseModel):
    article: NewArticle


class UpdateArticle(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    body: Optional[str] = None


class UpdateArticleRequest(BaseModel):
    article: UpdateArticle
