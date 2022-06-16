import qrcode
from flask import *
import base64

app = Flask(__name__)


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':        
        img= request.form['fn']
        res=qrcode.make(img)
        res.show()
        #encoded_qr_code = base64.b64encode(res)
        #res.save('/templates.jpg')
        return render_template('index.html', results=res.show())

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
