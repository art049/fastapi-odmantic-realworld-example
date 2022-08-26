from typing import Optional

from odmantic import AIOEngine
from odmantic.query import QueryExpression, desc

from core.exceptions import ArticleNotFoundException, NotArticleAuthorException
from models.article import ArticleModel
from models.user import UserModel
from schemas.article import MultipleArticlesResponse


async def build_get_articles_query(
    engine: AIOEngine,
    author: Optional[str],
    favorited: Optional[str],
    tag: Optional[str],
) -> Optional[QueryExpression]:
    query = QueryExpression()

    if author is not None:
        author_user = await engine.find_one(UserModel, UserModel.username == author)
        if author_user is None:
            return None
        query &= ArticleModel.author == author_user.id

    if tag is not None:
        query &= {+ArticleModel.tag_list: {"$elemMatch": {"$eq": tag}}}

    if favorited is not None:
        favorited_user = await engine.find_one(
            UserModel, UserModel.username == favorited
        )
        if favorited_user is None:
            return None
        query &= {
            +ArticleModel.favorited_user_ids: {"$elemMatch": {"$eq": favorited_user.id}}
        }

    return query


def build_get_feed_articles_query(user: UserModel) -> QueryExpression:
    return ArticleModel.id.in_(user.following_ids)


async def get_multiple_articles_response(
    engine: AIOEngine,
    user: Optional[UserModel],
    query: QueryExpression,
    limit: int,
    offset: int,
) -> MultipleArticlesResponse:
    articles = await engine.find(
        ArticleModel,
        query,
        skip=offset,
        limit=limit,
        sort=desc(ArticleModel.created_at),
    )
    count = await engine.count(ArticleModel, query)
    return MultipleArticlesResponse.from_article_instances(articles, count, user)


async def get_article_by_slug(engine: AIOEngine, slug: str) -> ArticleModel:
    article = await engine.find_one(ArticleModel, ArticleModel.slug == slug)
    if article is None:
        raise ArticleNotFoundException()
    return article


async def add_article_to_favorite(
    engine: AIOEngine, user: UserModel, article: ArticleModel
) -> ArticleModel:
    favorited_set = {*article.favorited_user_ids, user.id}
    article.favorited_user_ids = tuple(favorited_set)
    await engine.save(article)
    return article


async def remove_article_from_favorites(
    engine: AIOEngine, user: UserModel, article: ArticleModel
) -> ArticleModel:
    favorited_set = {*article.favorited_user_ids} - {user.id}
    article.favorited_user_ids = tuple(favorited_set)
    await engine.save(article)
    return article


def ensure_is_author(user: UserModel, article: ArticleModel):
    if user != article.author:
        raise NotArticleAuthorException()
