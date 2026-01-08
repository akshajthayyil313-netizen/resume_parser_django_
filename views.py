from django.http import JsonResponse

def upload_resume(request):
    return JsonResponse({"status": "API WORKING"})