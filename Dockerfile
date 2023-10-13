# Pythonのベースイメージを指定
FROM python:3.10.8

# 今回の要件にあった必要なパッケージをインストール


RUN apt-get update && \
    apt-get install -y wget unzip curl && \
    apt-get clean && \
    apt-get install -y cron &&\
    rm -rf /var/lib/apt/lists/*

# dockerコンテナ内に特定のバージョンのChromeをインストール
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

# ディレクトリにある全てのファイルをdockerコンテナ内にコピーする
COPY main.py /app/main.py
COPY scraper.py /app/scraper.py
COPY SpreadsheetAppender.py /app/SpreadsheetAppender.py
COPY crontab /etc/cron.d/crontab

# crontabファイルの権限設定
RUN chmod 0644 /etc/cron.d/crontab

# Pythonライブラリのインストールの前にrequirements.txtをコピー
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# cronのデーモンを実行するためのエントリポイントセットアップ
# -fはフォアグランドモード＝プロセスを終了しないでおくこと これがないと1回実施したら終了してしまうため
CMD ["cron", "-f"]
