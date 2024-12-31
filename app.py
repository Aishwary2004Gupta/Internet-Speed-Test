from flask import Flask, jsonify
import speedtest

app = Flask(__name__)

def bytes_to_mb(bytes):
    KB = 1024
    MB = KB * 1024
    return round(bytes / MB, 2)

@app.route('/api/speedtest', methods=['GET'])
def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.get_servers()
        st.get_best_server()
        download_speed = bytes_to_mb(st.download())
        upload_speed = bytes_to_mb(st.upload())
        ping = st.results.ping
        return jsonify({
            "download_speed": download_speed,
            "upload_speed": upload_speed,
            "ping": ping
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
