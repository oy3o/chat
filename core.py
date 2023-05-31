from oy3opy import *
from .channel import Channel
from .user import User
from .image import Image
from .video import Video
from .voice import Voice
from .sounds import Sounds
from .meta import Meta
from .file import File

@dataclass
class Text:
    data: str

    @property
    def type(self):
        return 'text'
    
    def __str__(self):
        return self.data

@dataclass
class Body:
    id: str
    name: str
    content: list

    def __str__(self):
        return self.name

@dataclass
class MessageBody(Body):
    channel: Channel
    user: User
    forward: str = None
    pin:bool = False

@dataclass
class Sended:
    body:Body
    def __str__(self):
        return str(self.body)

class Message(Sended):
    def __init__(self, body) -> None:
        self.body = body if isinstance(body, MessageBody) else MessageBody(**body)
    @property
    def type(self):
        return 'message'

class Notice(Sended):
    def __init__(self, body) -> None:
        self.body = body if isinstance(body, Body) else Body(**body)
    @property
    def type(self):
        return 'notice'