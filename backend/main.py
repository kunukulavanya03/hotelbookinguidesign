from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="This_Project_Defines_The_Backend_Api_For_Hotelbookinguidesign,_A_Hotel_Booking_Platform._The_Api_Is_Built_Using_Fastapi_And_Sqlalchemy,_Providing_A_Restful_Interface_For_Managing_Hotels,_Rooms,_Bookings,_And_User_Accounts._It_Is_Designed_To_Be_Consumed_By_A_React-Based_Frontend. API",
    description="Generated from Impact Analysis specifications",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "API is running",
        "endpoints": 1,
        "models": 7
    }

@app.get("/health")
def health():
    return {"status": "healthy", "service": "this_project_defines_the_backend_api_for_hotelbookinguidesign,_a_hotel_booking_platform._the_api_is_built_using_fastapi_and_sqlalchemy,_providing_a_restful_interface_for_managing_hotels,_rooms,_bookings,_and_user_accounts._it_is_designed_to_be_consumed_by_a_react-based_frontend."}

# Generated API endpoints
@app.put("/30")
def 30(id: int, item_data: schemas.FieldsCreate, db: Session = Depends(get_db)):
    # Update item
    item = db.query(models.Fields).filter(models.Fields.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item_data.dict().items():
        setattr(item, key, value)
    
    db.commit()
    db.refresh(item)
    return item



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
