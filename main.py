#!/usr/local/bin/python3
# coding: utf-8

__author__ = "Benny <benny.think@gmail.com>"

import logging
import os
import time
from pyrogram import Client, filters, types, raw

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(filename)s [%(levelname)s]: %(message)s')

PROXY = os.getenv("PROXY")
TOKEN = os.getenv("TOKEN")
APP_ID = os.getenv("APP_ID")
APP_HASH = os.getenv("APP_HASH")

DC_MAP = {
    1: "Miami",
    2: "Amsterdam",
    3: "Miami",
    4: "Amsterdam",
    5: "Singapore"
}


def read_job():
    with open('./scraper/recent_job.txt', 'r', encoding='utf-8') as file:
        join_text = [line for line in file]
        print(join_text)
    return join_text


def create_app():
    _app = Client("./session_memory/redirect_bot",
                  'api_id',
                  'api_hash',
                  bot_token='bot token')
    if PROXY:
        _app.proxy = dict(
            scheme="socks5",
            hostname=PROXY.split(":")[0],
            port=int(PROXY.split(":")[1])
        )

    return _app


app = create_app()
service_count = 0


@app.on_message(filters.command(["start"]))
def start_handler(client: "Client", message: "types.Message"):
    chat_id = 5517438705
    client.send_message(chat_id, 'Starting to send messages!')
    while True:
        try:
            jobs = read_job()
            job_text = ''.join(jobs)
            client.send_message(chat_id, job_text)
        except Exception:
            print('No new jobs')
            client.send_message(chat_id, 'No new jobs')
        time.sleep(40)


if __name__ == '__main__':
    app.run()
