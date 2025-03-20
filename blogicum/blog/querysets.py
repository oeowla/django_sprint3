from django.db import models
from django.utils import timezone
from django.http import Http404


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        )

    def get_published(self, id):
        try:
            return self.get(
                id=id,
                is_published=True,
                pub_date__lte=timezone.now(),
                category__is_published=True
            )
        except self.model.DoesNotExist:
            raise Http404()

    def publishe_for_category(self, category):
        return self.filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now()
        )
