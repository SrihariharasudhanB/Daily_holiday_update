from fetch_data import Fetcher
from mailing import Mail

fecher = Fetcher()
mail = Mail()

mail.sendMail(fecher.fetch())
