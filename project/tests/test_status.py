from app import main


def test_status(test_app):
    resp = test_app.get('/status')
    assert resp.status_code == 200
    assert resp.json() == {
        'status': 'OK - Healthy',
        'env': 'dev',
        'testing': True
    }
