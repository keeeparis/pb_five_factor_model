# Groups and Questions
ext_questions = {'EXT1' : 'Я душа компании',
                 'EXT2' : 'Я говорю немного',
                 'EXT3' : 'Я чувствую себя комфортно в обществе',
                 'EXT4' : 'Я остаюсь на заднем плане',
                 'EXT5' : 'Я начинаю разговоры',
                 'EXT6' : 'У меня есть мало что сказать',
                 'EXT7' : 'Я общаюсь с множеством разных людей на вечеринках',
                 'EXT8' : 'Я не люблю привлекать внимание к себе',
                 'EXT9' : 'Я не возражаю быть центром внимания',
                 'EXT10': 'Я молчалив в общении с незнакомцами'}

est_questions = {'EST1' : 'Я легко подвергаюсь стрессу',
                 'EST2' : 'Я чаще всего спокоен(спокойна)',
                 'EST3' : 'Я волнуюсь о всяких мелочах',
                 'EST4' : 'Я редко чувствую себя грустным(грустной)',
                 'EST5' : 'Я легко подвергаюсь беспокойству',
                 'EST6' : 'Я легко расстраиваюсь',
                 'EST7' : 'Мое настроение часто меняется',
                 'EST8' : 'У меня часто бывают перепады настроения',
                 'EST9' : 'Я легко раздражаюсь',
                 'EST10': 'Я часто чувствую себя унылым(унылой)'}

agr_questions = {'AGR1' : 'Я мало забочусь о других',
                 'AGR2' : 'Меня интересуют люди',
                 'AGR3' : 'Я обижаю людей',
                 'AGR4' : 'Я сопереживаю чужим чувствам',
                 'AGR5' : 'Меня не интересуют чужие проблемы',
                 'AGR6' : 'У меня мягкое сердце',
                 'AGR7' : 'Меня не очень интересуют другие люди',
                 'AGR8' : 'Я уделяю время другим',
                 'AGR9' : 'Я чувствую эмоции других людей',
                 'AGR10': 'Я располагаю людей к себе'}

csn_questions = {'CSN1' : 'Я всегда готов (всегда во всеоружии)',
                 'CSN2' : 'Я разбрасываю свои вещи вокруг',
                 'CSN3' : 'Я обращаю внимание на детали',
                 'CSN4' : 'Я навожу беспорядок',
                 'CSN5' : 'Я сразу делаю работу по дому',
                 'CSN6' : 'Часто забываю вернуть вещи на свое место',
                 'CSN7' : 'Мне нравится порядок',
                 'CSN8' : 'Я уклоняюсь от своих обязанностей',
                 'CSN9' : 'Я следую расписанию',
                 'CSN10' : 'Я требователен(требовательна) к своей работе'}

opn_questions = {'OPN1' : 'У меня богатый словарный запас',
                 'OPN2' : 'Мне трудно понимать абстрактные идеи',
                 'OPN3' : 'У меня богатое воображение',
                 'OPN4' : 'Меня не интересуют абстрактные идеи',
                 'OPN5' : 'У меня отличные идеи',
                 'OPN6' : 'У меня плохое воображение',
                 'OPN7' : 'Я быстро понимаю суть вещей',
                 'OPN8' : 'Я использую сложные слова',
                 'OPN9' : 'Я уделяю время размышлениям',
                 'OPN10': 'Я полон(полна) идей'}

ALL_QUESTIONS = { **ext_questions, **est_questions, **agr_questions, **csn_questions, **opn_questions }

def sorted_questions(questions: dict[str, str]) -> dict[str, str]:
  myKeys = list(questions.keys())
  myKeys.sort(key= lambda x: x[3])
  sorted_dict = {i: questions[i] for i in myKeys}
  return sorted_dict
  
ALL_SORTED_QUESTIONS = sorted_questions(ALL_QUESTIONS)

TRAITS_TRANSLATION = {
  'extraversion': 'Экстраверсия', 
  'neuroticism': 'Невротизм', 
  'agreeableness': 'Доброжелательность', 
  'conscientiousness': 'Сознательность', 
  'openness': 'Открытость'
}

ANSWERS = {
  1: "Полностью не согласен ❌",
  2: "Не согласен 🙅🏼‍♂️",
  3: "Нейтрально ☑️",
  4: "Согласен 🙋🏼‍♀️",
  5: "Полностью согласен ✅" 
}

ext_description = {
  "title": "Экстраверсия",
  "High": "Люди с высоким уровнем экстраверсии обычно яркие, общительные и энергичные. Они наслаждаются общением с другими, легко заводят новые знакомства и часто предпочитают общественные мероприятия. Экстраверты чувствуют себя комфортно в обществе и получают энергию от социальных взаимодействий. Они обладают хорошими коммуникативными навыками и часто привлекают внимание своей яркой личностью.",
  "Medium": "Люди со средним уровнем экстраверсии имеют баланс между общительностью и желанием провести время в одиночестве. Они могут наслаждаться социальными мероприятиями, но также ценят свою частную жизнь и время для отдыха. Такие индивиды не ищут постоянного общения, но они умеют адаптироваться к разным ситуациям и с удовольствием участвуют в социальных взаимодействиях по мере необходимости.",
  "Low": "Люди с низким уровнем экстраверсии предпочитают уединение и более небольшие группы. Они могут быть более замкнутыми и предпочитать индивидуальные занятия перед общественными мероприятиями. Такие индивиды не испытывают такой же потребности в общении, как экстраверты, и могут выбирать время в одиночестве для восстановления энергии."
}

est_description = {
  "title": "Невротизм",
  "High": "Люди с высоким уровнем невротизма часто испытывают сильные эмоции и более подвержены тревоге, депрессии и эмоциональным колебаниям. Они могут реагировать сильно на стрессовые ситуации и испытывать трудности в справлении с негативными эмоциями. Такие индивиды могут быть более восприимчивыми к критике и переживать неуверенность в себе.",
  "Medium": "Люди со средним уровнем невротизма могут проявлять сдержанность в эмоциях и иметь стабильный эмоциональный фон. Они не так сильно реагируют на стрессовые ситуации и легче переживают негативные события. Такие индивиды способны справляться с жизненными вызовами и имеют более уравновешенный эмоциональный опыт.",
  "Low": "Люди с низким уровнем невротизма имеют высокую эмоциональную стабильность и редко испытывают сильные колебания настроения. Они часто являются уверенными в себе и решительными, что позволяет им успешно справляться с жизненными вызовами. Такие индивиды могут быть более устойчивыми к стрессу и более способными оставаться спокойными в сложных ситуациях. Их стабильность и спокойствие могут оказывать положительное влияние на окружающих и помогать им создавать гармоничные отношения с другими."
}

agr_description = {
  "title": "Доброжелательность",
  "High": "Люди с высоким уровнем доброжелательности обладают добротой, состраданием и способностью понимать чувства и нужды других. Они чувствительны к эмоциональным сигналам окружающих и могут предложить поддержку и помощь тем, кто в ней нуждается. Высокая приветливость способствует развитию тесных и поддерживающих отношений с другими людьми, и такие индивиды часто оцениваются окружающими за свою заботливость и теплоту.",
  "Medium": "Люди со средним уровнем доброжелательности обладают балансом между эмпатией и самоудержанием. Они могут выказывать заботу и сочувствие, но также умеют сохранять свои границы и не позволять эмоциям управлять своим поведением. Такие индивиды могут быть доброжелательными и внимательными, но они также могут проявлять стойкость и решительность при необходимости.",
  "Low": "Люди с низким уровнем доброжелательности могут быть более независимыми и менее склонными к выражению эмоций. Они могут быть менее интересующимися чувствами и потребностями других и предпочитать сохранять эмоциональное расстояние. Такие индивиды могут быть более уверенными в себе и независимыми, но их поведение может быть воспринято окружающими как отстраненность или недостаток эмпатии."
}

csn_description = {
  "title": "Сознательность",
  "High": "Люди с высоким уровнем сознательности обладают выдающейся самодисциплиной, организованностью и ответственностью. Они четко определяют свои цели и настойчиво работают, чтобы достичь их. Такие люди надежны и часто выступают в роли лидеров, так как их способность планировать и координировать дела является очевидной. Они часто ставят себе высокие стандарты и стремятся к отличным результатам в своей работе и личной жизни.",
  "Medium": "Люди со средним уровнем сознательности могут демонстрировать баланс между дисциплиной и гибкостью. Они способны принимать обязательства и следовать им, но также могут быть менее строгими в своих методах и подходах. Такие индивиды имеют умеренную организованность и ответственность, что позволяет им адаптироваться к изменяющимся обстоятельствам и обращаться с неожиданными ситуациями.",
  "Low": "Люди с низким уровнем сознательности могут испытывать трудности в планировании и управлении своими обязанностями. Они могут проявлять небрежность и быть менее ответственными в своих делах. Такие индивиды могут быть более гибкими и спонтанными, но при этом могут также сталкиваться с трудностями в соблюдении сроков и выполнении обязательств. Однако они могут быть более творческими и открытыми к новым идеям."
}

opn_description = {
  "title": "Открытость",
  "High": "Люди с высокой открытостью к опыту обладают богатым внутренним миром и стремятся к постоянному познанию мира вокруг себя. Они открыты для новых идей, опытов, исследований и культурных взаимодействий. Такие индивиды питают страсть к искусству, литературе, наукам и креативным процессам. Они с легкостью воспринимают абстрактные понятия и могут видеть связи и возможности там, где другие не замечают. Люди с высокой открытостью к опыту часто считаются вдохновителями и инноваторами, способными привносить свежие идеи в работу и жизнь окружающих.",
  "Medium": "Люди со средним уровнем открытости к опыту предпочитают баланс между привычными и новыми впечатлениями. Они могут быть заинтересованы в изучении новых областей и идей, но не будут стремиться к экспериментам и риску в той же степени, что и те с высокой открытостью. Такие люди обладают здравым смыслом и склонностью к реализму, однако они также способны быть креативными и приспособиться к новым ситуациям, когда это необходимо.",
  "Low": "Люди с низкой открытостью к опыту обычно предпочитают традиционализм и предсказуемость. Они предпочитают избегать изменений и рискованных решений, предпочитая известное и знакомое. Такие индивиды ориентированы на практические аспекты жизни и не проявляют большого интереса к искусству, абстрактным наукам или необычным идеям. Им часто удобно следовать установленным правилам и нормам, и они могут быть более консервативными в своих взглядах и убеждениях. Тем не менее, они могут быть надежными и предсказуемыми в своих действиях и решениях."
}

def description_to_output(description: dict[str, str]) -> str:
  lines = [ f"<b>{value}</b>\n" if key == 'title' else f"{value}\n" for key, value in description.items()]
  output = "\n".join(lines).join(["\n", "\n"])
  return output
  
ext_output = description_to_output(ext_description)
est_output = description_to_output(est_description)
agr_output = description_to_output(agr_description)
csn_output = description_to_output(csn_description)
opn_output = description_to_output(opn_description)
