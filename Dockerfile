FROM python:3.10

# 컨테이너 내 프로젝트 root directory 설정
WORKDIR /app

# 필요한 module 설치
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 프로젝트 코드 복사
COPY . .

# Django 프로젝트에서 정적 파일 수집
RUN python manage.py collectstatic --noinput

# 포트 설정
EXPOSE 8000

# gunicorn 실행 (옵션: --workers 프로세스 수 설정)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "mysite.wsgi:application"]
