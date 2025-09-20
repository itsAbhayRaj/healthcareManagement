# Vercel Deployment Guide for Healthcare Django Project

This guide will help you deploy your Django healthcare project to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **GitHub Account**: Your code should be in a GitHub repository
3. **PostgreSQL Database**: You'll need a PostgreSQL database (recommend using Vercel Postgres or external service like Supabase)

## Project Structure

The project has been configured with the following Vercel-specific files:

- `vercel.json` - Vercel configuration
- `api/index.py` - WSGI application entry point
- `requirements-vercel.txt` - Python dependencies for Vercel
- `.gitignore` - Git ignore file for Django projects

## Deployment Steps

### 1. Push to GitHub

First, push your code to a GitHub repository:

```bash
# Add your GitHub remote (replace with your repository URL)
git remote add origin https://github.com/yourusername/healthcare-project.git

# Push to GitHub
git push -u origin master
```

### 2. Deploy to Vercel

1. **Via Vercel Dashboard:**
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Python project

2. **Via Vercel CLI:**
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Login to Vercel
   vercel login
   
   # Deploy
   vercel
   ```

### 3. Configure Environment Variables

In your Vercel project dashboard, go to Settings > Environment Variables and add:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
DJANGO_SETTINGS_MODULE=healthcare.settings.prod

# Database Configuration
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=your-database-host
DB_PORT=5432

# CORS Settings
CORS_ALLOWED_ORIGINS=https://your-frontend-domain.com,https://your-vercel-app.vercel.app

# Email Settings (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
```

### 4. Database Setup

#### Option A: Vercel Postgres (Recommended)
1. In your Vercel project, go to Storage tab
2. Create a new Postgres database
3. Use the connection details in your environment variables

#### Option B: External Database
- Use services like Supabase, PlanetScale, or AWS RDS
- Add the connection details to your environment variables

### 5. Run Database Migrations

After deployment, you'll need to run migrations. You can do this by:

1. **Using Vercel CLI:**
   ```bash
   vercel env pull .env.local
   python manage.py migrate
   ```

2. **Using Vercel Functions:**
   Create a temporary migration endpoint in your Django app

### 6. Static Files

The project is configured to use WhiteNoise for static file serving, which works well with Vercel's serverless environment.

## Configuration Details

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "manage.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb",
        "runtime": "python3.9"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "manage.py"
    }
  ],
  "env": {
    "DJANGO_SETTINGS_MODULE": "healthcare.settings.prod"
  }
}
```

### Key Settings for Vercel

1. **WSGI Application**: Located in `api/index.py`
2. **Static Files**: Configured with WhiteNoise
3. **Database**: PostgreSQL with environment variables
4. **CORS**: Configured for Vercel domains
5. **Security**: SSL handled by Vercel

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are in `requirements-vercel.txt`
2. **Database Connection**: Verify environment variables are set correctly
3. **Static Files**: Check WhiteNoise configuration
4. **CORS Issues**: Update `CORS_ALLOWED_ORIGINS` with your frontend domain

### Debugging

1. Check Vercel function logs in the dashboard
2. Use `vercel logs` command for real-time logs
3. Test locally with `vercel dev`

## Performance Optimization

1. **Database Connection Pooling**: Consider using connection pooling for production
2. **Caching**: Implement Redis caching for better performance
3. **CDN**: Vercel automatically provides CDN for static files

## Security Considerations

1. **Environment Variables**: Never commit sensitive data to Git
2. **CORS**: Configure CORS properly for your frontend domains
3. **HTTPS**: Vercel provides automatic HTTPS
4. **Database**: Use strong passwords and secure connections

## Monitoring

1. **Vercel Analytics**: Monitor performance and errors
2. **Database Monitoring**: Use your database provider's monitoring tools
3. **Logs**: Check Vercel function logs regularly

## Support

- [Vercel Documentation](https://vercel.com/docs)
- [Django on Vercel](https://vercel.com/guides/deploying-django-to-vercel)
- [WhiteNoise Documentation](https://whitenoise.readthedocs.io/)

## Next Steps

1. Set up your database
2. Configure environment variables
3. Deploy to Vercel
4. Run database migrations
5. Test your API endpoints
6. Set up monitoring and logging
