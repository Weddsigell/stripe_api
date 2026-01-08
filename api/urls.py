from django.urls import path

from .views import get_item, get_stripe_session_id

app_name = "api"

urlpatterns = [
    path("item/<int:id>/", get_item),
    path("buy/<int:id>/", get_stripe_session_id),
]
