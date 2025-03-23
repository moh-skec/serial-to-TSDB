from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.core.paginator import Paginator
from .models import Msg
from .serializers import MsgSerializer, MsgCreateSerializer, MsgUpdateSerializer


@method_decorator(csrf_exempt, name='dispatch')
class MsgView(View):
    def get(self, request, _=None):
        slug = request.GET.get('slug')
        sensor_id = request.GET.get('sensor_id')
        time = request.GET.get('time')

        filters = {}
        if slug:
            filters["slug__icontains"] = slug
        if sensor_id:
            filters["sensor_id"] = sensor_id
        if time:
            filters["time__gte"] = time

        msgs = Msg.objects.filter(**filters)
        serializer = MsgSerializer(msgs, many=True)

        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        paginator = Paginator(serializer.data, page_size)
        paginated_msgs = paginator.get_page(page)

        response_data = {
            "total_msgs": paginator.count,
            "total_pages": paginator.num_pages,
            "current_page": paginated_msgs.number,
            "msgs": list(paginated_msgs)
        }

        return JsonResponse(response_data)

    def post(self, request):
        data = json.loads(request.body)
        serializer = MsgCreateSerializer(data=data)
        if serializer.is_valid():
            msg = serializer.save()
            return JsonResponse(MsgSerializer(msg).data)
        return JsonResponse(serializer.errors, status=400)

    def put(self, request, msg_id):
        msg = get_object_or_404(Msg, id=msg_id)
        data = json.loads(request.body)
        serializer = MsgUpdateSerializer(msg, data=data, partial=True)
        if serializer.is_valid():
            msg = serializer.save()
            return JsonResponse(MsgSerializer(msg).data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, _, msg_id):
        msg = get_object_or_404(Msg, id=msg_id)
        msg.delete()
        return JsonResponse({"message": "Message deleted successfully"})
