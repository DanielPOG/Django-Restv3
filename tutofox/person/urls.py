from django.urls import path
from .views import PersonApiView, PersonApiViewDetail

urlpatterns = [
    path('v1/persons', PersonApiView.as_view()),
    path('v1/persons/<int:pk>', PersonApiViewDetail.as_view)
]
