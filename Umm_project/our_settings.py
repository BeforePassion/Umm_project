MY_DATABASE = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sys',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': 'database-2.clsjddrfobqa.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

Django_Secret_Key = {
    'django-insecure-2f4q)faq*4%*wtd5rz)dtd8^pou_)x25%b3r0t(x*w!m!_r&2b'
}