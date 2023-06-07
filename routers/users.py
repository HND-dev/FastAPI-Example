from fastapi import APIRouter, HTTPException

from models.users import UserModel

import requests

router = APIRouter(prefix= "/users")

BASEURL = "https://api.github.com/users/"

@router.get("/{username}")
async def get_user_info(username: str) -> UserModel:
    """
    Retrieve information about a GitHub user

    This endpoint send a request to the GitHub Rest API to get some information about
    an GitHub user

    This endpoint will return :
    * User login
    * User ID
    * User avatar url
    * User GitHub url
    * User name
        * Can be null depends on privacy settings of the user
    * User email
        * Can be null depends on privacy settings of the user
    * User public repo number

    """
    res = requests.get(BASEURL + username)
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 404:
        raise HTTPException(404, detail="User '" + username + "' not found")
    else:
        raise HTTPException(500, detail="Couldn't retrieve info of user '" + username + "'")