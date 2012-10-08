from django.db.models import *
from django.core.exceptions import ObjectDoesNotExist

def get_object_or_none(klass, *args, **kwargs):
    """
    Function is similar to ``get_object_or_404`` but 
    returns None if the object does not exist.
    """
    manager = None
    queryset = None
    if isinstance(klass, QuerySet):
        queryset = klass
    elif isinstance(klass, Manager):
        manager = klass
    else:
        manager = klass._default_manager
    try:
        return (queryset or manager).get(*args, **kwargs)
    except ObjectDoesNotExist:
        return None

def update(self, **kwargs):
	self.__class__.objects.filter(pk=self.pk).update(**kwargs)
	return self.__class__.objects.get(pk=self.pk)	

Model.update = update