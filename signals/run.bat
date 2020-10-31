@ECHO OFF
start "Chrome" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" "http://127.0.0.1:8000"
ECHO Congratulations!
python manage.py runserver 8000

pause