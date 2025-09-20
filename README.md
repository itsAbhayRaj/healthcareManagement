# 🏥 Healthcare API

A Django REST Framework API for managing healthcare data with JWT authentication.

## 🚀 Features

- **JWT Authentication** - Secure token-based authentication
- **Patient Management** - CRUD operations for patient records
- **User Management** - Registration, login, profile management
- **RESTful API** - Clean, well-documented API endpoints
- **PostgreSQL** - Robust database support
- **CORS Support** - Cross-origin resource sharing enabled

## 📋 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user
- `GET /api/auth/profile/` - Get user profile
- `POST /api/auth/token/refresh/` - Refresh access token

### Patients
- `GET /api/patients/` - List all patients
- `POST /api/patients/` - Create new patient
- `GET /api/patients/{id}/` - Get specific patient
- `PUT /api/patients/{id}/` - Update patient
- `PATCH /api/patients/{id}/` - Partial update patient
- `DELETE /api/patients/{id}/` - Delete patient

## 🛠️ Local Development

### Prerequisites
- Python 3.11+
- PostgreSQL
- pip

### Setup
1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd healthcare
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

## 🌐 Deployment

This project is ready for deployment on various platforms:

### Railway (Recommended)
1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repository
3. Add PostgreSQL database
4. Set environment variables
5. Deploy!

### Render
1. Go to [render.com](https://render.com)
2. Create new Web Service
3. Connect your repository
4. Add PostgreSQL database
5. Deploy!

### Heroku
1. Install Heroku CLI
2. Create Heroku app
3. Add PostgreSQL addon
4. Set environment variables
5. Deploy!

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

## 🧪 Testing the API

### 1. Register a user
```bash
curl -X POST https://your-api.railway.app/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "username": "testuser",
    "name": "Test User",
    "password": "password123",
    "password_confirm": "password123"
  }'
```

### 2. Login
```bash
curl -X POST https://your-api.railway.app/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

### 3. Use the API
```bash
curl -X GET https://your-api.railway.app/api/patients/ \
  -H "Authorization: Bearer <your-access-token>"
```

## 🔒 Security

- JWT tokens with configurable expiration
- Password validation
- CORS protection
- SQL injection protection
- XSS protection

## 📁 Project Structure

```
healthcare/
├── accounts/          # User authentication
├── patients/          # Patient management
├── doctors/           # Doctor management
├── mappings/          # Patient-Doctor mappings
├── healthcare/        # Main project settings
├── requirements.txt   # Python dependencies
├── Procfile          # Deployment configuration
└── README.md         # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues, please:
1. Check the [DEPLOYMENT.md](DEPLOYMENT.md) guide
2. Review the error logs
3. Create an issue on GitHub

---

**Happy coding! 🎉**

