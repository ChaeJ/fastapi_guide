from fastapi import Depends, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException

bearer = HTTPBearer(auto_error=False)

def admin_validator(request:Request, credentials: HTTPAuthorizationCredentials = Depends(bearer)):
    if not credentials or credentials.scheme.lower() != "bearer":        
        raise HTTPException(status_code=403, detail="Admin privileges required")
    
    print(f"Admin only dependency called {credentials.credentials}")
    
    return True