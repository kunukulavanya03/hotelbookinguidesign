from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="")

@router.put("/out")
def out(db: Session = Depends(get_db)):
    # TODO: Implement logic for /out
    return {"message": "Stub for /out", "method": "PUT"}

@router.get("/hotels/search?location={}&checkin={}&checkout={}")
def hotels_search?location={}&checkin={}&checkout={}(db: Session = Depends(get_db)):
    # TODO: Implement logic for /hotels/search?location={}&checkin={}&checkout={}
    return {"message": "Stub for /hotels/search?location={}&checkin={}&checkout={}", "method": "GET"}

@router.get("/hotel/{id}")
def hotel_{id}(db: Session = Depends(get_db)):
    # TODO: Implement logic for /hotel/{id}
    return {"message": "Stub for /hotel/{id}", "method": "GET"}

@router.post("/bookings")
def bookings(db: Session = Depends(get_db)):
    # TODO: Implement logic for /bookings
    return {"message": "Stub for /bookings", "method": "POST"}
