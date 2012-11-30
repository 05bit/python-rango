import functools
from django.contrib.gis.db.models.query import GeoQuerySet
from django.contrib.gis.db.models import *
from django.core.exceptions import ObjectDoesNotExist


class RangoGeoQuerySet(GeoQuerySet):

    def __getattr__(self, name):
        """
        Proxy query method to Model class.

        That's convinient to define domain specific query
        methods in models and chain them in queries.
        """
        method = getattr(self.model, name)
        return functools.partial(method, _queryset=self)

    def __unicode__(self):
        return u"<%s: %s>" % (self.__class__.__name__, self.model)

    def get(self, *args, **kwargs):
        try:
            return super(RangoGeoQuerySet, self).get(*args, **kwargs)
        except ObjectDoesNotExist:
            pass


class RangoGeoManager(GeoManager):
    """
    Default manager for RangoModel. It uses smart
    RangoGeoQuerySet for queries.
    """
    def get_query_set(self):
        return RangoGeoQuerySet(self.model, using=self._db)


class RangoGeoModel(Model):
    """
    RangoModel providing extra geo-features.
    """

    objects = RangoGeoManager()

    class Meta:
        abstract = True

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def get(cls, _queryset=None, **kwargs):
        _queryset = (_queryset is None) and cls.objects or _queryset
        try:
            return _queryset.get(**kwargs)
        except cls.DoesNotExist:
            pass

    @classmethod
    def create(cls, **kwargs):
        """
        Creates new instance and saves it to database.
        """
        return cls.objects.create(**kwargs)

    def update(self, **kwargs):
        """
        Updates instance fields. Note that it skips
        ``pre_save`` and ``post_save`` signals.
        """
        self.__class__.objects.filter(pk=self.pk).update(**kwargs)
        return self.__class__.objects.get(pk=self.pk)

    def _query_method(name):
        def method(cls, _queryset=None, **kwargs):
            queryset = (_queryset is None) and cls.objects or _queryset
            return getattr(queryset, name)(**kwargs)
        return method

    exclude = classmethod(_query_method('exclude'))
    filter = classmethod(_query_method('filter'))
    none = classmethod(_query_method('none'))
