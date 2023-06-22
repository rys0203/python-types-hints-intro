from datetime import datetime
# from typing import Union  # Python 3.9+
# from typing import Union, List # Python 3.6+
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "Michael"
    signup_ts: datetime | None = None
    # signup_ts: Union[datetime, None] = None  # Python 3.6+, Python 3.9+
    friends: list[int] = []
    # friends: List[int] = []  # Python 3.6+
    
external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)
print(user)

print(user.id)