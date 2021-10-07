# pip install xmltodict
import json
from xml.sax.saxutils import escape
import xmltodict
from bs4 import BeautifulSoup
import urllib.request
import pyrebase
import datetime


with open(r"auth/firebase.json") as f:  # 파이어베이스 주소
    config = json.load(f)
firebase = pyrebase.initialize_app(config)  # 파이어베이스 초기화 및 연동 완료
db = firebase.database()  # 파이어베이스 사용 준비 끝


# 현재 시간
current_datetime = datetime.datetime.now()
end_dateformat = '%Y%m%d'
end_day = current_datetime.strftime(end_dateformat)  # 현재날짜 ex)20211004
end_day = 20211004

start_dateformat = '%Y0101'
start_day = current_datetime.strftime(start_dateformat)
start_day = 20210704


try:

    for pageNo in range(1, 9999):  # 페이지 수
        url = f'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?ServiceKey=idawDPFYjt9%2BU6pv58Er11N0nrTks8dwI9b8enxlEZLhShOoFG%2Ff3ZRVaGnR%2FWt8PcOVUzLkcknK54sG%2Fa0Bkg%3D%3D&bgnde={start_day}&endde={end_day}&upkind=422400&pageNo={pageNo}'
        request = urllib.request.urlopen(url)
        # url 주소를 파일 형태로 읽음
        xmlString = request.read()

        # xml 파일을 json 파일로 변환
        xml_parse = xmltodict.parse(xmlString)
        xml_dict = json.loads(json.dumps(xml_parse))
        # print(type(xml_dict))

        for i in range(0, 10):   # 한 페이지에 고양이를 10개씩 소개함
            # 보호 상태
            state = xml_dict['response']['body']['items']['item'][i]['processState']

            if state == '보호중':
                # 특징
                cat_feature = xml_dict['response']['body']['items']['item'][i]['specialMark']
                # 유기번호
                cat_id = xml_dict['response']['body']['items']['item'][i]['desertionNo']
                sido = xml_dict['response']['body']['items']['item'][i]['orgNm'].split()[
                    0]  # 지역 시, 도
                # 공고일
                notice_day = xml_dict['response']['body']['items']['item'][i]['noticeSdt']
                # 공고 번호
                notice_num = xml_dict['response']['body']['items']['item'][i]['noticeNo']
                # 고양이 사진 주소
                cat_img = xml_dict['response']['body']['items']['item'][i]['popfile']
                # 특징
                cat_feature = xml_dict['response']['body']['items']['item'][i]['specialMark']
                # 고양이 색
                cat_color = xml_dict['response']['body']['items']['item'][i]['colorCd']
                # 몸무게
                cat_weigth = xml_dict['response']['body']['items']['item'][i]['weight']
                # 성별
                cat_gender = xml_dict['response']['body']['items']['item'][i]['sexCd']
                if cat_gender == 'F':
                    cat_gender = '암컷'
                else:
                    cat_gender = "수컷"

                # 보호소 명
                care_name = xml_dict['response']['body']['items']['item'][i]['careNm']
                # 보호소 연락처
                care_tel = xml_dict['response']['body']['items']['item'][i]['careTel']
                # 보호소 주소
                care_addr = xml_dict['response']['body']['items']['item'][i]['careAddr']

                cat_infor = {
                    '유기번호':  cat_id,
                    '지역': sido,
                    '공고일': notice_day,
                    '공고 번호': notice_num,
                    '고양이사진 주소': cat_img,
                    '특징': cat_feature,
                    '고양이 색': cat_color,
                    '몸무게': cat_weigth,
                    '성별': cat_gender,
                    '보호소 명': care_name,
                    '보호소 연락처': care_tel,
                    '보호소 주소': care_addr
                }

                print('num', pageNo, i, cat_id, cat_img)

                db.child("고양이").child(sido).child(
                    '유기번호').child(cat_id).set(cat_infor)
except:
    print("완료")

print("굳")
