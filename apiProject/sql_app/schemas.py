from pydantic import BaseModel
from typing import List, Optional


from pydantic.types import datetime as DateTime


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserLogin(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    paniers: List["Panier"] = []
    commande: List["Commande"] = []
    class Config:
        orm_mode = True


class UserWithPaniers(User):
    paniers: List["Panier"] = []


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: int
    description: str | None = None
    image: str
    stock: int
    category_id: int|None

    def get_price(self):
        return self.price

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    category: Optional[Category]|None

    class Config:
        orm_mode = True


class PanierBase(BaseModel):
    name: str
    quantity: int
    product_id: int 
    total: int 
    payed: bool


class PanierCreate(PanierBase):
    pass

class Panier(PanierBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
    
    product: Optional[Product]
    


class CommandeBase(BaseModel):
    prix_product: int
    quantity: int
    total: int
    date: DateTime
    payed : bool
    panier : List[Panier]

    def __init__(self, **data):
        super().__init__(**data)
        self.date = DateTime.now()

    def __repr__(self):
        return f"Commande({self.id}, {self.user_id}, {self.product_id}, {self.prix_product}, {self.quantity}, {self.total}, {self.date})"


class CommandeCreate(CommandeBase):
    pass


class Commande(CommandeBase):
    id: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True

    user: Optional[User]
    product: Optional[Product]


class CodePromoBase(BaseModel):
    code: str
    name: str
    discount: int


class CodePromoCreate(CodePromoBase):
    date_start: DateTime
    date_end: DateTime


class CodePromo(CodePromoBase):
    id: int
    date_start: DateTime
    date_end: DateTime

    class Config:
        orm_mode = True
