from django.conf import settings
from django.db.models import *
from django.utils import timezone
from django.contrib.flatpages.models import FlatPage
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField
import pytz, os



class Base(Model):
    """ Base model for all of the models in the application.
    """

    class Meta:
        abstract = True
    
    # Translators:  Used wherever a created time stamp is needed.                   
    created     = DateTimeField(verbose_name=_("created"), editable=False)
    
    # Translators: Used wherever an update time stamp is needed.
    updated     = DateTimeField(verbose_name=_("updated"), editable=False)
    
    # Translators: Used to determine whether something is active in the front end or not.
    is_active   = BooleanField(verbose_name=_("is active"), default=1)
    
    def save(self, *args, **kwargs):
        """ Save timezone-aware values for created and updated fields.
        """
        if self.pk is None:
            self.created = timezone.now()
        self.updated = timezone.now()
        super(Base, self).save(*args, **kwargs)
        
    def __unicode__ (self):
        if hasattr(self, "name") and self.name:
            return self.name
        else:
            return "%s" % (type(self))


# signals are separated to signals.py 
# just for the sake of organization
import signals