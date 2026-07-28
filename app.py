import os
from flask import Flask, jsonify, render_template_string, send_from_directory

app = Flask(__name__)
PUBLIC_DIR = os.path.join(os.getcwd(), 'public')

if not os.path.exists(PUBLIC_DIR):
    os.makedirs(PUBLIC_DIR)

@app.route('/')
def index():
    with open('index.html', 'r') as f:
        return render_template_string(f.read())

@app.route('/api/files')
def list_files():
    if not os.path.exists(PUBLIC_DIR):
        return jsonify([])
    files = [f for f in os.listdir(PUBLIC_DIR) if os.path.isfile(os.path.join(PUBLIC_DIR, f))]
    return jsonify(files)

# CRITICAL: as_attachment=True forces the browser to DOWNLOAD, not open in a tab
@app.route('/public/<path:filename>')
def download_file(filename):
    return send_from_directory(PUBLIC_DIR, filename, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)