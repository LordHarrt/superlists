from django.conf.urls import include, url

from lists.views import home_page

urlpatterns = [
    url(r'', home_page),
]