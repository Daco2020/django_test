"""
Django settings for django_test project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#부모의 부모의 경로를 사용하겠다. manage.py 가 있는 위치를 베이스 위치로 사용

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3d6ayg3w6gh)e4q#*9(x#&hshx@+)l36n4l8!(sky-gbcp_&fb'
# 서버에 인증된 유저만 접근할 수 있도록 토큰을 생성하고 값을 복구할 때 사용
# 인증관련된 값에 들어가는 비밀번호 같은 것, 우리 서버에 국한됨

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# 디버그 모드 에러메시지를 상세하게 보여줌. 로컬에서 개발은 트루, 배포에는 펄스로
# 배포시에 디버그를 노출하면 취약점이 공개되기 때문에
# 성능을 저하시킬 수 있음 하여 2가지 이유로 배포시에는 false로 바꿔야함!
# 세팅 파일도 나중에는 분리해서 관리됨

ALLOWED_HOSTS = ["*"]
# 허용되는 호스트 주소, *은 모두접근

# Application definition

INSTALLED_APPS = [
   # 'django.contrib.admin',
   # 'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 추가된 앱은 이 파일에 목록을 추가해주어야 함


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
   # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# 뷰에 들어가기 전에 검증하는 과정
# 목록에 있는 곳에 하나씩 들어가 검증함


ROOT_URLCONF = 'django_test.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_test.wsgi.application'
# 웹어플리케이션서버(파이썬 스크립트 실행 프로그램) 
# 웹 서버 게이트웨이 인터페이스 -> 규약(파이썬 스크립트를 변환하여 클라이언트에게
# 전달을 돕는 규약?

# 소켓 통신에 사용되는 프로토 -> ?


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_test',
        'USER': 'root',
        'PASSWORD': 'daco2020',
        'HOST': '127.0.0.1', #로컬호스트로 사용가능
        'PORT': '3306',
	'OPTIONS': {'charset': 'utf8mb4'} #반드시 설정
    }
}
# 환경변수 방법 2가지
# my_settings.py 만들어 따로 관리
# OS env


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# 리부를 디비에 바로 넣는게 아니라 따로 저장하고 경로만 디비에 저장?


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'