from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Hotelbookinguidesign_Is_A_Backend_Api_Designed_To_Support_The_Frontend_Application_Developed_With_React._The_Backend_Will_Use_Fastapi_For_Its_Lightweight_And_Fast_Performance,_Paired_With_Sqlalchemy_For_Database_Operations._This_Api_Will_Handle_User_Authentication,_Booking_Management,_And_Room_Availability. API",
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
    return {"status": "healthy", "service": "hotelbookinguidesign_is_a_backend_api_designed_to_support_the_frontend_application_developed_with_react._the_backend_will_use_fastapi_for_its_lightweight_and_fast_performance,_paired_with_sqlalchemy_for_database_operations._this_api_will_handle_user_authentication,_booking_management,_and_room_availability."}

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
