from fastapi import Header, HTTPException

def get_current_user(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Missing API key")
    return x_api_key
