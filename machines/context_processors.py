from .models import Machine


def all_machines(request):
    return {'machines': Machine.objects.all()}