"""
Django settings for meiduo_mall project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g*y102s37hy9i4t5fpms@-s6jj=fhf1&9+18*s7k!n2-kx=y(%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['api.meiduo.site', '127.0.0.1', 'localhost', 'www.meiduo.site']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
    'xadmin',
    'crispy_forms',
    'reversion',
    'django_crontab',  # 定时任务
    'corsheaders',
    'rest_framework',
    'users.apps.UsersConfig',
    'verifications.apps.VerificationsConfig',
    'oauth.apps.OauthConfig',
    'areas.apps.AreasConfig',
    'contents.apps.ContentsConfig',
    'goods.apps.GoodsConfig',
    'carts.apps.CartsConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'meiduo_mall.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'meiduo_mall.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '192.168.42.134',  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'meiduo',  # 数据库用户名
        'PASSWORD': 'meiduo',  # 数据库用户密码
        'NAME': 'meiduo_mall'  # 数据库名字
    },
    # mysql slave
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '192.168.42.134',  # 数据库主机
        'PORT': 8306,  # 数据库端口
        'USER': 'root',  # 数据库用户名
        'PASSWORD': 'mysql',  # 数据库用户密码
        'NAME': 'meiduo_mall'  # 数据库名字
    }
}

# redis config
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.42.134:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # session
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.42.134:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 验证码
    "verify_codes": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.42.134:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 浏览记录
    "history": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.42.134:6379/3",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    # 购物车
    "cart": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.42.134:6379/4",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'


# logs conf

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/meiduo.log"),  # 日志文件的位置
            'maxBytes': 50 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],
            'propagate': True,
        },
    }
}
# 用户模型制定
AUTH_USER_MODEL = 'users.User'

AUTHENTICATION_BACKENDS = [
    'users.utils.UsernameMobileAuthBackend',
]

REST_FRAMEWORK = {
    # 异常处理类
    'EXCEPTION_HANDLER': 'meiduo_mall.utils.exceptions.exception_handler',
    # 认证
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 分页
    'DEFAULT_PAGINATION_CLASS': 'meiduo_mall.utils.pagination.StandardResultsSetPagination',
}

# JWT有效期
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'users.utils.jwt_response_payload_handler',  # JWT登陆认证
}

# cors 白名单策略
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8080',
    'localhost:8080',
    'www.meiduo.site:8080',
    'api.meiduo.site:8000'
)
CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

# QQ登录参数
QQ_CLIENT_ID = '101474184'
QQ_CLIENT_SECRET = 'c6ce949e04e12ecc909ae6a8b09b637c'
QQ_REDIRECT_URI = 'http://www.meiduo.site:8080/oauth_callback.html'
QQ_STATE = '/index.html'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
#发送邮件的邮箱
EMAIL_HOST_USER = '2411534723@qq.com'
#在邮箱中设置的客户端授权密码
EMAIL_HOST_PASSWORD = 'gyihyfpymrftdjdi'
#收件人看到的发件人
EMAIL_FROM = '美多商场<2411534723@qq.com>'

# DRF缓存扩展
REST_FRAMEWORK_EXTENSIONS = {
    #缓存时间
    "DEFAULT_CACHE_RESPONE_TIMEOUT": 60*60,
    # 缓存存储
    "DEFAULT_USE_CACHE":"default",
}


# django文件存储
DEFAULT_FILE_STORAGE = 'meiduo_mall.utils.fastdfs.fdfs_storage.FastDFSStorage'

# FastDFS
FDFS_URL = 'http://image.meiduo.site:8888/'  
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')


# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',  # 工具条功能
        'height': 300,  # 编辑器高度
        # 'width': 300,  # 编辑器宽
    },
}
CKEDITOR_UPLOAD_PATH = ''  # 上传图片保存路径，使用了FastDFS，所以此处设为''

# 生成的静态html文件保存目录
GENERATED_STATIC_HTML_FILES_DIR = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc')


# 定时任务
CRONJOBS = [
    # 每5分钟执行一次生成主页静态文件
    # ('*/5 * * * *', 'contents.crons.generate_static_index_html', '>> /Users/delron/Desktop/meiduo_mall/logs/crontab.log')
    ('*/5 * * * *', 'contents.crons.generate_static_index_html', '>>' + os.path.join(os.path.dirname(BASE_DIR), "logs/crontab.log")),
]


# 解决crontab中文问题
CRONTAB_COMMAND_PREFIX = 'LANG_ALL=zh_cn.UTF-8'

# Haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://192.168.42.133:9200/',  # 此处为elasticsearch运行的服务器ip地址，端口号固定为9200
        'INDEX_NAME': 'meiduo',  # 指定elasticsearch建立的索引库的名称
    },
}

# 当添加、修改、删除数据时，自动生成索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 支付宝
ALIPAY_APPID = '2016081600258081'
ALIPAY_DEBUG = True
ALIPAY_URL = 'https://openapi.alipaydev.com/gateway.do'

# 配置读写分离
DATABASE_ROUTERS = ['meiduo_mall.utils.db_router.MasterSlaveDBRouter']

# 收集静态文件的保存目录
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'front_end_pc/static')
