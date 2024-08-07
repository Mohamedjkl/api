from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

def generate_random_egyptian_phone_number():
    country_code = "+20"
    valid_start_digits = ["10", "11", "12", "15"]
    start = random.choice(valid_start_digits)
    remaining_digits = ''.join(random.choices("0123456789", k=8))
    phone_number = country_code + start + remaining_digits
    return phone_number

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hi(count: int = 1):
    phone_numbers = [generate_random_egyptian_phone_number() for _ in range(count)]
    return {"phone_numbers": phone_numbers}
