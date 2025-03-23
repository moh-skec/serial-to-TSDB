from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.core.paginator import Paginator
from .models import UserProfile
from .serializers import UserProfileSerializer, UserProfileCreateSerializer, UserProfileUpdateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserProfileView(View):
    def get(self, request, _=None):
        name = request.GET.get('name')
        email = request.GET.get('email')

        filters = {}
        if name:
            filters["username__icontains"] = name
        if email:
            filters["email__icontains"] = email

        users = UserProfile.objects.filter(**filters)
        serializer = UserProfileSerializer(users, many=True)

        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        paginator = Paginator(serializer.data, page_size)
        paginated_users = paginator.get_page(page)

        response_data = {
            "total_users": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": paginated_users.number,
            "users": list(paginated_users)
        }

        return JsonResponse(response_data)

    def post(self, request):
        data = json.loads(request.body)
        serializer = UserProfileCreateSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse(UserProfileSerializer(user).data)
        return JsonResponse(serializer.errors, status=400)

    def put(self, request, user_id):
        user = get_object_or_404(UserProfile, id=user_id)
        data = json.loads(request.body)
        serializer = UserProfileUpdateSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse(UserProfileSerializer(user).data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, _, user_id):
        user = get_object_or_404(UserProfile, id=user_id)
        user.delete()
        return JsonResponse({"message": "User deleted successfully"})
