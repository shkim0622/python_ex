from flask import Flask

# Flask 애플리케이션 생성
app = Flask(__name__) 

#해당 URL에 대한 뷰 함수를 지정
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    # 애플리케이션 실행
    app.run(debug=True, port=5000)
