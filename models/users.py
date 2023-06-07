from pydantic import BaseModel

class UserModel(BaseModel):
    login: str
    id: int
    avatar_url: str
    html_url: str
    name: str | None = None
    email: str | None = None
    public_repos: int