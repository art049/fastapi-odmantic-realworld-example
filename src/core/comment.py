from typing import Tuple

from odmantic.bson import ObjectId
from odmantic.engine import AIOEngine

from core.exceptions import CommentNotFoundException, NotCommentAuthorException
from models.article import ArticleModel, CommentModel
from models.user import UserModel


def ensure_is_comment_author(user: UserModel, comment: CommentModel):
    if comment.author != user:
        raise NotCommentAuthorException()


async def add_new_comment(
    engine: AIOEngine, article: ArticleModel, comment: CommentModel
):
    article.comments += (comment,)
    await engine.save(article)


def get_comment_and_index_from_id(
    article: ArticleModel, comment_id: ObjectId
) -> Tuple[CommentModel, int]:
    for index, comment in enumerate(article.comments):
        if comment.id == comment_id:
            return comment, index
    raise CommentNotFoundException()


async def delete_comment_by_index(engine: AIOEngine, article: ArticleModel, index: int):
    article.comments = article.comments[:index] + article.comments[index + 1 :]
    await engine.save(article)
