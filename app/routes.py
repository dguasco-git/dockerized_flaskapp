from flask import Blueprint, render_template, send_from_directory, jsonify, current_app
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    files = os.listdir(current_app.config['FILES_DIR'])
    return render_template('index.html', files=files)

@bp.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(current_app.config['FILES_DIR'], filename, as_attachment=True)

@bp.route('/api/files')
def api_files():
    files = os.listdir(current_app.config['FILES_DIR'])
    return jsonify(files)
