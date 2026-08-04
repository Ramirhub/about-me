import os
from flask import Flask, jsonify, render_template_string, send_from_directory, request

app = Flask(__name__)
PUBLIC_DIR = os.path.join(os.getcwd(), 'public')
if not os.path.exists(PUBLIC_DIR):
    os.makedirs(PUBLIC_DIR)

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return render_template_string(f.read())

# Route to serve the single pics.rar file
@app.route('/download/rar')
def download_rar():
    return send_from_directory(PUBLIC_DIR, 'pics.rar', as_attachment=True)

# Route to check the verification code
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    user_code = data.get('code', '').strip().upper()
    
    if user_code == 'XPEU7X':
        return jsonify({'success': True})
    else:
        return jsonify({'success': False})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)