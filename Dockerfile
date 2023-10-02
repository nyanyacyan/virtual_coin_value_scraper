# Pythonのベースイメージを指定
FROM python:3.10.8

# 必要なパッケージをインストール
RUN apt-get update && \
    apt-get install -y wget unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 特定のバージョンのChromeをインストール
RUN curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || true && \
    apt-get update && \
    apt-get install -f -y && \
    rm google-chrome-stable_current_amd64.deb

# ChromeDriverのダウンロード
RUN wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Pythonライブラリのインストール
RUN pip install selenium gspread APScheduler requests