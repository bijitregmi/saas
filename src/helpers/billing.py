# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
from decouple import config

DJANGO_DEBUG = config("DJANGO_DEBUG", default=False, cast=bool)
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default=str, cast=str)

stripe.api_key = STRIPE_SECRET_KEY

stripe.Customer.create(
  name="Jenny Rosen",
  email="jennyrosen@example.com",
)