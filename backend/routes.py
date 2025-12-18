from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="")

@router.get("/hotels")
def hotels(db: Session = Depends(get_db)):
    # TODO: Implement logic for /hotels
    return {"message": "Stub for /hotels", "method": "GET"}

@router.get("/bookings")
def bookings(db: Session = Depends(get_db)):
    # TODO: Implement logic for /bookings
    return {"message": "Stub for /bookings", "method": "GET"}

@router.get("/hotels/search")
def hotels_search(db: Session = Depends(get_db)):
    # TODO: Implement logic for /hotels/search
    return {"message": "Stub for /hotels/search", "method": "GET"}

@router.get("/hotel/{id}")
def hotel_{id}(db: Session = Depends(get_db)):
    # TODO: Implement logic for /hotel/{id}
    return {"message": "Stub for /hotel/{id}", "method": "GET"}

@router.post("/bookings")
def bookings(db: Session = Depends(get_db)):
    # TODO: Implement logic for /bookings
    return {"message": "Stub for /bookings", "method": "POST"}
