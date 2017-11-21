from django.http import HttpResponse

from rest_framework import permissions
from rest_framework import views, status

from mandel_brot.serializers import Mandelbrot

#http://127.0.0.1:8000/Mandelbrot/getMandelbrot?w=100&h=250&it=1500


class ImageView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        return HttpResponse(Mandelbrot(width=request.query_params['w'],
                                       height=request.query_params['h'],
                                       iterations=request.query_params['it']).in_bytes()
                            , status=status.HTTP_201_CREATED, content_type="image/png")

