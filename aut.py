import time
from seleniumwire import webdriver

"""
options = {
    'proxy': {
        'http': 'http://tdt1RvAi59:VtSlkEIrJt@212.115.44.178:58542', 
        'https': 'https://tdt1RvAi59:VtSlkEIrJt@212.115.44.178:58542',
        'no_proxy': 'localhost,127.0.0.1' # excludes
    }
}

"""

options = {
    'proxy': {
        'https': 'https://tdt1RvAi59:VtSlkEIrJt@212.115.44.178:58542'
    }
}



browser = webdriver.Chrome('D:\\t_t\\chromedriver.exe', seleniumwire_options=options)

time.sleep(9)
browser.get('https://www.myip.com/')
print('esperar..')
time.sleep(9)