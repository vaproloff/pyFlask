from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    username: str = Field(..., title="Name", max_length=100)
    email: EmailStr = Field(..., title="Email", max_length=120)


class UserIn(BaseModel):
    username: str = Field(..., title="Name", max_length=100)
    email: EmailStr = Field(..., title="Email", max_length=120)
    password: str = Field(..., title="Password", min_length=6, max_length=20)
