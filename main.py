import pickle
import telebot
from telebot import types

token = 
bot = telebot.TeleBot(token)

class Proekt:
    def __init__(self,nazvanie, stages = dict(), gotovnost = 'Не завершён'):
        self.nazvanie = nazvanie
        self.stages = stages
        self.gotovnost = gotovnost

@bot.message_handler(commands=['whereami'])
def func(message):
    with open(str(message.chat.id) + 'whereami.pickle', 'rb') as f:
        whereami = pickle.load(f)
    bot.send_message(message.chat.id, text = str(whereami))


@bot.message_handler(commands=['start'])
def start(message):
    userid = str(message.chat.id)
    whereami = ''
    proekti = []
    with open(userid + 'proekti.pickle', 'wb') as f:
        pickle.dump(proekti, f, pickle.HIGHEST_PROTOCOL)
    with open(userid + 'whereami.pickle', 'wb') as f:
        pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
    zametki = dict()
    with open(userid + 'zametki.pickle', 'wb') as f:
        pickle.dump(zametki, f, pickle.HIGHEST_PROTOCOL)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_notes = types.KeyboardButton('📝Заметки')
    btn_projects = types.KeyboardButton("🧠🌪Проекты")
    btn_help = types.KeyboardButton("🆘help")
    markup.add(btn_notes,btn_projects,btn_help)
    bot.send_message(message.chat.id, text= ' !!!ПРЕДУПРЕЖДЕНИЕ ПРИ НАПИСАНИИ /start ВСЕ ОБНУЛИТСЯ\n\nПривет, это уникальный бот, который позволяет создавать заметки, напоминания и вести проекты.\n Для помощи нажмите help \n \n Made by Егор Зиновьев и Максим Москвин',reply_markup=markup)
@bot.message_handler(commands=['🆘help'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, это уникальный бот, который позволяет создавать заметки, напоминания и вести проекты.\n Made by Егор Зиновьев и Максим Москвин')

@bot.message_handler(content_types=['text'])
def func_btn_help(message):
    btn_edit_notes = types.KeyboardButton("Редактировать заметку")
    btn_mainmenu = types.KeyboardButton("🏚Назад в главное меню")
    btn_backnotes = types.KeyboardButton('Назад в заметки')
    btn_create_notes = types.KeyboardButton("Создать заметку")
    btn_read_notes = types.KeyboardButton('Прочитать заметку')
    btn_delete_notes = types.KeyboardButton("Удалить заметку")
    btn_delete_all_notes = types.KeyboardButton("Удалить все заметки")
    btn_notes = types.KeyboardButton('📝Заметки')
    btn_projects = types.KeyboardButton("🧠🌪Проекты")
    btn_create_project = types.KeyboardButton('Создать новый проект')
    btn_read_project = types.KeyboardButton('Открыть проект')
    btn_delete_project = types.KeyboardButton('Удалить проект')
    btn_create_stage = types.KeyboardButton("Создать новый этап")
    btn_read_stage = types.KeyboardButton("Открыть этап")
    btn_delete_stage = types.KeyboardButton("Удалить этап")
    btn_status = types.KeyboardButton('Изменить готовность проекта')
    btn_back_projects = types.KeyboardButton("Вернуться к проектам")
    btn_help = types.KeyboardButton("🆘help")
    btn_yes = types.KeyboardButton('Да')
    btn_no = types.KeyboardButton('Нет')
    userid = str(message.chat.id)
    with open(userid + 'whereami.pickle', 'rb') as f:
        whereami = pickle.load(f)

    if message.text == 'Назад в заметки':
        whereami = 'zametki'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_create_notes, btn_read_notes, btn_delete_notes, btn_delete_all_notes, btn_mainmenu)
        bot.send_message(message.chat.id, text='Заметки', reply_markup=markup)
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'zametki.pickle', 'rb') as f:
            zametki = pickle.load(f)
        if zametki == {}:
            bot.send_message(message.chat.id, text='Заметок нет', reply_markup=markup)
        else:
            stroka = '--------------\n'
            for i in zametki.keys():
                stroka += str(i + '\n')
            stroka += '--------------'
            whereami = 'zametki'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text=stroka, reply_markup=markup)
    if message.text == '🏚Назад в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_notes, btn_projects, btn_help)
        whereami = 'mainmenu'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        bot.send_message(message.chat.id, text='Главное меню', reply_markup=markup)
    if message.text == 'Вернуться к проектам':
        whereami = 'proekti'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)

    if whereami != 'status1' and whereami !='status2' and whereami != 'stage_delete1' and whereami != 'stage_delete2' and whereami != 'stage_read' and whereami != 'stage_create2' and whereami != 'stage_create1' and whereami != 'proekti_read2' and whereami != 'proekti_read1' and whereami != 'proekti_delete1' and whereami != 'proekti_delete2' and whereami != 'proekti_create1' and whereami != 'zametki_add1' and whereami != 'zametki_read1' and whereami != 'zametki_add2' and whereami != 'zametki_read2' and whereami != 'zametki_edit' and whereami != 'zametki_delete1' and whereami != 'zametki_delete2' and whereami != 'zametki_delete_all':
        if message.text == '🆘help':
            bot.send_message(message.chat.id,'Привет, это уникальный бот, который позволяет создавать заметки, напоминания и вести проекты.\n Made by Егор Зиновьев и Максим Москвин')
        if message.text == 'Открыть проект' and whereami == 'proekti':
            whereami = 'proekti_read1'
            with open(userid + 'proekti.pickle', 'rb') as f:
                proekti = pickle.load(f)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_create_project)
            if len(proekti) == 0:
                bot.send_message(message.chat.id, text='Проектов нет, смотреть нечего!', reply_markup=markup)
            else:
                with open(userid + 'whereami.pickle', 'wb') as f:
                    pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, text='Введите название проекта', reply_markup=markup)


        if message.text == '📝Заметки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_create_notes, btn_read_notes, btn_delete_notes, btn_delete_all_notes, btn_mainmenu)
            bot.send_message(message.chat.id, text='Заметки', reply_markup=markup)
            with open(userid + 'zametki.pickle', 'rb') as f:
                zametki = pickle.load(f)
            if zametki == {}:
                bot.send_message(message.chat.id, text='Заметок нет', reply_markup=markup)
            else:
                stroka = '--------------\n'
                for i in zametki.keys():
                    stroka += str(i +'\n')
                stroka += '--------------'
                whereami = 'zametki'
                with open(userid + 'whereami.pickle', 'wb') as f:
                    pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, text=stroka, reply_markup=markup)
        if message.text == '🧠🌪Проекты' or message.text == 'Вернуться к проектам':
            whereami = 'proekti'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'proekti.pickle', 'rb') as f:
                proekti = pickle.load(f)
            if len(proekti) == 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(btn_mainmenu,btn_create_project)
                bot.send_message(message.chat.id, text='Проектов нет', reply_markup=markup)
            else:
                stroka = '--------------\n'
                for i in range(len(proekti)):
                    stroka += str(proekti[i].nazvanie) + '\n' + 'Готовность: ' + str(proekti[i].gotovnost) + '\n\n'
                stroka += '--------------\n'
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                markup.add(btn_mainmenu, btn_create_project, btn_read_project, btn_status, btn_delete_project)
                bot.send_message(message.chat.id, text=stroka, reply_markup=markup)
        if message.text == 'Создать новый проект':
            whereami = 'proekti_create1'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Введите название проекта', reply_markup=markup)
        if message.text == 'Удалить проект':
            whereami = 'proekti_delete1'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Введите название проекта, который хотите удалить.', reply_markup=markup)
        if message.text == 'Прочитать заметку':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_backnotes)
            whereami = 'zametki_read1'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text='Введите название заметки', reply_markup=markup)
        if message.text == 'Удалить заметку':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_backnotes)
            whereami = 'zametki_delete1'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text='Введите название заметки', reply_markup=markup)
        if message.text == 'Удалить все заметки':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_yes, btn_no)
            whereami = 'zametki_delete_all'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text='ВЫ ХОТИТЕ УДАЛИТЬ ВСЕ ЗАМЕТКИ!\nВы уверены?', reply_markup=markup)
        if message.text == 'Создать заметку':
            whereami = 'zametki_add1'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_backnotes)
            bot.send_message(message.chat.id, text='Введите название заметки', reply_markup=markup)
        if message.text == 'Изменить готовность проекта':
            whereami = 'status1'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Введите название проекта', reply_markup=markup)
    elif whereami == 'proekti_read1':
        nazvanie = message.text
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        flag = 0
        for i in range(len(proekti)):
            if nazvanie == proekti[i].nazvanie:
                flag = 1

        if flag == 1:
            with open(userid + 'nazvanie.pickle', 'wb') as f:
                pickle.dump(nazvanie, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects,btn_create_stage ,btn_read_stage, btn_delete_stage)
            for i in range(len(proekti)):
                if nazvanie == proekti[i].nazvanie:
                    number = i
                    break
            stroka = '--------------\n'
            for i in proekti[number].stages.keys():
                stroka += str(i) + '\n'
            stroka += '--------------'
            whereami = 'proekti_read2'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            if stroka == '--------------\n--------------':
                with open(userid + 'number.pickle', 'wb') as f:
                    pickle.dump(number, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, text='--------------\nЭтапов нет\n--------------', reply_markup=markup)
            else:
                with open(userid + 'number.pickle', 'wb') as f:
                    pickle.dump(number, f, pickle.HIGHEST_PROTOCOL)
                bot.send_message(message.chat.id, text=stroka, reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Такого проекта нет. Введите другое название.', reply_markup=markup)

    elif whereami == 'proekti_read2' and message.text == 'Создать новый этап':
        whereami = 'stage_create1'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        bot.send_message(message.chat.id, text='Введите название этапа.', reply_markup=markup)
    elif message.text == 'Открыть этап' and whereami == 'proekti_read2':
        whereami = 'stage_read'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        bot.send_message(message.chat.id, text='Введите название этапа', reply_markup=markup)
    elif whereami == 'status1':

        flag = 0
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        for i in range(len(proekti)):
            if message.text == proekti[i].nazvanie:
                flag = 1
                break
        if flag == 1:
            whereami = 'status2'
            nazvanie = message.text
            with open(userid + 'nazvanie.pickle', 'wb') as f:
                pickle.dump(nazvanie, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Введите текст', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Такого проекта нет.', reply_markup=markup)
    elif whereami == 'status2':
        whereami = 'proekti'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        with open(userid + 'nazvanie.pickle', 'rb') as f:
            nazvanie = pickle.load(f)
        for i in range(len(proekti)):
            if nazvanie == proekti[i].nazvanie:
                proekti[i].gotovnost = message.text
        with open(userid + 'proekti.pickle', 'wb') as f:
            pickle.dump(proekti, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        bot.send_message(message.chat.id, text='Все прошло успешно!', reply_markup=markup)

    elif whereami == 'stage_create1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        nazvanie_stage = message.text
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        with open(userid + 'number.pickle', 'rb') as f:
            number = pickle.load(f)
        if proekti == []:
            number = 0
        if nazvanie_stage not in proekti[number].stages.keys():
            proekti[number].stages[nazvanie_stage] = ''
            whereami = 'stage_create2'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'nazvanie_stage.pickle', 'wb') as f:
                pickle.dump(nazvanie_stage, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'proekti.pickle', 'wb') as f:
                pickle.dump(proekti, f, pickle.HIGHEST_PROTOCOL)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Введите текст.', reply_markup=markup)
        else:
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Введите другое название.', reply_markup=markup)
    elif whereami == 'stage_create2':
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        with open(userid + 'number.pickle', 'rb') as f:
            number = pickle.load(f)
        with open(userid + 'nazvanie_stage.pickle', 'rb') as f:
            nazvanie_stage = pickle.load(f)
        proekti[number].stages[nazvanie_stage] = str(message.text)
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'nazvanie_stage.pickle', 'wb') as f:
            pickle.dump(nazvanie_stage, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'proekti.pickle', 'wb') as f:
            pickle.dump(proekti, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        bot.send_message(message.chat.id, text='Все прошло успешно!', reply_markup=markup)

    elif message.text == 'Удалить этап':
        whereami = 'stage_delete1'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        bot.send_message(message.chat.id, text='Введите название этапа, который хотите удалить.', reply_markup=markup)

    elif whereami == 'stage_delete1':
        nazvanie_stage = message.text
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        with open(userid + 'number.pickle', 'rb') as f:
            number = pickle.load(f)
        if nazvanie_stage in proekti[number].stages.keys():
            whereami = 'stage_delete2'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'nazvanie_stage.pickle', 'wb') as f:
                pickle.dump(nazvanie_stage, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_yes, btn_no)
            bot.send_message(message.chat.id, text='Вы уверены?', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Такого этапа нет. Введите другое название.', reply_markup=markup)
    elif whereami == 'stage_delete2' and message.text == 'Да':
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        with open(userid + 'nazvanie_stage.pickle', 'rb') as f:
            nazvanie_stage = pickle.load(f)
        with open(userid + 'number.pickle', 'rb') as f:
            number = pickle.load(f)
        del proekti[number].stages[nazvanie_stage]
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        whereami = 'proekti'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'proekti.pickle', 'wb') as f:
            pickle.dump(proekti, f, pickle.HIGHEST_PROTOCOL)
        bot.send_message(message.chat.id, text='Этап был удален', reply_markup=markup)
    elif whereami == 'stage_delete2' and message.text == 'Нет':
        whereami = 'proekti'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        bot.send_message(message.chat.id, text='Хорошо, что вы передумали!', reply_markup=markup)

    elif whereami == 'proekti_delete1':
        nazvanie = message.text
        flag = 0
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        for i in range(len(proekti)):
            if nazvanie == proekti[i].nazvanie:
                flag = 1
        if flag == 1:
            whereami = 'proekti_delete2'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'nazvanie.pickle', 'wb') as f:
                pickle.dump(nazvanie, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_yes, btn_no)
            bot.send_message(message.chat.id, text='Вы уверены?', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Такого проекта нет. Введите другое название.', reply_markup=markup)
    elif whereami == 'proekti_delete2' and message.text == 'Да':
        with open(userid + 'nazvanie.pickle', 'rb') as f:
            nazvanie = pickle.load(f)
        whereami = 'proekti'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        for i in range(len(proekti)):
            if proekti[i].nazvanie == nazvanie:
                proekti.pop(i)
                break
        with open(userid + 'proekti.pickle', 'wb') as f:
            pickle.dump(proekti, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu, btn_back_projects)
        bot.send_message(message.chat.id, text='Удаление прошло успешно!', reply_markup=markup)
    elif whereami == 'proekti_delete2' and message.text == 'Нет':
        whereami = 'proekti'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_back_projects)
        bot.send_message(message.chat.id, text='Хорошо, что вы передумали!', reply_markup=markup)

    elif whereami == 'proekti_create1':
        proekt = Proekt(message.text)
        nazvanie = message.text
        flag = 0
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        for i in range(len(proekti)):
            if nazvanie == proekti[i].nazvanie:
                flag = 1

        if flag == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Введите другое название', reply_markup=markup)
        else:
            proekti.append(proekt)
            whereami = 'proekti'
            with open(userid + 'proekti.pickle', 'wb') as f:
                pickle.dump(proekti, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Проект успешно создан!', reply_markup=markup)

    elif whereami == 'zametki_add1':
        with open(userid + 'zametki.pickle', 'rb') as f:
            zametki = pickle.load(f)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if message.text in zametki.keys():
            markup.add(btn_mainmenu, btn_backnotes)
            bot.send_message(message.chat.id, text='Введите другое название', reply_markup=markup)
        else:
            zametki[message.text] = ''
            whereami = 'zametki_add2'
            nazvanie = message.text
            with open(userid + 'nazvanie.pickle', 'wb') as f:
                pickle.dump(nazvanie, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'zametki.pickle', 'wb') as f:
                pickle.dump(zametki, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text='Введите текст')
    elif whereami == 'zametki_add2':
        whereami = 'zametki'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_notes)
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'zametki.pickle', 'rb') as f:
            zametki = pickle.load(f)
        with open(userid + 'nazvanie.pickle', 'rb') as f:
            nazvanie = pickle.load(f)
        zametki[nazvanie] = message.text
        with open(userid + 'zametki.pickle', 'wb') as f:
            pickle.dump(zametki, f, pickle.HIGHEST_PROTOCOL)
        bot.send_message(message.chat.id, text='Заметка создана', reply_markup=markup)
    elif whereami == 'zametki_read1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        with open(userid + 'zametki.pickle', 'rb') as f:
            zametki = pickle.load(f)
        if message.text in zametki.keys():
            whereami = 'zametki_read2'
            markup.add(btn_backnotes, btn_edit_notes)
            nazvanie = message.text
            with open(userid + 'nazvanie.pickle', 'wb') as f:
                pickle.dump(nazvanie, f, pickle.HIGHEST_PROTOCOL)
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text=zametki[message.text], reply_markup=markup)
        else:
            markup.add(btn_mainmenu,btn_backnotes)
            bot.send_message(message.chat.id, text='Такой заметки нет. Введите другое название.', reply_markup=markup)
    elif whereami == 'zametki_read2':
        if message.text == 'Редактировать заметку':
            whereami = 'zametki_edit'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_backnotes)
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text='Введите новый текст', reply_markup=markup)
    elif whereami == 'zametki_edit':
        with open(userid + 'nazvanie.pickle', 'rb') as f:
            nazvanie = pickle.load(f)
        with open(userid + 'zametki.pickle', 'rb') as f:
            zametki = pickle.load(f)
        zametki[nazvanie] = message.text
        with open(userid + 'zametki.pickle', 'wb') as f:
            pickle.dump(zametki, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_backnotes)
        bot.send_message(message.chat.id, text='Все прошло успешно', reply_markup=markup)
    elif whereami == 'zametki_delete1':
        whereami = 'zametki_delete2'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        nazvanie = message.text
        with open(userid + 'nazvanie.pickle', 'wb') as f:
            pickle.dump(nazvanie, f, pickle.HIGHEST_PROTOCOL)
        with open(userid + 'zametki.pickle', 'rb') as f:
            zametki = pickle.load(f)
        if nazvanie not in zametki.keys():
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_backnotes)
            whereami = 'zametki'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            bot.send_message(message.chat.id, text='Такой заметки не существует', reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_yes, btn_no)
            bot.send_message(message.chat.id, text='Вы уверены?', reply_markup=markup)
    elif whereami == 'zametki_delete2' and message.text == 'Да':
        with open(userid + 'nazvanie.pickle', 'rb') as f:
            nazvanie = pickle.load(f)
        with open(userid + 'zametki.pickle', 'rb') as f:
            zametki = pickle.load(f)
        del zametki[nazvanie]
        with open(userid + 'zametki.pickle', 'wb') as f:
            pickle.dump(zametki, f, pickle.HIGHEST_PROTOCOL)
        whereami = 'zametki'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_backnotes)
        bot.send_message(message.chat.id, text='Заметка успешно удалена!', reply_markup=markup)
    elif whereami == 'zametki_delete2' and message.text == 'Нет':
        whereami = 'zametki'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_backnotes)
        bot.send_message(message.chat.id, text='Хорошо, что Вы передумали', reply_markup=markup)
    elif whereami == 'zametki_delete_all' and message.text == 'Да':
        zametki = dict()
        with open(userid + 'zametki.pickle', 'wb') as f:
            pickle.dump(zametki, f, pickle.HIGHEST_PROTOCOL)
        whereami = 'mainmenu'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_mainmenu)
        bot.send_message(message.chat.id, text='Все заметки были удалены', reply_markup=markup)
    elif whereami == 'zametki_delete_all' and message.text == 'Нет':
        whereami = 'zametki'
        with open(userid + 'whereami.pickle', 'wb') as f:
            pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn_backnotes)
        bot.send_message(message.chat.id, text='Хорошо, что вы передумали!', reply_markup=markup)
    elif whereami == 'stage_read':
        nazvanie_stage = message.text
        with open(userid + 'proekti.pickle', 'rb') as f:
            proekti = pickle.load(f)
        with open(userid + 'number.pickle', 'rb') as f:
            number = pickle.load(f)
        if nazvanie_stage in proekti[number].stages.keys():
            whereami = 'proekti'
            with open(userid + 'whereami.pickle', 'wb') as f:
                pickle.dump(whereami, f, pickle.HIGHEST_PROTOCOL)
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text=proekti[number].stages[nazvanie_stage], reply_markup=markup)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(btn_mainmenu, btn_back_projects)
            bot.send_message(message.chat.id, text='Такого этапа нет. Введите другое название.', reply_markup=markup)


bot.infinity_polling(timeout=10, long_polling_timeout = 5)
