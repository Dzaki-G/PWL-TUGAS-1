from django.http import JsonResponse

def apply_coupon(request):
    return JsonResponse({"message": "Coupon applied!"})
