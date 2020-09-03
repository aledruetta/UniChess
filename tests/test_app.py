def test_configs(config):
    assert config["DEBUG"] is False


def test_request_return_404(client):
    assert client.get("/url_not_found").status_code == 404
