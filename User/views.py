from django.http import JsonResponse

from .models import User


# Create your views here.
def get_user_role_and_tg_id(request):
    if request.method == "POST":
        token = request.POST.get("token")
        print(token)
        user = User.objects.get(token=token)
        print(user.id)
        if user:
            return JsonResponse({'id':user.id,'tg_id': user.tg_id, 'role': user.role},status=200)
        return JsonResponse({'message':'error'},status=404)
    return JsonResponse({'message':'error method'})