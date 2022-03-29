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

    