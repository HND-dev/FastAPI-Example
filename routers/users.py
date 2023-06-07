from fastapi import APIRouter, HTTPException

from models.users import UserModel

import requests

router = APIRouter(prefix= "/users")

BASEURL = "https://api.github.com/users/"

@router.get("/{username}")
async def get_user_info(username: str) -> UserModel:
    res = requests.get(BASEURL + username)
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 404:
        raise HTTPException(404, detail="User '" + username + "' not found")
    else:
        raise HTTPException(500, detail="Couldn't retrive info of user '" + username + "'")