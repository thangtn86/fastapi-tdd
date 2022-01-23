import json


def test_create_summary_201(test_app_with_db):
    resp = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"})
    )

    assert resp.status_code == 201
    assert resp.json()["url"] == "https://foo.bar"


def test_create_summary_invalid_json_422(test_app):
    resp = test_app.post("/summaries/", data=json.dumps({}))

    assert resp.status_code == 422
    assert resp.json() == {
        "detail": [
            {
                "loc": ["body", "url"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_read_summary_200(test_app_with_db):
    resp = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"})
    )
    summary_id = resp.json()["id"]

    resp = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert resp.status_code == 200

    resp_dict = resp.json()
    assert resp_dict["id"] == summary_id
    assert resp_dict["url"] == "https://foo.bar"
    assert resp_dict["summary"]
    assert resp_dict["created_at"]


def test_read_summary_404(test_app_with_db):
    resp = test_app_with_db.get("/summaries/999/")

    assert resp.status_code == 404
    assert resp.json()["detail"] == "Summary not found"


def test_read_all_summaries_200(test_app_with_db):
    resp = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar"})
    )
    summary_id = resp.json()["id"]

    resp = test_app_with_db.get("/summaries/")
    assert resp.status_code == 200

    resp_list = resp.json()
    assert len(list(filter(lambda d: d["id"] == summary_id, resp_list))) == 1
