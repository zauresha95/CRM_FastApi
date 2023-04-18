import re
from datetime import date, datetime
from pydantic import BaseModel, validator


class ClientCabinetSchema(BaseModel):
    """ClientCabinetSchema"""
    client_id: int
    name: str
    surname: str
    email: str
    phone: int
    date_of_birth: date
    created: date = datetime.now()
    updated: date = datetime.now()


    @validator('email')
    def check_email(cls, v):
        if not re.match('(\w|\.)+\@+[a-zA-Z]+\.[a-zA-Z]+',v):
            raise ValueError('must be mail format')
        return v.title()
    
    @validator('phone')
    def check_phone(cls, v):
        if not re.match('7\d{10}',str(v)):
            raise ValueError('must be phone format')
        return int(str(v).title())


class AdminCabinetSchema(BaseModel):
    """AdminCabinetSchema"""
    admin_id: int
    name: str
    surname: str
    email: str
    phone: int
    date_of_birth: date
    created: date = datetime.now()
    updated: date = datetime.now()

    @validator('email')
    def check_email(cls, v):
        if not re.match('(\w|\.)+\@+[a-zA-Z]+\.[a-zA-Z]+', v):
            raise ValueError('must be mail format')
        return v.title()

    @validator('phone')
    def check_phone(cls, v):
        if not re.match('7\d{10}', str(v)):
            raise ValueError('must be phone format')
        return int(str(v).title())