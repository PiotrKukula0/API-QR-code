from flask import Flask, request, make_response
import qrcode
import io

app = Flask(__name__)


@app.route("/qr", methods=["GET"])
def qr():
    url = request.args.get('url')
    img = qrcode.make(url)
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    response = make_response(buffer.getvalue())
    response.mimetype = 'image/png'
    response.headers["Content-Disposition"] = "attachment; filename=qr_code.png"
    return response


if __name__ == "__main__":
    app.run()
