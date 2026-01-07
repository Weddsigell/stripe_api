import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_item(request, id):
    item = Item.objects.get(id=id)
    return item


    item = get_object_or_404(Item, id=id)
def get_stripe_session_id(request, id):
    
    session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/success/",
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
    )

    return redirect(session.url, code=303)
