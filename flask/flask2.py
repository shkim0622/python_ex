from flask import Flask
import time

# Flask 애플리케이션 생성
app = Flask(__name__)

# 루트 URL에 대한 뷰 함수
@app.route('/')
def index():
    
    # 시간 측정 시작
    start_time = time.time()
    end_time = time.time()
    time_a = end_time - start_time
    print(f"응답 시간: {time_a} ")
    return "Hello, World!@@@@@@@@@@@@"

if __name__ == '__main__':
    # 애플리케이션 실행
    app.run(debug=True, host='0.0.0.0',port=5001)
