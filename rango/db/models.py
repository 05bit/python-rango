from django.db.models import *
# from django.db.models import Model as DjangoModel
from django.core.exceptions import ObjectDoesNotExist


class RangoQuerySet(query.QuerySet):

    def __getattr__(self, name):
        """
        Proxy query method to Model class.

        That's convinient to define domain specific query
        methods in models and chain them in queries.
        """
        return getattr(self.model, name)


class RangoManager(Manager):
    """
    Default manager for RangoModel. It uses smart
    RangoQuerySet for queries.
    """
    def get_query_set(self):
        return RangoQuerySet(self.model, using=self._db)


class RangoModel(Model):
    """
    That's experimental Model class. Let's play with Django ORM
    queries API and try to dry it!

    Now you can define filter methods in models and chain
    them in queries::

        class MyModel(RangoModel):
            is_active = models.BooleanField()

            @classmethod
            def active(cls, _queryset=None):
                return cls.filter(_queryset, is_active=True)


        all_objects = MyModel.all()
        active_objects = all_objects.active()
    """

    objects = RangoManager()

    class Meta:
        abstract = True

    def update(self, **kwargs):
        """
        Updates instance fields. Note that it skips
        ``pre_save`` and ``post_save`` signals.
        """
        self.__class__.objects.filter(pk=self.pk).update(**kwargs)
        return self.__class__.objects.get(pk=self.pk)

    @classmethod
    def all(cls, _queryset=None):
        if _queryset is None:
            return cls.objects.all()
        else:
            return _queryset.all()

    @classmethod
    def filter(cls, _queryset=None, **kwargs):
        if _queryset is None:
            _queryset = cls.objects.all()
        return _queryset.filter(**kwargs)


# def get_object_or_none(klass, *args, **kwargs):
#     """
#     Function is similar to ``get_object_or_404`` but 
#     returns None if the object does not exist.
#     """
#     manager = None
#     queryset = None
#     if isinstance(klass, QuerySet):
#         queryset = klass
#     elif isinstance(klass, Manager):
#         manager = klass
#     else:
#         manager = klass._default_manager
#     try:
#         return (queryset or manager).get(*args, **kwargs)
#     except ObjectDoesNotExist:
#         return None
