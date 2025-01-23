from django.http import JsonResponse
from .models import User
# Create your views here.

def user(request):
    if request.method == "GET":
        users = User.objects.all()
        users_data = [{'id': user.id, 'username': user.username,'tg_id':user.tg_id} for user in users]
        return JsonResponse({'users': users_data})

    if request.method == 'POST':
        # username = request.POST['username']
        tg_id = request.POST['tg_id']
        # password = request.POST['password']

        # Check if the user already exists
        if User.objects.filter(tg_id=tg_id).exists():
            return JsonResponse({'error': 'User already exists'}, status=400)

        # Create the new user
        user = User.objects.create(tg_id=tg_id)
        user.save()

        # Return user data
        user_data = {'id': user.id, 'username': user.username}
        return JsonResponse({'user': user_data}, status=201)