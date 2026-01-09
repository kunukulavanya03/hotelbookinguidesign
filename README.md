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

- user_authentication
- room_booking
- availability_management

## API Endpoints

- `POST /api/auth/register` - Endpoint for user registration.
- `POST /api/auth/login` - Endpoint for user login.
- `GET /api/rooms/{date}` - Endpoint to get available rooms on a specific date.
- `POST /api/rooms/book` - Endpoint to book a room.
- `POST /api/admin/rooms/update_availability` - Endpoint for admin to update room availability.

## License

MIT
