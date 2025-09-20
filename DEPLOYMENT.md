# Healthcare API Deployment Guide

## 🚀 Free Deployment Platforms

### Option 1: Railway (Recommended)
**Why Railway?** Free PostgreSQL, automatic deployments, easy setup

#### Steps:
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your healthcare repository
5. Add PostgreSQL database:
   - Click "New" → "Database" → "PostgreSQL"
6. Set environment variables in Variables tab:
   ```
   SECRET_KEY=your-super-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app.railway.app
   DB_NAME=railway
   DB_USER=postgres
   DB_PASSWORD=auto-generated
   DB_HOST=auto-generated
   DB_PORT=5432
   ```
7. Deploy! Your API will be live at `https://your-app.railway.app`

### Option 2: Render
**Why Render?** Free tier, easy setup, good for beginners

#### Steps:
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python manage.py migrate && python manage.py collectstatic --noinput && gunicorn healthcare.wsgi:application --bind 0.0.0.0:$PORT`
6. Add PostgreSQL database:
   - Click "New" → "PostgreSQL"
7. Set environment variables
8. Deploy!

### Option 3: Heroku
**Why Heroku?** Most popular, lots of documentation

#### Steps:
1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-healthcare-api`
4. Add PostgreSQL: `heroku addons:create heroku-postgresql:hobby-dev`
5. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app.herokuapp.com
   ```
6. Deploy: `git push heroku main`

## 🔧 Pre-Deployment Setup

### 1. Update manage.py for production:
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare.settings.prod')
```

### 2. Create .env file locally (don't commit this):
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

## 📋 Environment Variables Needed

Set these in your deployment platform:

### Required:
- `SECRET_KEY` - Django secret key (generate a new one)
- `DEBUG` - Set to `False` for production
- `ALLOWED_HOSTS` - Your domain (e.g., your-app.railway.app)
- `DB_NAME` - Database name
- `DB_USER` - Database user
- `DB_PASSWORD` - Database password
- `DB_HOST` - Database host
- `DB_PORT` - Database port (usually 5432)

### Optional:
- `CORS_ALLOWED_ORIGINS` - Frontend domains
- `EMAIL_HOST` - SMTP server
- `EMAIL_HOST_USER` - Email username
- `EMAIL_HOST_PASSWORD` - Email password

## 🧪 Testing Your Deployed API

### 1. Health Check:
```bash
GET https://your-app.railway.app/api/auth/
```

### 2. Register User:
```bash
POST https://your-app.railway.app/api/auth/register/
{
    "email": "test@example.com",
    "username": "testuser",
    "name": "Test User",
    "password": "password123",
    "password_confirm": "password123"
}
```

### 3. Login:
```bash
POST https://your-app.railway.app/api/auth/login/
{
    "email": "test@example.com",
    "password": "password123"
}
```

### 4. Use API:
```bash
GET https://your-app.railway.app/api/patients/
Authorization: Bearer <your-token>
```

## 🎯 API Endpoints

After deployment, your API will be available at:

- **Base URL**: `https://your-app.railway.app`
- **Authentication**: `https://your-app.railway.app/api/auth/`
- **Patients**: `https://your-app.railway.app/api/patients/`
- **Admin**: `https://your-app.railway.app/admin/`

## 🔒 Security Notes

1. **Never commit** `.env` files
2. **Use strong** SECRET_KEY
3. **Set DEBUG=False** in production
4. **Use HTTPS** (most platforms provide this automatically)
5. **Rotate** database passwords regularly

## 🆘 Troubleshooting

### Common Issues:
1. **Build fails**: Check requirements.txt
2. **Database connection**: Verify environment variables
3. **Static files**: Ensure whitenoise is installed
4. **CORS errors**: Set CORS_ALLOWED_ORIGINS

### Debug Commands:
```bash
# Check logs
heroku logs --tail

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser
```

## 🎉 Success!

Once deployed, your healthcare API will be live and accessible worldwide!

