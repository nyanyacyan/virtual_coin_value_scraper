# Pythonのベースイメージを指定
FROM python:3.10.8

# 必要なパッケージをインストール
# 必要最低限のものしかインストールしない。
# apt-get updateは最新のカタログのイメージ
# apt-get install -y wget unzip curl && インストールしたり、zip解凍、

RUN apt-get update && \
    apt-get install -y wget unzip curl && \
    apt-get clean && \
    apt-get install -y cron &&\
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

# pythonスクリプトとcrontabファイルをコピー
COPY main.py /app/main.py
COPY crontab /etc/cron.d/crontab

# crontabファイルの権限設定
RUN chmod 0644 /etc/cron.d/crontab

# Pythonライブラリのインストールの前にrequirements.txtをコピー
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# cronのデーモンを実行するためのエントリポイントセットアップ
CMD ["cron", "-f"]
