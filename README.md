# Hotelbookinguidesign

Backend API for Hotelbookinguidesign

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign.git))

## Project Structure

```
Hotelbookinguidesign/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- User registration and login
- Hotel search based on location, dates, and guests
- Hotel details view with rooms and amenities
- Booking management (create, view, cancel)
- Admin panel for hotel and room management
- JWT authentication
- Data validation
- Error handling

## API Endpoints

- `POST /api/auth/register` - Registers a new user.
- `POST /api/auth/login` - Logs in an existing user.
- `GET /api/hotels` - Retrieves a list of hotels, optionally filtered by location, dates, and number of guests.
- `GET /api/hotels/{hotel_id}` - Retrieves details for a specific hotel.
- `POST /api/bookings` - Creates a new booking.
- `GET /api/bookings/{booking_id}` - Retrieves details for a specific booking.
- `GET /api/users/{user_id}/bookings` - Retrieves all bookings for a specific user.
- `DELETE /api/bookings/{booking_id}` - Cancels a booking.
- `POST /api/admin/hotels` - Adds a new hotel (Admin only).
- `PUT /api/admin/hotels/{hotel_id}` - Updates an existing hotel (Admin only).

## License

MIT
