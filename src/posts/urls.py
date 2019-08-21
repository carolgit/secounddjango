from django.conf.urls import url
from .views import post_list, post_detail, post_create, post_update, post_delete

urlpatterns = [
    url('<post_id>/delete', post_delete),
    url('<post_id>/update', post_update),
    url('<post_id>/', post_detail),
    url('create/', post_create),
    url('', post_list),
]
