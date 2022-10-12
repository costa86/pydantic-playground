from datetime import datetime
from enum import Enum
from typing import Literal, Union
from pydantic import BaseModel, Field, EmailStr, PositiveInt, PaymentCardNumber, FutureDate, validate_arguments,\
    SecretStr, BaseSettings

from pydantic.color import Color

######

#curl -sSL https://install.python-poetry.org | POETRY_HOME=$HOME/.local/bin python3 -

class DevConfig(BaseModel):
    env: Literal["dev"]
    a: str = "dede"


class ProdConfig(BaseModel):
    env: Literal["prod"]
    c: str = "ppppppppp"
    d: str = "ooooooooooo"


class Config(BaseModel):
    config: Union[DevConfig, ProdConfig]


con = Config(config={"env": "prod"})
print(con)
#######


class License(Enum):
    GPL = "GPL"
    GPL_V3 = "GPLv3+"
    MIT = "MIT"
    MPL = "MPL 2.0"


class User(BaseSettings):
    id: int = Field(ge=1)
    rate: PositiveInt
    email: EmailStr
    friends: list[str] | int
    card: PaymentCardNumber
    some_date: FutureDate
    license: License
    password: SecretStr
    color: Color
    created_at: datetime
    # loads env var! must inherit from BaseSettings
    username: str = Field(..., env='USER')

color = "ff00ff"
color = 'hsl(180, 100%, 50%)'
# color = "dedewein"
card_number = "378282246310005"
card_number = "5105105105105100"

a = User(
    id=4,
    friends=5,
    rate=50,
    some_date=FutureDate(2022, 10, 15),
    license=License.GPL_V3,
    email=EmailStr("ana@mail.com"),
    password=SecretStr("12345"),
    color=Color(color), created_at="2022-05-05T15:15:30",
    card=card_number,
)

print(a.json())
print(a.password.get_secret_value())
print(a.color.as_named())
print(a.card.brand)



########
@validate_arguments
def sample(age: PositiveInt, name: str) -> str:
    print(f"{name} is {age} yo")
    return name

sample(50, "ana")
########