def test_obtain_websocket_connection(client, url):
    connection = client.connect(url)
    assert connection.ok


def test_url_scheme_is_insecure(client, url):
    connection = client.connect(url)
    assert not connection.secure


def test_handle_ws_url_scheme(client):
    ws_url = "ws://host:8080/resource"
    connection = client.connect(ws_url)
    assert connection.ok
    assert connection.request_url == "http://host:8080/resource"
