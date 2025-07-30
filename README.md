# Copyright (c) 2025 Rowe Tampus
# Licensed under the MIT License
# 🎬 Netflix-like Movie Application

A full-stack movie streaming application built with **Django REST Framework** (Backend) and **React.js** (Frontend), featuring a wanna be (close but far) Netflix-like UI with video upload and playback capabilities.

## ✨ Features

- 🎥 **Movie Management**: Create, read, update, and delete movies
- 📁 **Video Upload**: Upload and store video files (MP4, AVI, MOV, WMV, FLV, WebM)
- 🎮 **Video Playback**: Custom video player with controls and keyboard shortcuts
- 🎨 **Netflix-like UI**: Modern, responsive design with smooth animations
- 📱 **Responsive Design**: Works on desktop and mobile devices
- 🔔 **Real-time Feedback**: Toast notifications for user actions
- ⚡ **Loading States**: Smooth loading indicators throughout the app

## 🛠️ Tech Stack

### Backend
- **Django 5.2.4** - Web framework
- **Django REST Framework** - API development
- **django-cors-headers** - Cross-origin resource sharing
- **SQLite** - Database (can be easily changed to PostgreSQL/MySQL)

### Frontend
- **React.js** - User interface library
- **Axios** - HTTP client for API calls
- **react-toastify** - Toast notifications
- **CSS3** - Styling with Netflix-inspired design

## 🚀 Quick Start
**GIT CLONE THE PROJECT REPOSITORY*
### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup


1. **Navigate to backend directory:**
   ```bash
   cd movieplatform
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start Django server:**
   ```bash
   python manage.py runserver
   ```

   The backend will be available at `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd movie-frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start React development server:**
   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`

## 📁 Project Structure

```
NetflixAppProject/
├── movieplatform/          # Django Backend
│   ├── movieplatform/      # Django project settings
│   ├── movies/            # Movies app
│   │   ├── models.py      # Movie model
│   │   ├── serializers.py # API serializers
│   │   ├── views.py       # API views
│   │   └── urls.py        # URL routing
│   ├── media/             # Uploaded video files
│   └── manage.py          # Django management
├── movie-frontend/        # React Frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   │   ├── MovieList.jsx
│   │   │   ├── MovieDetail.jsx
│   │   │   ├── MovieForm.jsx
│   │   │   ├── MoviePlayer.jsx
│   │   │   └── Header.jsx
│   │   ├── App.js         # Main app component
│   │   ├── api.js         # API client
│   │   └── App.css        # Styling
│   └── package.json
└── README.md
```

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/movies/` | List all movies |
| POST | `/api/movies/` | Create new movie |
| GET | `/api/movies/<id>/` | Get single movie |
| PUT | `/api/movies/<id>/` | Update movie |
| DELETE | `/api/movies/<id>/` | Delete movie |

## 🎮 Usage

1. **Add Movies**: Click "Add Movie" to upload a new movie with video file
2. **Browse Movies**: View all movies in a Netflix-style grid layout
3. **Movie Details**: Click on a movie to view details
4. **Play Movies**: Click "Play Movie" to watch uploaded videos
5. **Edit Movies**: Modify movie information and replace video files
6. **Delete Movies**: Remove movies from your collection

## 🎨 UI Features

- **Netflix-inspired Design**: Dark theme with red accents
- **Responsive Grid**: Movie cards adapt to screen size
- **Custom Video Player**: Full-screen playback with controls
- **Smooth Animations**: Hover effects and transitions
- **Loading States**: Visual feedback during operations
- **Toast Notifications**: Success/error messages

## 🔒 File Upload

- **Supported Formats**: MP4, AVI, MOV, WMV, FLV, WebM
- **File Size Limit**: 500MB per video
- **Storage**: Files stored in `media/videos/` directory
- **Validation**: Frontend and backend file validation

## 🚀 Deployment

### Backend Deployment
1. Set `DEBUG = False` in `settings.py`
2. Configure production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure CORS for production domain

### Frontend Deployment
1. Build the project: `npm run build`
2. Deploy to Vercel, Netlify, or any static hosting service

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## Video Demo 
[Link here](https://youtu.be/GsHcDy5Zb4I)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
