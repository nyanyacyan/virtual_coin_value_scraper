# Pythonのベースイメージを指定
FROM python:3.10.8

# 必要なパッケージをインストール
RUN apt-get update \
    && apt-get install -y wget unzip

# 特定のバージョンのChromeをインストール
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb

# ChromeDriverのダウンロード
RUN wget -q https://chromedriver.storage.googleapis.com/117.0.5938.132/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Pythonライブラリのインストール
RUN pip install selenium
