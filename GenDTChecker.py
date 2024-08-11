import asyncio
import os
import sys
from aiohttp import ClientSession
from colorama import Fore, Style, init

init(autoreset=True) 

class Geniuszly:
    def __init__(self, token=None):
        self.user_token = token if token else input(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Введите токен: ').strip()
        if not self.user_token:
            print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Токен не может быть пустым. Пожалуйста, введите действительный токен.")
            return
        self.print_logo()
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Проверка токена...\n')
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        asyncio.run(self.verify_token())

    def print_logo(self):
        logo = f"""
{Fore.LIGHTYELLOW_EX}   _____            _____ _______ _____ _               _             
  / ____|          |  __ \__   __/ ____| |             | |            
 | |  __  ___ _ __ | |  | | | | | |    | |__   ___  ___| | _____ _ __ 
 | | |_ |/ _ \ '_ \| |  | | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| |  __/ | | | |__| | | | | |____| | | |  __/ (__|   <  __/ |   
  \_____|\___|_| |_|_____/  |_|  \_____|_| |_|\___|\___|_|\_\___|_|   
                                                                                  
        """
        print(logo)
        print(f"""
        {Fore.LIGHTYELLOW_EX}╭────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╮
        | {Fore.LIGHTGREEN_EX}Используйте: python {os.path.basename(__file__)} [OPTION]                    {Fore.LIGHTYELLOW_EX}| 
        | {Fore.LIGHTGREEN_EX}Параметры:                                              {Fore.LIGHTYELLOW_EX}| 
        | {Fore.LIGHTGREEN_EX}-help       Показать эту справку                        {Fore.LIGHTYELLOW_EX}| 
        | {Fore.LIGHTGREEN_EX}-token      Указать токен Discord для проверки          {Fore.LIGHTYELLOW_EX}| 
        ╰────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╯
        """)

    async def verify_token(self):
        headers = {
            'Authorization': self.user_token,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'
        }

        # Создание сессии для общения с API Discord
        try:
            async with ClientSession(headers=headers) as session:
                # Проверка доступности токена
                async with session.get('https://discordapp.com/api/v6/users/@me/library') as response:
                    if response.status != 200:
                        error_message = (await response.json()).get("message", "Ошибка при проверке токена.")
                        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [ЗАБЛОКИРОВАНО] {Fore.LIGHTRED_EX}{error_message}')
                        return

                # Получение информации о пользователе через API Discord
                async with session.get("https://discordapp.com/api/v6/users/@me") as user_info:
                    user_data = await user_info.json()
                    self.display_user_info(user_data)
        except Exception as e:
            print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Произошла ошибка: {Fore.LIGHTRED_EX}{e}")

    def display_user_info(self, user_data):
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [ЗАБЛОКИРОВАНО] {Fore.LIGHTRED_EX}Ложно')
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [ТЕГ] {Fore.LIGHTGREEN_EX}{user_data.get("username", "Неизвестно")}#{user_data.get("discriminator", "Неизвестно")}')
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [EMAIL] {Fore.LIGHTGREEN_EX}{user_data.get("email", "Не указан")}')
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [ID] {Fore.LIGHTGREEN_EX}{user_data.get("id", "Не указан")}')
        
        phone_status = "✓" if user_data.get("phone") else "✗"
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [ТЕЛЕФОН] {Fore.LIGHTGREEN_EX}{phone_status}')
        
        email_verified_status = "✓" if user_data.get("verified") else "✗"
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [EMAIL ВЕРИФИЦИРОВАН] {Fore.LIGHTGREEN_EX}{email_verified_status}')
        
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_data.get("id", "")}/{user_data.get("avatar", "")}.png?size=256'
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» [АВАТАР] {Fore.LIGHTGREEN_EX}{avatar_url}')

        self.save_user_data(user_data)

    def save_user_data(self, user_data):
        """Сохраняет информацию о пользователе в файл."""
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_data.get("id", "")}/{user_data.get("avatar", "")}.png?size=256'
        with open("user_data.txt", "w", encoding="utf-8") as f:
            f.write("Информация о пользователе:\n")
            f.write(f'Тег: {Fore.LIGHTGREEN_EX}{user_data.get("username", "Неизвестно")}#{user_data.get("discriminator", "Неизвестно")}\n')
            f.write(f'Email: {Fore.LIGHTGREEN_EX}{user_data.get("email", "Не указан")}\n')
            f.write(f'ID: {Fore.LIGHTGREEN_EX}{user_data.get("id", "Не указан")}\n')
            f.write(f'Телефон: {Fore.LIGHTGREEN_EX}{"✓" if user_data.get("phone") else "✗"}\n')
            f.write(f'Email верифицирован: {f"{Fore.LIGHTGREEN_EX}✓" if user_data.get("verified") else f"{Fore.LIGHTRED_EX}✗"}\n')
            f.write(f'Аватар: {Fore.LIGHTGREEN_EX}{avatar_url}\n')
        print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Информация о пользователе сохранена в файл {Fore.LIGHTGREEN_EX}user_data.txt")

    @staticmethod
    def print_help():
        print("""{Fore.LIGHTYELLOW_EX}   _____            _____ _______ _____ _               _             
  / ____|          |  __ \__   __/ ____| |             | |            
 | |  __  ___ _ __ | |  | | | | | |    | |__   ___  ___| | _____ _ __ 
 | | |_ |/ _ \ '_ \| |  | | | | | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | |__| |  __/ | | | |__| | | | | |____| | | |  __/ (__|   <  __/ |   
  \_____|\___|_| |_|_____/  |_|  \_____|_| |_|\___|\___|_|\_\___|_|   
        """)
        print(f"""
        {Fore.LIGHTYELLOW_EX}╭────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╮
        | {Fore.LIGHTGREEN_EX}Используйте: python {os.path.basename(__file__)} [OPTION]                    {Fore.LIGHTYELLOW_EX}| 
        | {Fore.LIGHTGREEN_EX}Параметры:                                              {Fore.LIGHTYELLOW_EX}| 
        | {Fore.LIGHTGREEN_EX}-help       Показать эту справку                        {Fore.LIGHTYELLOW_EX}| 
        | {Fore.LIGHTGREEN_EX}-token      Указать токен Discord для проверки          {Fore.LIGHTYELLOW_EX}| 
        ╰────────────────────━━━━━━━━━━━━━━━━━━━━━────────────────╯
        """)

if __name__ == '__main__':
    if '-help' in sys.argv:
        Geniuszly.print_help()
    elif '-token' in sys.argv:
        try:
            token_index = sys.argv.index('-token') + 1
            if token_index < len(sys.argv):
                token = sys.argv[token_index]
                os.system('cls' if os.name == 'nt' else 'clear')
                checker = Geniuszly(token=token)
            else:
                print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Ошибка: Токен не указан. Используйте -help для получения помощи.")
        except IndexError:
            print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenDTChecker {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» {Fore.LIGHTYELLOW_EX}Ошибка: Токен не указан. Используйте -help для получения помощи.")
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        checker = Geniuszly()
