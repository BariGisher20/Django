from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Вы не вввели тег')

        self.count = 0
        for form in self.forms:

            if self.count > 0 and form.cleaned_data.get('is_main'):  # не могли бы вы объяснить эту конструкцию? Как ведется подсчет в self.count именно по is_main? Данную форму нашла в интернете
                raise ValidationError('Главный может быть только 1 тег')
            else:
                if form.cleaned_data.get('is_main'):
                    print(f"{form.cleaned_data.get('tags')} - главный раздел")
                    self.count += 1
                else:
                    continue
        if self.count < 1:
            raise ValidationError('Должен быть хотя бы один основной тег')

        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ArticleTagInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

