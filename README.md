   "Как закинуть себе проект из гитхаб а потом обратно"
1. заходим в директорию будущего проекта после открывает там консоль и в консоле прописываем команду 'git clone git@github.com:VektorRozh333/yandex_scooter_project.git'
2. если он пустой то в нём создаём ветку или меняем название, создаём файлы README и .gitignore (python)
3. пишем команду 'git add .' и после делаем первый комит "git commit -m 'first commit'"
4. отправляем изменения в гитхаб командой 'git push' но если вся разработка происходила в другой ветке то перед отправкой
проводим слияние веток, главное чтобы на той ветке был сделан комит и самое важное (НИКОГДА НЕ УДАЛЯТЬ ФАЙЛЫ И ПАПКИ ВРУЧНУЮ) это вызовит конфликт в ветках

    
    "Создание среды для программирования"
1. создать виртуальное окружение в самом проекте (обязательно нужна версия python 3.9.13): python -m venv venv
2. активировать виртуальное окружение: source venv/script/activate
3. создать файл '.gitignore' в проекте и взять скопировать содержимое с файла 'Python.gitignore' в github
4. сделать абгрейд для pip 'python -m pip install pip==25.3' 
5. установка плагина 'pip install selenium==4.36.0',
удалить плагин 'pip uninstall selenium==4.36.0',
проверить список плагинов 'pip list'.
6. какие плагины требуются для проекта: 
    allure-pytest              2.16.0
    allure-python-commons      2.16.0
    attrs                      26.1.0
    certifi                    2026.5.20
    cffi                       2.0.0
    charset-normalizer         3.4.7
    chromedriver-autoinstaller 0.6.4
    colorama                   0.4.6
    exceptiongroup             1.3.1
    h11                        0.16.0
    idna                       3.18
    iniconfig                  2.1.0
    outcome                    1.3.0.post0
    packaging                  26.2
    pip                        26.0.1
    pluggy                     1.6.0
    pycparser                  2.23
    Pygments                   2.20.0
    PySocks                    1.7.1
    pytest                     8.4.2
    python-dotenv              1.2.1
    requests                   2.32.5
    selenium                   4.36.0
    setuptools                 58.1.0
    sniffio                    1.3.1
    sortedcontainers           2.4.0
    tomli                      2.4.1
    trio                       0.31.0
    trio-websocket             0.12.2
    typing_extensions          4.15.0
    urllib3                    2.6.3
    webdriver-manager          4.1.2
    websocket-client           1.9.0
    wsproto                    1.2.0
7. как правильно пользоваться ветками в своём проекте:
    прежде чем создавать ветку нужно выполнить команду 'git init',
    чтобы переименовать ветку с (master) на (main) нужно выполнить команду 'git branch --move master main'
    создать новую ветку (develop) можно с помощью команды 
    'git branch develop' а потом переключиться на неё 'git checkout develop',
    вернуться на ветку назад 'git checkout -'
    посмотреть все ветки в проекте 'git branch -a'
    переключиться на новую ветку 'git checkout develop',
    создать новую ветку и переключиться на неё 
    'git checkout -b develop',
    добавить изменения из одной ветки в другую 'git merge',
    перенести изменения из ветки (develop) в ветку (main) нужно находиться в ветке (main) и ввести 'git merge develop',
    если вдруг произошёл конфликт с ветками и у текущей ветки develop появился статус merged (develop|MERGED) то можно использовать команду 'git merge --abort' эта команда отменяет незавершённое слияние.
обязательно основной ветке прописывать название 'main'
8. добавление файла '__init__.py' для того, чтобы директория проекта должна функцианировать как пакет или подпакет.
9. сделать ревизию в файловой системе (commit) после завершении определённого этапа разработки автоматизации тестов, прежде чем делать (commit) нужно добавить в индекс все изменённые файлы и папки в текущую директорию 'git add .', после только и делается (commit)
'git commit -m "описание данных изменений"', после посмотреть статус сделанных коммитов (находятся ли они в статусе изменений) 
'git status', посмотреть список всех коммитов 'git log'.
10. Запушить свой проект в свой репозиторий на github командой 'git push'


    "Как создать ssh ключ и gitconfig"
1. зайти вдиректорию пользователя C:\Users\user
2. создать папку .ssh в ней через консоль прописать команду 'ssh-keygen -t ed25519 -C "your_email@example.com"'
3. находясь в user через консоль прописать команды 'git config --global user.name "Ваше Имя"' и 'git config --global user.email "you@example.com"'
4. добавить свой ключ в гитхаб, заходим в .ssh и копируем всё содержимое из файла id_ed25519.pub потом заходим в гитхаб в settings переходим в раздел (ssh and gpg keys)
после создаём ключ прописываем название и вставляем содержимое из файла id_ed25519.pub в раздел key


как работать с pytest
    'pytest (путь до теста/название теста)' пример 'pytest tests/test_main.page' сели путь до теста с самого начала директории 'pytest yandex_project_ui/tests/test_main_page.py'
как работать с allure
    Чтобы сохранить результаты Allure в папку yandex_project_ui, в терминале нужно находиться в данной папке и использовать комманду: 'pytest --alluredir=allure-results'
    Если сразу запустить с конкретным тестом и добавить путь к ним: 'pytest tests/test_main_page.py --alluredir=allure-results'
    Для просмотра через временный сервер: 'allure serve allure-results'
    Для статического отчёта: 'allure generate allure-results -o allure-report --clean'