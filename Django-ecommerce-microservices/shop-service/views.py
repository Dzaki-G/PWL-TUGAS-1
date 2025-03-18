from django.http import JsonResponse

def view_products(request):
    return JsonResponse({"message": "List of products!"})

def view_product(request, id):
    return JsonResponse({"message": f"Details of product {id}!"})
