from django.db import models


MAX_NAME_LENGTH: int = 256


class BaseModel(models.Model):
    """Базовая модель."""

    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Добавлено",
    )

    class Meta:
        abstract = True


class BaseTitle(models.Model):
    """Базовая модель заголовка."""

    title = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name="Заголовок",
    )

    class Meta:
        abstract = True
