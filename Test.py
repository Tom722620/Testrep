import os
import subprocess
from datetime import datetime, timedelta

# Установка параметров Git (должно быть выполнено только один раз)

git_config_name = input("git_config_name: ")
git_token = input("git_token: ")


print(f"Настройка Git: user.name={git_config_name}")
subprocess.run(['git', 'config', '--global', 'user.name', git_config_name], check=True)
subprocess.run(['git', 'config', '--global', 'credential.helper', 'store'], check=True)

# Сохранение токена в качестве учетной записи Git
git_credential = f'https://x-access-token:{git_token}@github.com'
subprocess.run(['git', 'credential', 'approve'], input=f'url={git_credential}\n'.encode(), check=True)

try:
    subprocess.run(['git', 'init'], check=True)
    print("Репозиторий успешно инициализирован.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при инициализации репозитория: {e}")
    exit(1)

# Создание файла test.txt со случайными датами коммитов
print("Создание файла test.txt с коммитами...")
with open('test.txt', 'w') as file:
    current_date = datetime.now()
    for i in range(250):
        new_date = current_date - timedelta(days=i)
        formatted_date = new_date.strftime('%c %z')  # Формат даты, который понимает Git
        file.write(formatted_date + '\n')

# Добавление всех файлов в индекс Git
try:
    subprocess.run(['git', 'add', '.'], check=True)
    print("Файлы успешно добавлены в индекс Git.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при добавлении файлов в индекс Git: {e}")
    exit(1)

# Создание коммита
commit_message = "Automated commit"
try:
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)
    print(f"Коммит с сообщением '{commit_message}' успешно создан.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при создании коммита: {e}")
    exit(1)

# Отправка изменений на удалённый репозиторий
try:
    subprocess.run(['git', 'push', '-u', 'https://github.com/Tom722620/Testrep', 'master'], check=True)
    print("Изменения успешно отправлены на удалённый репозиторий.")
except subprocess.CalledProcessError as e:
    print(f"Ошибка при отправке изменений на удалённый репозиторий: {e}")
    exit(1)
