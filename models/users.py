from pydantic import BaseModel

class UserModel(BaseModel):
    login: str
    id: int
    avatar_url: str
    html_url: str
    name: str | None = None
    email: str | None = None
    public_repos: int


class RepoModel(BaseModel):
    id: int
    node_id: str
    name: str
    html_url: str
    description: str | None = None
    language: str | None = None
    git_url: str
    ssh_url: str
    clone_url: str
    forks: int
    open_issues: int
    watchers: int

