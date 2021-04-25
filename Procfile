release: python manage.py migrate
web: bin/start-stunnel uvicorn ChatApp.asgi:application --limit-max-requests=1200 --port $PORT
