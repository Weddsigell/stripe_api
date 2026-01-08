import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_item(request, id):
    if request.method == "GET":
        item = Item.objects.get(id=id)
        return render(
            request,
            "item.html",
            {"item": item, "publishable_key": settings.STRIPE_PUBLISHABLE_KEY},
        )


def get_stripe_session_id(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        return JsonResponse({"error": "Item does not exist"}, status=404)

    if request.method == "GET":
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

        return JsonResponse({"session_id": session.id})


def index(request):
    items = Item.objects.all()
    return render(request, "index.html", {"items": items})
