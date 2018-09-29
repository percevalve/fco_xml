from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r"^person/(?P<entity_id>[A-Za-z0-9]+)/?$", WikiDetailsAPI.as_view(), name="wikidata_details"),
    url(r"^person/picker/(?P<keyword>[A-Za-z0-9]+)/?$", PersonPickerAPI.as_view(), name="wikidata_picker"),
]