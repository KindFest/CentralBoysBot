import requests
import json


def get_anekdot():
    url = "https://anekdot.ru/"
    req = requests.get(url)
    start_pos = req.text.   find("<div class=\"favor_random wordwrap\" onclick=\"goUrl('/random/anekdot/');\">")
    end_pos = req.text.find("<div class=\"fr sm red link\" onclick=\"goUrl('/random/anekdot/');\">ещё &gt;</div></div>")
    anekdot = req.text[start_pos + 72:end_pos].replace('<br>', '\n').rstrip()
    return anekdot


def datebase(command, chat_id):
    if command == '/start' or command == '/start@CentralBoysBot':
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            if data[item].get('anekdot'):
                if data[item]['anekdot']['chat_id'] == chat_id and data[item]['anekdot']['is_chat_active']:
                    answer = 'Бот уже активирован'
                    break
                elif data[item]['anekdot']['chat_id'] == chat_id and not data[item]['anekdot']['is_chat_active']:
                    data[item]['anekdot']['is_chat_active'] = True
                    answer = 'Бот активирован'
                    break
        else:
            data[str(len(data) + 1)] = {'anekdot': {
                'chat_id': chat_id,
                'is_chat_active': True,
                'is_timer_active': False
                }}
            answer = 'Бот активирован'
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            return answer
    elif command == '/stop' or command == '/stop@CentralBoysBot':
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            if data[item].get('anekdot'):
                if data[item]['anekdot']['chat_id'] == chat_id and data[item]['anekdot']['is_chat_active']:
                    answer = 'Бот остановлен'
                    data[item]['anekdot']['is_chat_active'] = False
                    data[item]['anekdot']['is_timer_active'] = False
                    break
                elif data[item]['anekdot']['chat_id'] == chat_id and not data[item]['anekdot']['is_chat_active']:
                    data[item]['anekdot']['is_chat_active'] = False
                    data[item]['anekdot']['is_timer_active'] = False
                    answer = 'Бот и не был активирован'
                    break
        else:
            answer = 'Сначала нужно активировать бота командой /start'
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            return answer
    elif command == '/anekdot' or command == '/anekdot@CentralBoysBot':
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            if data[item].get('anekdot'):
                if data[item]['anekdot']['chat_id'] == chat_id and data[item]['anekdot']['is_chat_active']:
                    answer = get_anekdot()
                    break
                elif data[item]['anekdot']['chat_id'] == chat_id and not data[item]['anekdot']['is_chat_active']:
                    answer = 'Сначала нужно активировать бота командой /start'
                    break
        else:
            answer = 'Сначала нужно активировать бота командой /start'
        return answer
    elif command == '/timer' or command == '/timer@CentralBoysBot':
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            if data[item].get('anekdot'):
                if data[item]['anekdot']['chat_id'] == chat_id and data[item]['anekdot']['is_chat_active']:
                    if data[item]['anekdot']['is_timer_active']:
                        data[item]['anekdot']['is_timer_active'] = False
                        answer = 'Функция таймера отключена'
                        break
                    elif not data[item]['anekdot']['is_timer_active']:
                        data[item]['anekdot']['is_timer_active'] = True
                        answer = 'Функция таймера активирована'
                        break
        else:
            answer = 'Сначала нужно активировать бота командой /start'
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            return answer
