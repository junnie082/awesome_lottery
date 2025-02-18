# 베이스 이미지로 Amazon Linux 사용
FROM public.ecr.aws/amazonlinux/amazonlinux:latest

# 필수 패키지 업데이트 및 설치
RUN yum update -y && \
    yum install -y httpd \
    python3 \
    python3-pip \
    git

# Django와 필요한 Python 패키지 설치
RUN pip3 install --upgrade pip
RUN pip3 install django mod_wsgi

# Django 프로젝트 파일을 컨테이너로 복사 (현재 디렉토리의 Django 프로젝트를 복사)
COPY . /var/www/django_project

# Django 프로젝트 디렉토리로 이동
WORKDIR /var/www/django_project

# Django 애플리케이션을 위한 설정
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate

# Apache 설정을 위한 WSGI 설정 파일 복사 (필요 시 Django 프로젝트에 맞게 수정)
COPY ./apache-config.conf /etc/httpd/conf.d/

# Apache 서버 실행을 위한 설정 파일
RUN echo 'mkdir -p /var/run/httpd' >> /root/run_apache.sh && \
    echo 'mkdir -p /var/lock/httpd' >> /root/run_apache.sh && \
    echo '/usr/sbin/httpd -D FOREGROUND' >> /root/run_apache.sh && \
    chmod 755 /root/run_apache.sh

# 80번 포트 노출
EXPOSE 80

# Apache 실행
CMD /root/run_apache.sh
