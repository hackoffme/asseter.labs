from django.urls import path
from catalog import view_rest

urlpatterns = [
    path('products/', view_rest.CatalogView.as_view()),
]
