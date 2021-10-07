import re
from flask import Flask, render_template, request, url_for, redirect, session, jsonify
import pyrebase
import json
import datetime


with open(r"auth/firebase.json") as f:  # 파이어베이스 주소
    config = json.load(f)

firebase = pyrebase.initialize_app(config)  # 파이어베이스 초기화 및 연동 완료
db = firebase.database()  # 파이어베이스 사용 준비 끝

# db에 저장하는 방법
# information = {"id": "abc", "pwd": 12356}
# db.child("user").child("good").set(signin)


app = Flask(__name__)
app.secret_key = "asfasdfsdagdfhsa"  # 시크릿 키


# # api data 함수
# def api_data(sido):
#     global all_cat_id
#     global all_sido
#     global all_notice_day
#     global all_notice_num
#     global all_cat_img
#     global all_cat_feature
#     global all_cat_color
#     global all_cat_weigth
#     global all_cat_gender
#     global all_care_name
#     global all_care_tel
#     global all_care_addr
#     all_cat_id = []  # '유기번호'
#     all_sido = []  # '지역'
#     all_notice_day = []  # 공고일
#     all_notice_num = []  # 공고 번호
#     all_cat_img = []  # 고양이사진 주소
#     all_cat_feature = []  # 특징
#     all_cat_color = []  # 고양이 색
#     all_cat_weigth = []  # 몸무게
#     all_cat_gender = []  # 성별
#     all_care_name = []  # 보호소 명
#     all_care_tel = []  # 보호소 연락처
#     all_care_addr = []  # 보호소 주소

#     sido_cats_info = db.child("고양이").child(sido).get().val()
#     # print(sido_cats_info)

#     for sido_c_id in sido_cats_info:  # sido_c_id 변수는 sido에 해당하는 모든 고양이 유기번호를 뜻함
#         sido_cat = db.child("고양이").child(sido).child(sido_c_id).get().val()  # 한마리 개체
#         # print(sido_c_id)

#         all_cat_id.append(sido_cat['유기번호'])
#         all_sido.append(sido_cat['지역'])
#         all_notice_day.append(sido_cat['공고일'])
#         all_notice_num.append(sido_cat['공고 번호'])
#         all_cat_img.append(sido_cat['고양이사진 주소'])
#         all_cat_feature.append(sido_cat['특징'])
#         all_cat_color.append(sido_cat['고양이 색'])
#         all_cat_weigth.append(sido_cat['몸무게'])
#         all_cat_gender.append(sido_cat['성별'])
#         all_care_name.append(sido_cat['보호소 명'])
#         all_care_tel.append(sido_cat['보호소 연락처'])
#         all_care_addr.append(sido_cat['보호소 주소'])


# 대문 페이지
@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")  # index.html(대문 페이지)을 열어


# 지역 세부 페이지
@app.route("/regions", methods=['GET'])
def move_regions():
    return render_template("regions.html")  # regions.html(지역 세부페이지)을 열어


# 로그인 페이지
@app.route("/login")
def login():
    if "uid" in session:  # 세션안에 유저 아이디가 있을 경우  (= 로그인이 유지가 된 상태)
        return render_template("index.html")
        # 로그인 페이지로 접속해도 강제적으로 대문페이지로 보냄

    else:  # 세션안에 유저 아이디가 없는 경우 (로그인이 안되어있는 상태)
        return render_template("login.html")  # 로그인 안되어있으면 로그인 페이지로 가


# 로그인 기능
@app.route("/login_done", methods=['POST', 'GET'])
def login_done():
    uid = request.form['uid']  # login.html(로그인 페이지)에서 받아온 아이디 값
    pwd = request.form['pwd']  # login.html(로그인 페이지)에서 받아온 비밀번호 값
    users = db.child('users').get().val()  # 데이터베이스에서 유저 id 값들을 딕셔너리형태로 반환
    if users == None:   # 데이터베이스에 유저 id 값이 아무것도 없을 경우
        return redirect(url_for('login'))  # 로그인 페이지로 머물러있어

    else:  # 데이터베이스에 유저 id 값이 아무거나 한개라도 있을 경우
        try:  # 예외 처리  (try의 내부 코드들을 실행하고 에러 발생시 except의 내부 코드 실행)

            # 데이터베이스안에 있는 id 값 중에서 로그인 페이지에 받아온 id 값이 있는지 없는지 비교. 없으면 에러가 발생하고 'excetp'로 넘어감. 있으면 userinfo 변수에 id 값아 저장되고 if 문으로 넘어감
            userinfo = users[uid]
            if userinfo['pwd'] == pwd:  # 유저 id 값의 비밀번호가 맞는지 안맞는지 비교
                # 비밀번호가 일치하면 세션에 유저 아이디 정보를 넣어서 로그인 상태로 유지시킴
                session['uid'] = uid

                # 로그인 완료 했으니 index.html(대문페이지)로 보냄
                return redirect(url_for('index'))

            else:  # 비밀번호가 일치하지 않을 경우
                return redirect(url_for('login'))  # 로그인 페이지에 계속 머무르게 함
        except:  # 에러 발생시 작동    # 로그인 페이지에서 입력한 id 값이 데이터베이스에 없을 경우 에러가 남.
            return redirect(url_for('login'))  # 로그인 페이지에 계속 머무르게 함


# 로그인 유지상태 확인
@app.route('/log_maintain')
def log_maintain():
    if "uid" in session:
        return jsonify({'login': 'True'})


# 로그아웃
@app.route("/log_out", methods=['get'])
def login_out():
    session.pop("uid")  # 세션에 아이디 정보를 삭제
    return redirect(url_for("index"))  # 대문 페이지로 가


# 회원가입 페이지
@app.route("/signup")
def signup():
    return render_template("/signup.html")


# 회원가입 기능
@app.route("/signup_done", methods=['POST'])
def signup_done():
    uid = request.form['uid']  # join.html에서 id에 입력한 값을 가져옴
    pwd = request.form['pwd']  # join.html에서 pwd에 입력한 값을 가져옴
    email = request.form['email']  # join.html에서 email에 입력한 값을 가져옴
    name = request.form['name']  # join.html에서 name에 입력한 값을 가져옴

    information = {
        "pwd": pwd,
        'email': email,
        'name': name
    }

    users = db.child('users').get().val()  # 데이터베이스에서 유저 id 값들을 딕셔너리형태로 반환

    if users == None:  # 데이터 베이스에 아무것도 없을 경우
        db.child("users").child(uid).set(information)  # 데이터 베이스에 아이디 및 개인정보 추가
        return redirect(url_for("index"))  # 회원가입 완료했으면 index 페이지로 가
    else:  # 데이터 베이스에 아무 자료라도 있을 경우
        for i in users:  # 데이터베이스에 있는 모든 유저 id 값을 한개씩 i 값에 대입
            if uid == i:  # 데이터베이스에 있는 모든 유저 id 갑 중에서 회원가입하려는 id 값이 있을 경우
                return redirect(url_for("signup"))  # 회원 가입 페이지에 그대로 유지
            else:  # 데이터 베이스에 있는 모든 유저 id 값 중에서 회원가입하려는 id 값이 없을 경우
                db.child("users").child(uid).set(
                    information)  # 데이터베이스에 아이디 및 개인정보 추가
                return redirect(url_for("index"))  # 회원 가입 완료했으니 index 페이지로 가


#  api 시도 받는 역할
@app.route('/cat_card_sido', methods=['GET', 'POST'])
def cat_card_sido():
    global sido
    sido = request.args.get('sido_give')
    return sido

# api 정보 보내주는 역할


@app.route('/cat_list_info', methods=['GET', 'POST'])
def cat_list_info():
    sido_cats_info = db.child("고양이").child(sido).child('유기번호').get().val()
    return jsonify({'msg': dict(sido_cats_info)})


# 카드 리스트 페이지
@app.route('/cat_list', methods=['GET', 'POST'])
def cat_list():
    return render_template('/cat_list.html')

# Cat Test ~ 1   Result1~7 페이지


@app.route("/cat_test")
def cat_test():
    return render_template("cat_test.html")


@app.route("/cat_test1")
def cat_test1():
    return render_template("cat_test1.html")


@app.route("/result1")
def result1():
    return render_template("result1.html")


@app.route("/result2")
def result2():
    return render_template("result2.html")


@app.route("/result3")
def result3():
    return render_template("result3.html")


@app.route("/result4")
def result4():
    return render_template("result4.html")


@app.route("/result5")
def result5():
    return render_template("result5.html")


@app.route("/result6")
def result6():
    return render_template("result6.html")


@app.route("/result7")
def result7():
    return render_template("result7.html")


@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
