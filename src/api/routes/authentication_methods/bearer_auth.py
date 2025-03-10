from fastapi import HTTPException, status, APIRouter, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.utils.settings import FAKE_TOKEN

router = APIRouter()

security = HTTPBearer()


def authenticate_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials.credentials != FAKE_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid token")
    return credentials.credentials


@router.get("/bearer-auth")
def bearer_auth(token: str = Depends(authenticate_token)):
    return {"message": "Authenticated", "token": token}
