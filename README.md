# hotelbookinguidesign

Backend API for hotelbookinguidesign

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Hotelbookinguidesign))

## Project Structure

```
hotelbookinguidesign/
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

- Hotel Search
- Hotel Details
- Booking System

## API Endpoints

- `GET /hotels/search?location={}&checkin={}&checkout={}` - Search for hotels based on location and date range
- `GET /hotel/{id}` - View details of a specific hotel
- `POST /bookings` - Book a hotel room

## License

MIT
