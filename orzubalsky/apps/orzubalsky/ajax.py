from dajaxice.decorators import dajaxice_register
from dajaxice.utils import deserialize_form
from orzubalsky.views import *


@dajaxice_register(method='POST')
def ajax_load(request, slug=None):
    """ """
    return home(request)