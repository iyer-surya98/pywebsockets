from typing import Optional
from pydantic import BaseModel


class WebSocketConnectionResponse(BaseModel):
    ok: bool
    secure: bool
    error: Optional[str] = None
    request_url: str
