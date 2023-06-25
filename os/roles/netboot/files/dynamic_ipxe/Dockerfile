FROM python:3

WORKDIR /dynamic_ipxe

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000/tcp

CMD [ "gunicorn", "--bind=0.0.0.0", "-w", "4", "app:app" ]    
