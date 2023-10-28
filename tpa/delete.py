
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django
django.setup()
from tpa.ticketing.models import Block, Baseball, Point, Grade
from tpa.ticketing.serializers import SeatSerializer
import time
idx = 0

Point.objects.all().delete()
Block.objects.all().delete()
Grade.objects.all().delete()
Baseball.objects.all().delete()
