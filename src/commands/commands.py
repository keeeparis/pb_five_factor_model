import datetime
import math
import plotly.express as px

from asyncio import sleep
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import ContextTypes, ConversationHandler

from src.utils.utils import *
from src.model.model import *
from src.db.database import *
from src.db.utils import *

BEGIN = 0 

# helper func
def generator(x: dict[str, str]):
  current = 0
  list_dict = list(x.items())
  
  while len(list_dict) > current:    
    yield list_dict[current]
    current += 1 
  
def process_answer(question_name: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
  question = context.user_data[question_name]
  context.user_data[question[0]] = list(ANSWERS.values()).index(update.message.text) + 1
  del context.user_data[question_name] 

async def calculate_result(user_data: Dict, user):
  data = traverse_results(user_data)

  extraversion = (data['EXT1'] + data['EXT2'] + data['EXT3'] + data['EXT4'] + data['EXT5'] + data['EXT6'] + data['EXT7'] + data['EXT8'] + data['EXT9'] + data['EXT10'])/10 
  neuroticism = (data['EST1'] + data['EST2'] + data['EST3'] + data['EST4'] + data['EST5'] + data['EST6'] + data['EST7'] + data['EST8'] + data['EST9'] + data['EST10'])/10 
  agreeableness = (data['AGR1'] + data['AGR2'] + data['AGR3'] + data['AGR4'] + data['AGR5'] + data['AGR6'] + data['AGR7'] + data['AGR8'] + data['AGR9'] + data['AGR10'])/10 
  conscientiousness = (data['CSN1'] + data['CSN2'] + data['CSN3'] + data['CSN4'] + data['CSN5'] + data['CSN6'] + data['CSN7'] + data['CSN8'] + data['CSN9'] + data['CSN10'])/10 
  openness = (data['OPN1'] + data['OPN2'] + data['OPN3'] + data['OPN4'] + data['OPN5'] + data['OPN6'] + data['OPN7'] + data['OPN8'] + data['OPN9'] + data['OPN10'])/10 
  
  [results_for_text, results_for_plot] = model([extraversion, neuroticism, agreeableness, conscientiousness, openness])

  df = pd.DataFrame(results_for_plot)
  
  output = f"Результаты @{user.username}:\n"
  facts = [f"<b>{TRAITS_TRANSLATION[key]}</b> — <i>{math.ceil(value)}</i>" for key, value in results_for_text.items()]
  output += "\n".join(facts).join(["\n", "\n"])
  
  fig = px.bar(
    df, 
    x='trait', 
    y='value',
    range_y=[0, 100],
    labels={ 'trait': '', 'value': '' },
    title=f"Результаты @{user.username} - {datetime.datetime.now().strftime('%d/%m/%Y')} - by @five_factor_model_bot",
    color='trait',
    color_discrete_map={
      TRAITS_TRANSLATION['extraversion']: '#7FD4C1', TRAITS_TRANSLATION['neuroticism']: '#30BFDD', TRAITS_TRANSLATION['agreeableness']: '#8690FF', TRAITS_TRANSLATION['conscientiousness']: '#ACD0F4', TRAITS_TRANSLATION['openness']: '#F7C0BB'
    }
  )
  fig.update_layout(showlegend=False)
    
  img = fig.to_image(format='png')
  
  return [output, img, results_for_text]
  
async def question(update: Update, context: ContextTypes.DEFAULT_TYPE, questions):
  process_answer('question', update, context)
  user = update.message.from_user
    
  try:
    question = next(questions)
    context.user_data['question'] = question
    
    await update.message.reply_text(
      question[1],
      reply_markup=answer_markup,
    )

    return question[0]
  
  except:
    await update.message.reply_text(
      "Спасибо! Вы закончили прохождение теста.",
      reply_markup=ReplyKeyboardRemove()
    )
    
    await sleep(1)
    
    await update.message.reply_text(
      "Идет подсчет результатов..."
    )
    
    [output, img, results_for_text] = await calculate_result(context.user_data, user)
    
    db.connect(reuse_if_open=True)
    
    create_test(
      user_id=user.id, 
      ext_result=results_for_text['extraversion'],
      est_result=results_for_text['neuroticism'],
      agr_result=results_for_text['agreeableness'],
      csn_result=results_for_text['conscientiousness'],
      opn_result=results_for_text['openness']
    )
    
    db.close()
    
    await sleep(1)
    
    await update.message.reply_text(
      f"{output}",
      parse_mode='HTML'
    )
    
    await update.message.reply_photo(img)
    
    await sleep(1)
    
    # results descriptions
    await update.message.reply_text(
      f"{ext_output}",
      parse_mode='HTML'
    )
    await update.message.reply_text(
      f"{est_output}",
      parse_mode='HTML'
    )
    await update.message.reply_text(
      f"{agr_output}",
      parse_mode='HTML'
    )
    await update.message.reply_text(
      f"{csn_output}",
      parse_mode='HTML'
    )
    await update.message.reply_text(
      f"{opn_output}",
      parse_mode='HTML'
    )
        
    return ConversationHandler.END

# keyboards
reply_start_keyboard = [
  ["Начать", "Отмена"], 
]

reply_answers_keyboard = [
  [ANSWERS.get(5), ANSWERS.get(4)],
  [ANSWERS.get(3)],
  [ANSWERS.get(2), ANSWERS.get(1)],
  ["Отмена"],
]

# markups
start_markup = ReplyKeyboardMarkup(reply_start_keyboard, resize_keyboard=True, one_time_keyboard=True)
answer_markup = ReplyKeyboardMarkup(reply_answers_keyboard, resize_keyboard=True)

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  """Start the conversation and ask for starting the test"""  
  db.connect(reuse_if_open=True)
  
  chat_id = update.message.chat_id
  current_user = update.effective_user

  if not user_exists(user_id=current_user.id):
    create_user(id=current_user.id, username=current_user.username, first_name=current_user.first_name, last_name=current_user.last_name, chat_id=chat_id)
      
  db.close()
  
  await update.message.reply_text("Добрый день!")
  
  start_text = open('assets/description.txt', 'r')

  await update.message.reply_text(
    f"{start_text.read()}",
    parse_mode="Markdown"
  )
  
  start_text.close()
  
  await sleep(1)
    
  context.user_data['generator'] = generator(ALL_SORTED_QUESTIONS)
  
  await update.message.reply_text(
    "Начать выполнение теста?", 
    reply_markup=start_markup)
  
  return BEGIN

async def attempt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  db.connect(reuse_if_open=True)
  
  chat_id = update.message.chat_id
  current_user = update.effective_user

  if not user_exists(user_id=current_user.id):
    create_user(id=current_user.id, username=current_user.username, first_name=current_user.first_name, last_name=current_user.last_name, chat_id=chat_id)

  db.close()
  
  global all_questions_generator
  all_questions_generator = generator(ALL_SORTED_QUESTIONS) 
  
  await update.message.reply_text(
    "Начать выполнение теста?", 
    reply_markup=start_markup)
  
  return BEGIN

async def begin_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:  
  generator = context.user_data['generator']
  question = next(generator)
  context.user_data['question'] = question
  
  await update.message.reply_text(
    question[1],
    reply_markup=answer_markup,
  )
    
  return question[0]

async def test_question_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
  generator = context.user_data['generator']
  key = await question(update, context, generator)
  return key

async def fallback_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:  
  await update.message.reply_text(
    "Пожалуйста, выберете один из предложенных вариантов. Eсли хотите закончить тест - нажмите кнопку Отмена", 
    reply_markup=answer_markup
  )
  return

async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:  
  await update.message.reply_text(
    "Вы прервали тест. Ну что ж, возвращайтесь скорее. \
    Для прохождения теста нажмите /attempt",
    reply_markup=ReplyKeyboardRemove()
  )
  return ConversationHandler.END
  
async def description_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  start_text = open('assets/description.txt', 'r')

  await update.message.reply_text(
    f"{start_text.read()}",
    parse_mode="Markdown"
  )
  
  start_text.close()
  
  await update.message.reply_text(
    "Чтобы начать прохождение теста - /attempt"
  )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  await update.message.reply_text(
    "/start - Начать тест\n/attempt - Начать теста\n/cancel - Прервать тест\n/description - Описание теста\n/help - Помощь" 
  )
