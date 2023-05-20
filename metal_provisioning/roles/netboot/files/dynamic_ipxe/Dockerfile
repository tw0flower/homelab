FROM python:3

WORKDIR /dynamic_ipxe

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "gunicorn", "-w", "4", "app:app" ]
