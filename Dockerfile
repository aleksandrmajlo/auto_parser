FROM python:3.11-bullseye

# Установим Chromium и chromedriver
RUN apt-get update && apt-get install -y \
    chromium chromium-driver fonts-liberation libappindicator3-1 libasound2 \
    libatk-bridge2.0-0 libatk1.0-0 libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 \
    libnspr4 libnss3 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 \
    xdg-utils libu2f-udev libvulkan1 libglib2.0-0 libpango-1.0-0 libxshmfence1 \
    libgbm1 libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

ENV CHROME_BIN="/usr/bin/chromium"
ENV CHROMEDRIVER_PATH="/usr/bin/chromedriver"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]