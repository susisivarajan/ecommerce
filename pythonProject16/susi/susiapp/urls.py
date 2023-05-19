
from django.urls import path

from .import views
urlpatterns=[
    path("",views.index,name='index'),
    path("view/<int:susi_id>/", views.detail, name='view'),
    path("add", views.add_movie, name='add'),
    path("update/<int:new_id>/",views.update_detail,name='update'),
    path("delete/<int:delete_id>/",views.delete_detail,name='delete'),
    path("list",views.list_view.as_view(),name="list"),
    path("detail/<int:pk>/",views.detail_view.as_view(),name="detail"),
    path("update/<int:pk>/",views.update_view.as_view(),name="update"),
    path("delete/<int:pk>/",views.delete_view.as_view(),name='delete'),
]