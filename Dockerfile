# Python 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 라이브러리 설치
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Nginx 설치
RUN apt-get update && apt-get install -y nginx

# 프로젝트 파일 복사
COPY . /app/

# 포트 8000을 노출 (Gunicorn)
EXPOSE 8000

# Nginx와 Gunicorn 설정 (포트 80을 사용할 경우)
CMD ["sh", "-c", "gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 & nginx -g 'daemon off;'"]
