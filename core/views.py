from django.http import JsonResponse

from .models import Visit


def home(request):
    visit = Visit.objects.create()

    return JsonResponse(
        {
            "message": "Hello from Phoenix",
            "visit_id": visit.id,
        }
    )


def health(request):
    return JsonResponse(
        {
            "status": "ok",
        }
    )
