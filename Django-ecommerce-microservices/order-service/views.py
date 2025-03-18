from django.http import JsonResponse

def create_order(request):
    return JsonResponse({"message": "Order created!"})

def order_status(request):
    return JsonResponse({"message": "Order status!"})
