from sqlalchemy.orm import Session
from . import models, auth

def create_user(db: Session, email, password):
    hashed = auth.hash_password(password)
    user = models.User(email=email, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db, email, password):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        return None
    if not auth.verify_password(password, user.password):
        return None
    return user

def create_license(db, license_data):
    license = models.License(**license_data.dict())
    db.add(license)
    db.commit()
    db.refresh(license)
    return license