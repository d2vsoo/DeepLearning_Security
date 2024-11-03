# 모듈 불러오기
from flask import Flask, url_for, render_template, request, session, redirect
from flask_login import LoginManager

# app 인스턴스 생성 //////////////////////////////////////////////////////////
app = Flask(__name__)

# 시크릿 키
app.secret_key = '_@0339@033@33@3_'


# 로그인 매니저
# 

# 테스트용 아이디, 패스워드 ///////////////////////////////////////
ID = 'hello'
PW = 'world'
signup_id = ''
signup_password = ''


# 라우팅 /////////////////////////////////////////////////
# 메인
@app.route('/')
def main_page():
    if 'userID' in session:
        return render_template('main.html', username = session.get('userID'), login_status = True)
    else:
        return render_template('main.html', login_status = False)


# 로그인
@app.route('/login', methods = ['get'])
def login_page():
    global ID, PW, signup_id, signup_password
    
    _id_ = request.args.get('login_id')
    _password_ = request.args.get('login_pw')


    if ID == _id_ and _password_ == PW:
        # print(_id_, _password_)
        session['userID'] = _id_
        return redirect(url_for('main_page'))
    
    
    # elif로 회원가입된 상태를 불러오면 어떨까 싶었는데 잘 안됐음
    # elif _id_ == signup_id and _password_ == signup_password:
    #     # print(_id_, _password_)
    #     session['userID'] = signup_id
    #     return redirect(url_for('main_page'))
    
    
    else:
        return redirect(url_for('main_page'))


# 로그아웃
@app.route('/logout')
def logout_page():
    session.pop('userID')
    return redirect(url_for('main_page'))


# 회원가입
@app.route('/signup')
def signup_page():
    return render_template('signup.html')


# 회원가입 완료 시
@app.route('/signup_done', methods = ['get'])
def signup_done_page():
    
    # signup_name = request.args.get('signup_name')
    # signup_id = request.args.get('signup_id')
    # signup_password = request.args.get('signup_password')
    # signup_email = request.args.get('signup_email')
    
    # db 중복체크를 위한 코드
    # if DB.signup(signup_name, signup_id, signup_password, signup_email):
    #     return redirect(url_for('main_page'))
    # else:
    #     return redirect(url_for('signup_page'))
    
    # print(signup_name, signup_id, signup_password, signup_email)
    return redirect(url_for('main_page'))


# 캠 페이지
@app.route('/cam')
def cam_page():
    return render_template('cam.html')


# 히스토리 페이지
@app.route('/history')
def history_page():
    return render_template('history.html')


# 실행 /////////////////////////////////////////////////
if __name__ == '__main__':
    app.run()

