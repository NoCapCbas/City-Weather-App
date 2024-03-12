Weather App, using Django

Dependencies
- Docker
- Open Weather API
- .env file

Create a .env file within the main project directory:
```bash
## do not put this file under version control!
## so add this file in .gitignore in production, or keep repo private
SECRET_KEY='django-insecure-123'
DEBUG=False

SUPER_USER_NAME='root'
SUPER_USER_PASSWORD='root'
SUPER_USER_EMAIL='root@root.com'
```
