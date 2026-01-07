import stripe
from django.conf import settings
from django.http import JsonResponse

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_item(request, id):
    item = Item.objects.get(id=id)
    return item


def get_stripe_id(request, id):
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/success/",
        line_items=[{"price": 54.00, "quantity": 2}],
        mode="payment",
    )

    return JsonResponse({"session_id": session.id})
