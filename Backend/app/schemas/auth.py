from pydantic import BaseModel ,Field , EmailStr  , ValidationInfo , field_validator , model_validator


class LoginRequest(BaseModel):
    email: EmailStr
    password:str = Field(...,min_length=6 , max_length=128)


class SignupRequest(BaseModel):
    name:str= Field(...,min_length=4 , max_length=20)
    email: EmailStr
    password:str = Field(...,min_length=6 , max_length=128)
    confirm_password:str = Field(...,min_length=6 , max_length=128)

    @model_validator(mode="after")
    def check_password_match(self):
        if self.password != self.confirm_password:
            raise ValueError("password do not match")
        return self

