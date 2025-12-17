from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/live/ver.php")
def version_check():
    version = request.args.get("version", "2.19.2")
    lang = request.args.get("lang", "es")
    device = request.args.get("device", "android")
    appstore = request.args.get("appstore", "official")

    client_ip = request.headers.get("X-Forwarded-For", request.remote_addr)

    return jsonify({
        "appstore_url": "https://discord.gg/aVa8kB2t",
        "billboard_msg": "Servidor em manutencao | Server under maintenance | ...",
        "cdn_url": "https://dl.cdn.freefiremobile.com/live/ABHotUpdates/",
        "client_ip": client_ip,
        "code": 0,
        "country_code": "DO",
        "force_to_restart_app": False,
        "gdpr_version": 2,
        "is_firewall_open": False,
        "is_review_server": False,
        "is_server_open": True,
        "maintenance_announcement": "",
        "maintenance_region": "",
        "query_params": {
            "appstore": appstore,
            "device": device,
            "lang": lang,
            "version": version
        },
        "remote_option_version": "1.0.0",
        "remote_version": version,
        "server_url": "https://myfreefirehost.onrender.com/"
    })

