from django.http import JsonResponse

def add_to_cart(request):
    return JsonResponse({"message": "Item added to cart!"})

def remove_from_cart(request):
    return JsonResponse({"message": "Item removed from cart!"})
