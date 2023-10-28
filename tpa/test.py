import requests
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django
django.setup()
from tpa.ticketing.models import Block, Baseball, Point, Grade, Football, Seat
from tpa.ticketing.serializers import SeatSerializer
import time
idx = 0

#Point.objects.all().delete()
#Block.objects.all().delete()
#Grade.objects.all().delete()
#Baseball.objects.all().delete()

# 요청 헤더 설정
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko,en;q=0.9,en-US;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': 'SCOUTER=z3tn1jt1igms0f; mxuid=6286e520-2718-4253-92fd-1a6afd2860c2; ACEFCID=UID-64213BC88EDF6312C195FD82; _ga=GA1.1.925149570.1694002522; _fbp=fb.2.1694002593383.938403197; ACEUACS=1679899592880106226; TKLINK_SES=AAAAlzayBAg4eXwKuxQm6-19YcWgXrSJ-3jpin7DMo3M1NFd3YBI_fCET5-rUTMl_nhjCP1E8_cgn0RJR4Ur-CPf5kadJoz5awLcdng6LoNi3MM5dsAqlRjgTL99ICvpBB3B2zgUcM-SBu3_zAdHrgKzdohpFt73qOHll567xFwci5vWM6MhEhsEfNMoW8KSyYH5NcE0DzhXvTBkujCZzIq4zyk.A; TKLINK=I5CKSo5m%2F2tcpCeYfAdGJFELUU3wwrgZLSqXRFxBXfW3dJY6uJANteOPOIcZ7xbfc3kk%2BAIfrU7MjuYCT%2Fg6lTfPmcYWAeOy5oA1G6vbhNCb5Abd00rP%2BFiI90JygU9fRafOShDwz8FUiXq0oYpGRppWlU8u7RuWlpj2PYN%2FnREC%2BkruIdnLPakMvrPZhV7ZsYTrrdaRy9unNU0A9hIFspwhyVOREUzsqRD3vaIwkAg9Pweapb4IfmhVWcNjrbAQxivN1lTGPsazi9QlBeMJwCjGxcnrDupuvi07PxSPEjd2Mdb6WKBB5urWUAwmOcYTkXi%2Bm7YKmtkWgeR07F1n4RwaSAJsHzsvqVCbq%2FU3kp0rfnWdl9StolG1vxiauC%2Fl; VIEW_TKLINK_ID="jbs******@naver.com"; TKLINK_PAYCO_VIP_FLAG=false; DRTOUR=dHGkV1a6bcG1jGqC4Vz7oLl7cMcEQSkbOhspxlWlJ2Bdv%2FIKf5KYEgIfBzcmfFDBdfSi5BS8kzjDCQ7K6NA%2FSubTgb3gm3JSIh1pMS4dYP4%3D; ALBS2A39876863068=1696429685561276527; AUFBS2A39876863068=1694617200000000000|4|1694790000000000000|2|1679899592880106226; gateKey_ID=; AUBS2A39876863068=1696433681461105143%7C11%7C1694844104688221894%7C2%7C1679899592880106226%7C1; cro_uv_ymd=20231005; TKLINK_CHK=AAAA1808teBfGch2nmp1LXL_FeLYAKN07xQFmJo5-x6xKvNn9rJ3-5dFZeRjc-epF31i2M4Fm5eSHn-zqLiH-9lHsGKsiqimKpnT2g2LAsGSFSUnwnjE4NdpRsL7PA_tNuvUoyNpKolQpXA940I8OTotm8-C_7iin_URZ0eGVXUeysNGGqknkC2lSWCG1nkqS2pJikoRADERJUefsBDPI7KUxJ9L4-dsrtGUNOl1Z6abPEyuRDpgAWQdvuvmEfQXVO45bFkLMcvBESFLS_4vyQ1MhdQ0GtuKbdqt2vRnABD9dCio.YjsmhQWSEUDc44SCqcRz5sH7PNJI0FSK4lotHtdjMu2uSWR_VVVGxn1BKByGaZ-UEkEjztSWbHxOfiESCFxeSBG0hKLR7oxrRcQOcbiZS6w26uaZsWP35zEYi-bCKbWlgok8Zz6sEOJ5m6O9VdQh44aPHew1ZmP4OEH1-QNwNUGQfQebf_ADs6UVLl53rZqDrzzFzbGDkwgJh5CRRgFdA6PvZB77XSdpha-ZuekPdUatFbTIRklXA5SB6PTXQ9NvwfvDlsMm0M4qE50yzpBwMAYEykTrF9yVWv09gWfoK32Scc3KNWRFC669F3gtqDu1R2oLy6091GMKi0DAzRZraQ; _AceT=fb.2.1694002593383.938403197; JSESSIONID=E2CAA73C3009F1EEE38F441F7E52E336.WAS2; _dd_s=rum=1&id=bc41952b-8cee-4775-9cde-89dfc99bc8df&created=1696429664103&expire=1696437036071; _ga_PVZX56STJJ=GS1.1.1696433680.18.1.1696436136.59.0.0; ASBS2A39876863068=1696433681461105143%7C1696436136223834123%7C1696433681461105143%7C0%7Chttpswwwticketlinkcokrreserveplanschedule1356805670menuIndexreserve; ARBS2A39876863068=httpswwwticketlinkcokrreserveplanschedule1356805670menuIndexreservehttpswwwticketlinkcokrreserveproduct42446scheduleId1356805670',
    'Origin': 'https://www.ticketlink.co.kr',
    'Sec-Ch-Ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69',
    # 필요한 다른 헤더도 추가하세요.
}

# POST 요청을 보낼 데이터


'''
# POST 요청 보낼 URL

'''
'''


#url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/510169111/grades?_=1696215241301" 삼성
#url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/608468859/grades?_=1695963865432" #grade
##url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/613465577/grades?_=1696231635325" #기아
#url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/161457368/grades?_=1696233139540" #kt
#url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/400897953/grades?_=1696233883414" #lg
#url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/356554792/grades?_=1696234215824" #ssg
url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/1356805670/grades?_=1696431222930"
blocks = []
grades = []


idx = 0
#url = "https://www.ticketlink.co.kr/api/V2/plan/schedules/1009995215/grades?_=1695963865432" #grade
response = requests.get(url,headers=headers)
json_data = response.json()["data"]

for item in json_data:
    try:
        grade = Grade.objects.create(
            gradeId=item['gradeId'],  #ㅇㅇ
            name=item['name'],
            color=item['color'],
            price=item['price'],
        )
    except:
        grade = Grade.objects.get(gradeId=item['gradeId'])
    print("grade", idx)
    grade.save()
    idx = idx+1
    grades.append(grade)

url = "https://www.ticketlink.co.kr/reserve/plan/schedule/1356805670?menuIndex=reserve" #ssg
#url = "https://www.ticketlink.co.kr/reserve/plan/schedule/400897953?menuIndex=reserve" #lg
#url = "https://www.ticketlink.co.kr/reserve/plan/schedule/161457368?menuIndex=reserve" #kt
#url = "https://www.ticketlink.co.kr/reserve/plan/schedule/613465577?menuIndex=reserve" #기아
#url = "https://www.ticketlink.co.kr/reserve/plan/schedule/510169111?menuIndex=reserve"
#url = "https://www.ticketlink.co.kr/reserve/plan/schedule/1009995215?menuIndex=reserve"
response = requests.get(url,headers=headers)
json_data = json.loads(response.text.split("initData.meta = ")[1].split('initData.grades')[0].split(';')[0])
#json_data = response.json()["data"]
json_data = json_data["draw"]["blockInfo"] #block

for item in json_data:
    block = Block.objects.create(
        blockId=item['blockId'], #
        blockName=item['blockName']
    )
    
    linked_point = Point.objects.create(
        x=item['linkedPoint']['x'],
        y=item['linkedPoint']['y'] 
    )
    block.linkedPoint = linked_point
    
    vector_point = Point.objects.create(
        x=item['vectorPoint']['x'],
        y=item['vectorPoint']['y']
    )
    block.vectorPoint = vector_point
    
    for corner_point_data in item['cornerPoints']:
        corner_point = Point.objects.create(
            x=corner_point_data['x'],
            y=corner_point_data['y']
        )
        block.cornerPoints.add(corner_point)
    
    for grade_data in item['grades']:
        grade_id = grade_data['gradeId']
        try:
            grade = Grade.objects.get(
                gradeId=grade_id
            )
            block.grade.add(grade)
        except:
            pass
            
    print("block", idx)
    block.save()
    idx = idx + 1
    blocks.append(block)

football = Football.objects.create(
        name="대구 FC",
        eng="dgb",
)
'''
blocks = Football.objects.get(name="대구 FC").blocks.all()

for i in blocks:
    payload = str(i.blockId) 
    url = 'https://www.ticketlink.co.kr/api/V2/plan/1356805670/seat-all/canverse/block2' #ssg
    response = requests.post(url, headers=headers,data=json.dumps(payload))
    
    if response.status_code == 200:
        json_data = response.json()["data"]["able"][str(i.blockId)]
        for key, value in json_data.items():
            for item in value:
                serializer = SeatSerializer(data=item)
                if serializer.is_valid():
                    next_id =  Seat.objects.all().order_by('-id').first().id + 1
                    instance_data = serializer.validated_data
                    instance_data['id'] = next_id
                    serializer.save(id=next_id)
                else:
                    pass
                print("seat", idx)
                idx = idx + 1
    else:
        print(f"오류 응답: {response.status_code}")

