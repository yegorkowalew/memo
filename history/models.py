from django.db import models


class IconType(models.Model):
    """Model definition for IconType."""

    icon = models.CharField(
        verbose_name="Код иконки",
        max_length=50
    )
    color = models.CharField(
        verbose_name="Цвет",
        max_length=50
    )

    class Meta:
        """Meta definition for IconType."""

        verbose_name = 'тип иконки'
        verbose_name_plural = 'типы иконок'

    def __str__(self):
        """Unicode representation of IconType."""
        return '%s, %s' % (self.icon, self.color)


class History(models.Model):
    """Model definition for History."""
    icon_text = models.ForeignKey(
        IconType,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name="Название",
        max_length=200
    )
    link = models.CharField(
        verbose_name="Ссылка",
        max_length=200
    )
    short_text = models.CharField(
        verbose_name="Короткий текст",
        max_length=200
    )
    full_text = models.TextField(
        verbose_name="Полный текст",
        blank=True,
        null=True
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        """Meta definition for History."""

        verbose_name = 'история'
        verbose_name_plural = 'истории'

    def __str__(self):
        """Unicode representation of History."""
        return "%s - %s" % (self.name, self.last_updated)
