#!/usr/bin/env python
"""
Simple deployment script for healthcare API
"""
import os
import subprocess
import sys

def run_command(command):
    """Run a command and return the result"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {command}")
        print(f"Error: {e.stderr}")
        return None

def main():
    """Main deployment function"""
    print("🚀 Starting Healthcare API Deployment...")
    
    # Set production environment
    os.environ['DJANGO_SETTINGS_MODULE'] = 'healthcare.settings.prod'
    
    # Run migrations
    print("\n📊 Running database migrations...")
    run_command("python manage.py migrate")
    
    # Collect static files
    print("\n📁 Collecting static files...")
    run_command("python manage.py collectstatic --noinput")
    
    # Create superuser (optional)
    print("\n👤 Creating superuser...")
    print("You can create a superuser manually with: python manage.py createsuperuser")
    
    print("\n✅ Deployment preparation complete!")
    print("\n🌐 Your API is ready to be deployed to:")
    print("   - Railway: https://railway.app")
    print("   - Render: https://render.com") 
    print("   - Heroku: https://heroku.com")
    
    print("\n📋 Next steps:")
    print("1. Push your code to GitHub")
    print("2. Connect to your chosen platform")
    print("3. Set environment variables")
    print("4. Deploy!")

if __name__ == "__main__":
    main()

