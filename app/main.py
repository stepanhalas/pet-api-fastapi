from fastapi import FastAPI

app = FastAPI()

# Фейкова база даних
pets = [
    {"id": 1, "name": "Tom", "type": "cat"},
    {"id": 2, "name": "Buddy", "type": "dog"},
]

@app.get("/")
def root():
    return {"message": "Welcome to Pet API!"}

@app.get("/pets")
def get_pets():
    return pets

@app.get("/pets/{pet_id}")
def get_pet(pet_id: int):
    for pet in pets:
        if pet["id"] == pet_id:
            return pet
    return {"error": "Pet not found"}

@app.post("/pets")
def create_pet(pet: dict):
    pet["id"] = len(pets) + 1
    pets.append(pet)
    return pet
