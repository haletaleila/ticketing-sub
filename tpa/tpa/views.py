from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

class ReactAppView(View):
    def get(self,request):
        try:
            with open(os.path.join(str(settings.BASE_DIR), 'frontend', 'build', 'index.html'), encoding='utf-8') as file:
                return HttpResponse(file.read())

        except Exception as e:
            return HttpResponse(
                '''
                index.html not found!
                ''',
                status=501,
            )