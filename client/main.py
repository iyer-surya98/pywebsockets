from dataclasses import dataclass, field
from client.schemas import WebSocketConnectionResponse


@dataclass
class WebSocketClient:
    _secure: bool = False
    _request_url: str = field(default_factory=str)

    def connect(self, url: str) -> WebSocketConnectionResponse:
        self._request_url = url
        if url.startswith("http:"):
            self._secure = False
        elif url.startswith("https:"):
            self._secure = True
        elif url.startswith("ws:"):
            self._secure = False
            self._request_url = url.replace("ws:", "http:")
        else:
            raise ValueError("Provided URL must have schemes http:, https: or ws:")
        return WebSocketConnectionResponse(
            ok=True, secure=self._secure, request_url=self._request_url
        )
