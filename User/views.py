from django.http import JsonResponse

from .models import User


# Create your views here.
def get_user_role_and_tg_id(request,token):
    if request.method == "POST":
        user = User.objects.get(token=token)
        if user:
            return JsonResponse({'id':user.id,'tg_id': user.tg_id, 'role': user.role})
        return JsonResponse({'message':'error'})
    return JsonResponse({'message':'error method'})