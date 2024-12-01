# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : main.py                 #
# ----------------------------------------------- #

# from handler import send_alert
import config
import time
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_timestamp():
    timestamp = time.strftime("%Y-%m-%d %X")
    return timestamp


@app.post("/api/webhook")
def webhook():
    # 配置能回调本接口的IP白名单, 不在这里面的都直接返回401, 下面这四个IP是TradingView官方的
    whitelisted_ips = ['52.89.214.238', '34.212.75.30', '54.218.53.128', '52.32.178.7']
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if client_ip not in whitelisted_ips:
        return jsonify({'message': 'Unauthorized'}), 401
    try:
        if request.method == "POST":
            data = request.get_json()
            if data["key"] == config.sec_key:
                print(get_timestamp(), "Alert Received & Sent!")
                # TODO: 解析请求体, 通过ccxt向交易所 发起交易
                return jsonify({'message': 'Webhook received successfully'}), 200
            else:
                print("[X]", get_timestamp(), "Alert Received & Refused! (Wrong Key)")
                return jsonify({'message': 'Unauthorized'}), 401

    except Exception as e:
        print("[X]", get_timestamp(), "Error:\n>", e)
        return jsonify({'message': 'Error'}), 400
    
@app.post("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    from waitress import serve
    print("[*]", get_timestamp(), "Server Started!")
    serve(app, host="0.0.0.0", port=8080)
