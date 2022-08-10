import datetime

from flask import Flask, render_template, jsonify, request, session, url_for, redirect

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
# client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('account.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/newaccount')
def newaccount():
    return render_template('newaccount.html')


# 회원가입
@app.route('/login', methods=['POST'])
def account_login():
    existing_user = db.login.find_one({'id': request.form['id_give']})

    if existing_user is None:
        id_receive = request.form['id_give']
        pw_receive = request.form['pw_give']
        pw1_receive = request.form['pw1_give']
        if id_receive == "":

            return jsonify({'result': 'fail', 'msg': '아이디를 입력하세요!'})
        elif pw_receive == "":

            return jsonify({'result': 'fail', 'msg': '비밀번호를 입력하세요!'})
        elif not pw_receive == pw1_receive:
            return jsonify({'result': 'fail', 'msg': '비밀번호가 일치하지 않습니다!'})
        else:
            user = {
                'id': id_receive,
                'pw': pw_receive
            }
            db.login.insert_one(user)
            return jsonify({'result': 'success', 'msg': '회원가입 완료!'})

    return jsonify({'result': 'fail', 'msg': '이미 있는 아이디 입니다!'})


# 로그인
@app.route('/login1', methods=['POST'])
def account1_login():
    existing_id = db.login.find_one({'$and': [{'id': request.form['id_give1']}, {'pw': request.form['pw_give1']}]})

    if existing_id is not None:
        return jsonify({'result': 'success'})
    return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# # 로그아웃
# @app.route('/logout')
# def logout():
#     session.pop('id', None)
#     return render_template('account.html')

# 삭제하기
@app.route('/delete', methods=['POST'])
def delete():
    date_receive = request.form['date_give']
    name_receive = request.form['name_give']
    code_receive = request.form['code_give']
    delete1 = db.orders.find_one({'$and': [{'date': date_receive}, {'name': name_receive}, {'code': code_receive}]})
    if date_receive == "" or name_receive == "" or code_receive == "":
        return jsonify({'result': 'fail', 'msg': '입력 정보가 부족합니다.'})
    else:
        if delete1 is None:
            return jsonify({'result': 'fail', 'msg': '일치하는 데이터가 없습니다'})
        else:
            db.orders.delete_one({'$and': [{'date': date_receive}, {'name': name_receive}, {'code': code_receive}]})
            return jsonify({'result': 'success', 'msg': '삭제 완료!'})


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    code_receive = request.form['code_give']
    if name_receive == "":
        return jsonify({'result': 'fail', 'msg': '이름을 적으세요'})
    elif count_receive == "-- 점수 --":
        return jsonify({'result': 'fail', 'msg': '점수를 입력하세요'})
    elif address_receive == "":
        return jsonify({'result': 'fail', 'msg': '종목을 적으세요'})
    elif code_receive == "":
        return jsonify({'result': 'fail', 'msg': '삭제코드를 입력하세요'})
    else:
        doc = {
            'date': datetime.date.today().strftime("%Y/%m/%d"),
            'name': name_receive,
            'count': count_receive,
            'address': address_receive,
            'phone': phone_receive,
            'code': code_receive

        }
        db.orders.insert_one(doc)
        return jsonify({'result': 'success', 'msg': '등록 완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # page = request.args.get('page', type=int, default=1)
    # orders1 = db.orders.find({}, {'_id' : False})
    # orders = orders1.pagination(page, per_page=10, error_out=False)
    # return jsonify({'result': 'success', 'orders': orders})
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
