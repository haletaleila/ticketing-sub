import requests
import os
import time
# 이미지 저장할 폴더 생성
if not os.path.exists('dgb'):
    os.makedirs('dgb')

imageUrl = '//image.toast.com/aaaaab/ticketlink/TKL_CONCERT/daegu_seat_ver2023_0608_4_{x}_{y}.png'

for x in range(0,16):
    for y in range(0,16):
        # 이미지 URL 완성
        formattedUrl = imageUrl.format(x=x, y=y)
        response = requests.get('https:' + formattedUrl, stream=True)
        response.raise_for_status()

        # 파일로 저장
        with open(f'dgb/seat_{x}_{y}.png', 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        time.sleep(0.1)