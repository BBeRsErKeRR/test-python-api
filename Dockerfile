FROM python:3.8
WORKDIR /user/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn","-c g_config.py","application:app"]