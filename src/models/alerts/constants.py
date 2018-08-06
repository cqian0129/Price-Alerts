
URL = "https://api.mailgun.net/v3/sandboxe82fd39d902a453bb8ef26fc554dadca.mailgun.org/messages"
API_KEY = "key-7175395d9cc90ef517e4c89bb907dd20"
FROM = "Mailgun Sandbox <postmaster@sandboxe82fd39d902a453bb8ef26fc554dadca.mailgun.org>"
import os

# URL = os.environ.get('MAILGUN_URL')
# API_KEY = os.environ.get('MAILGUN_API_KEY')
# FROM = os.environ.get('MAILGUN_FROM')

ALERT_TIMEOUT = 10
COLLECTION = "alerts"