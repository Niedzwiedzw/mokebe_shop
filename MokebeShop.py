from subprocess import call
import webbrowser

PYTHON_PATH = 'python3.6'
BASE_IP = '127.0.0.1:8080'

webbrowser.open('http://' + BASE_IP)
call([PYTHON_PATH, 'manage.py', 'runserver', BASE_IP])


