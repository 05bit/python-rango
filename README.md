Rango
=====

Rango is a bit spice for Django.

Why?
----

I beleive that short and plain imports are better than long
nested ones.

In Django you should write in your ``views.py``:

    from django.core.urlresolvers import reverse
    from django.shortcuts import get_object_or_404, redirect
    from django.contrib.auth.decorators import login_required

In Rango:

    from rango.urls import reverse
    from rango.views import get_object_or_404, login_required

Actually that is experimental project tending to build cleaner
API for Django.

Core features
-------------

### New ``reverse`` method

It works like that:

    from rango.urls import reverse
    reverse('url_name', pk=8)

Django ``reverse`` works so:

    from django.core.urlresolvers import reverse
    reverse('url_name', kwargs={'pk': 8})

### Base model class

It has shorctuts for ``all``, ``get``, ``filter`` and ``exclude``
methods and some extra magic:

    from rango import models

    class MyModel(models.RangoModel):
        class MyModel(RangoModel):
            title = models.CharField(max_length=100)
            is_active = models.BooleanField()

            @classmethod
            def active(cls, _queryset=None):
                return cls.filter(_queryset, is_active=True)

    all_objects = MyModel.all()
    start_with_a = MyModel.filter(title__startswith="a")
    active_objects = start_with_a.active()

**Note!** Now you can define filter methods in model class
and chain them in queries. Magic!

### Shortcuts ``rango.views``

    from rango.views import render_to, ajax_request, render_to_response, \
           render, redirect, get_object_or_404, login_required

### Mailing shortcut

If you need to compose E-mail message body from template and
send it you may use a shortcut:

    from rango.mail import send_template

    send_template(subject='Subject', template='mail.html',
                  recipient_list=[to@example.com],
                  context={})

Full method signature:

    def send_template(subject=None, template=None, recipient_list=[],
                      context={}, from_email=None, **kwargs)

### Other shortcuts and stuff

    from rango.crypto import random_token
    random_token(20)  # creates rangom string

    # Yes! that's replacement for
    # from django.conf import settings
    from rango import settings
    settings.has_setting('CUSTOM_SETTINGS')
    settings.get_setting('CUSTOM_SETTINGS', default='Some value')

    from rango.utils import safe_filename
    from rango import models
    class MyFile(models.Model):
        file = models.FileField(upload_to=safe_upload_to('files'))
        # files will be uploaded to
        # files/<instance id>/<random>_<filename>


Documentation
-------------

It's not ready yet, I'm working on it.

If you're brave, watch in the source :)
