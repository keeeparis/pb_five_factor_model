import logging
from decouple import config
from telegram.ext import (
  Application,
  CommandHandler,
  ConversationHandler,
  MessageHandler,
  filters,
)
from telegram import __version__ as TG_VER
from telegram import Update

from src.commands.commands import *
from src.utils.utils import *

from src.db.database import *

try:
  from telegram import __version_info__
except ImportError:
  __version_info__ = (0,0,0,0,0)
  
if __version_info__ < (20, 0, 0, "alpha", 1):
  raise RuntimeError(
    f"This example is not compatible with your current PTB version {TG_VER}. To view the "
    f"{TG_VER} version of this example, "
    f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
  )

logging.basicConfig(
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

def questions_states():
  filter_regex = filters.Regex("^(Полностью согласен|Согласен|Нейтрально|Полностью не согласен|Не согласен)")
  states_dict = {}
  
  for key in ALL_SORTED_QUESTIONS.keys():
    states_dict[key] = [MessageHandler(filter_regex, test_question_command)]
  
  return states_dict

BEGIN = 0

def main() -> None:
  """Start the bot."""
  # Create the Application and pass it your bot's token.
  application = Application.builder().token(config('TOKEN')).build()
    
  conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start_command), CommandHandler("attempt", attempt_command)],
    states={
      BEGIN: [MessageHandler(filters.Regex("^(Начать|да|Да)$"), begin_command)],
      **questions_states(),
    },
    fallbacks=[
      MessageHandler(filters.Regex("^Отмена$"), cancel_command),
      MessageHandler(filters.TEXT, fallback_command)
    ],
  )
  
  application.add_handler(conv_handler)
  application.add_handler(CommandHandler("description", description_command))
  application.add_handler(CommandHandler("help", help_command))
  application.add_handler(CommandHandler("list", bots_command))
    
  # Start Bot
  application.run_polling(allowed_updates=Update.ALL_TYPES)
  
if __name__ == "__main__":
  main()
