from django.urls import path
from sonicgrid.views import home

from sonicgrid.apps import SonicgridConfig

app_name = SonicgridConfig.name

urlpatterns = [
    path("", home, name='home'),
]