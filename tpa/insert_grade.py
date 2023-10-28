import json
import os
import csv
from uuid import uuid4
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django
django.setup()
from django.core.files import File
from PIL import Image as ING
from tpa.ticketing.models import Grade
from django.core.files.temp import NamedTemporaryFile
from botocore.exceptions import NoCredentialsError

json_data = [
        {
            "gradeId": 79326,
            "name": "챔피언석",
            "color": "rgb(209, 80, 80)",
            "price": 45000,
        },
        {
            "gradeId": 79327,
            "name": "중앙테이블석2인",
            "color": "rgb(40, 71, 134)",
            "price": 40000,
        },
        {
            "gradeId": 79328,
            "name": "중앙테이블석3인",
            "color": "rgb(40, 71, 134)",
            "price": 40000,
        },
        {
            "gradeId": 79329,
            "name": "3루 서프라이즈석",
            "color": "rgb(223, 114, 66)",
            "price": 22000,
        },
        {
            "gradeId": 79330,
            "name": "1루 서프라이즈석",
            "color": "rgb(223, 114, 66)",
            "price": 22000,
        },
        {
            "gradeId": 79331,
            "name": "3루 타이거즈 가족석(4인)",
            "color": "rgb(94, 150, 74)",
            "price": 17500,
        },
        {
            "gradeId": 79332,
            "name": "1루 타이거즈 가족석(4인)",
            "color": "rgb(94, 150, 74)",
            "price": 17500,
        },
        {
            "gradeId": 79333,
            "name": "3루 타이거즈 가족석(6인)",
            "color": "rgb(94, 150, 74)",
            "price": 17500,
        },
        {
            "gradeId": 79334,
            "name": "1루 타이거즈 가족석(6인)",
            "color": "rgb(94, 150, 74)",
            "price": 17500,
        },
        {
            "gradeId": 79335,
            "name": "3루 파티석(4인)",
            "color": "rgb(133, 192, 220)",
            "price": 25000,
        },
        {
            "gradeId": 79336,
            "name": "1루 파티석(4인)",
            "color": "rgb(133, 192, 220)",
            "price": 25000,
        },
        {
            "gradeId": 79337,
            "name": "3루 스카이피크닉석(4인)",
            "color": "rgb(77, 73, 154)",
            "price": 17500,
        },
        {
            "gradeId": 79338,
            "name": "1루 스카이피크닉석(4인)",
            "color": "rgb(77, 73, 154)",
            "price": 17500,
        },
        {
            "gradeId": 79339,
            "name": "에코다이나믹스가족석(6인)",
            "color": "rgb(110, 190, 136)",
            "price": 16000,
        },
        {
            "gradeId": 79340,
            "name": "3루 K9",
            "color": "rgb(219, 89, 175)",
            "price": 14000,
        },
        {
            "gradeId": 79341,
            "name": "1루 K9",
            "color": "rgb(219, 89, 175)",
            "price": 14000,
        },
        {
            "gradeId": 79342,
            "name": "3루 K8",
            "color": "rgb(240, 188, 46)",
            "price": 14000,
        },
        {
            "gradeId": 79343,
            "name": "1루 K8",
            "color": "rgb(240, 188, 46)",
            "price": 14000,
        },
        {
            "gradeId": 79344,
            "name": "3루 K5",
            "color": "rgb(147, 203, 59)",
            "price": 13000,
        },
        {
            "gradeId": 79345,
            "name": "1루 K5",
            "color": "rgb(147, 203, 59)",
            "price": 13000,
        },
        {
            "gradeId": 79346,
            "name": "3루 K3",
            "color": "rgb(149, 117, 193)",
            "price": 9000,
        },
        {
            "gradeId": 79347,
            "name": "1루 K3",
            "color": "rgb(149, 117, 193)",
            "price": 9000,
        },
        {
            "gradeId": 79348,
            "name": "외야석",
            "color": "rgb(205, 173, 87)",
            "price": 11000,
        },
        {
            "gradeId": 79349,
            "name": "3루 휠체어석",
            "color": "rgb(149, 117, 193)",
            "price": 4000,
        },
        {
            "gradeId": 79350,
            "name": "1루 휠체어석",
            "color": "rgb(149, 117, 193)",
            "price": 4000,
        },
        {
            "gradeId": 79351,
            "name": "스카이박스(10인실)",
            "color": "rgb(74, 132, 209)",
            "price": 60000,
        },
        {
            "gradeId": 79352,
            "name": "스카이박스(14인실)",
            "color": "rgb(74, 132, 209)",
            "price": 60000,
        },
        {
            "gradeId": 79353,
            "name": "스카이박스(18인실)",
            "color": "rgb(74, 132, 209)",
            "price": 60000,
        }
]
idx = 0

for item in json_data:
    grade = Grade.objects.create(
        gradeId=item['gradeId'],
        name=item['name'],
        color=item['color'],
        price=item['price'],
    )
    
    print(idx)
    grade.save()
    idx = idx+1