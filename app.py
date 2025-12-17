from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/live/ver.php')
def version_check():
    version = request.args.get('version', '2.19.2')
    lang = request.args.get('lang', 'es')
    device = request.args.get('device', 'android')

    return jsonify({
        "appstore_url": "https://tu-discord.com",
        "billboard_msg": "Bienvenido a mi server privado!",
        "cdn_url": "https://dl.cdn.freefiremobile.com/live/ABHotUpdates/",
        "code": 0,
        "force_to_restart_app": False,
        "is_server_open": True,
        "remote_version": version,
        "server_url": "https://tu-login-custom.com/",
        "query_params": {
            "device": device,
            "lang": lang,
            "version": version
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
