import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tempfile
import pytest
from app import create_app

@pytest.fixture
def client():
    tmp_dir = tempfile.TemporaryDirectory()
    with open(os.path.join(tmp_dir.name, 'test.txt'), 'w') as f:
        f.write('hello')

    app = create_app()
    app.config['FILES_DIR'] = tmp_dir.name
    app.testing = True
    client = app.test_client()

    yield client

    tmp_dir.cleanup()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'test.txt' in response.data

def test_api_files(client):
    response = client.get('/api/files')
    assert response.status_code == 200
    assert b'test.txt' in response.data

def test_download(client):
    response = client.get('/download/test.txt')
    assert response.status_code == 200
    assert b'hello' in response.data
