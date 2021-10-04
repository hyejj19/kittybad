
import json
import pyrebase


with open(r"auth/firebase.json") as f:  # 파이어베이스 주소
    config = json.load(f)
firebase = pyrebase.initialize_app(config)  # 파이어베이스 초기화 및 연동 완료
db = firebase.database()  # 파이어베이스 사용 준비 끝



def api_data(sido):
    global all_cat_id
    global all_sido
    global all_notice_day
    global all_notice_num
    global all_cat_img
    global all_cat_feature
    global all_cat_color
    global all_cat_weigth
    global all_cat_gender
    global all_care_name
    global all_care_tel
    global all_care_addr
    all_cat_id = []  # '유기번호'
    all_sido = []  # '지역'
    all_notice_day = []  # 공고일
    all_notice_num = []  # 공고 번호
    all_cat_img = []  # 고양이사진 주소
    all_cat_feature = []  # 특징
    all_cat_color = []  # 고양이 색
    all_cat_weigth = []  # 몸무게
    all_cat_gender = []  # 성별
    all_care_name = []  # 보호소 명
    all_care_tel = []  # 보호소 연락처
    all_care_addr = []  # 보호소 주소

    sido_cats_info = db.child("고양이").child(sido).get().val()
    # print(sido_cats_info)

    for sido_c_id in sido_cats_info:  # seoul_c_id 변수는 서울 고양이 유기번호를 뜻함
        sido_cat = db.child("고양이").child(sido).child(
            sido_c_id).get().val()  # 한마리 개체
        # print(sido_c_id)

        all_cat_id.append(sido_cat['유기번호'])
        all_sido.append(sido_cat['지역'])
        all_notice_day.append(sido_cat['공고일'])
        all_notice_num.append(sido_cat['공고 번호'])
        all_cat_img.append(sido_cat['고양이사진 주소'])
        all_cat_feature.append(sido_cat['특징'])
        all_cat_color.append(sido_cat['고양이 색'])
        all_cat_weigth.append(sido_cat['몸무게'])
        all_cat_gender.append(sido_cat['성별'])
        all_care_name.append(sido_cat['보호소 명'])
        all_care_tel.append(sido_cat['보호소 연락처'])
        all_care_addr.append(sido_cat['보호소 주소'])

api_data('강원도')
print(all_cat_id[0])