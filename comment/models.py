from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel
from publication.models import Publication


class Comment(BaseModel):
    text = models.TextField()
    publication = models.ForeignKey(
        to=Publication,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="Публикация"
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=True,
        related_name="comment",
        verbose_name="От кого"
    )


class CommentLike(BaseModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comment_like",
        verbose_name="От кого"
    )

    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        related_name="like",
        verbose_name="Какому комментарию"
    )


class CommentToComment(BaseModel):
    text = models.TextField()
    comment = models.ForeignKey(
        to=Comment,
        on_delete=models.CASCADE,
        related_name="comment",
        verbose_name="На комментарий"
    )
    user = models.ForeignKey(
        to=User,
        null=True,
        on_delete=models.CASCADE,
        related_name="comment_to_comment",
        verbose_name="От кого"
    )


class CommentToCommentLike(BaseModel):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="comment_to_comment_like",
        verbose_name="От кого"
    )

    comment = models.ForeignKey(
        to=CommentToComment,
        on_delete=models.CASCADE,
        related_name="like",
        verbose_name="Какому комментарию (на комментарий)"
    )
