from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:first>/add/<int:second>/", views.add_numbers, name="add_numbers"),
    path("transform/<str:word>/", views.transform, name="upper"),
    path("check/<str:word>/", views.check, name="check"),
    path("calc/<int:first>/<str:operation>/<int:second>/", views.calc, name="calc"),
]