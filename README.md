# pytest
Автотесты на питоне

Для успешного запуска тестов на Вашем компьютере нужно сделать следующее:

1) Установить Python

2) Установить утилилиту Virtualenv (в командной строке: pip install vitrualenv)

3) Создать виртуальное окружение:
    Для Win: virtualenv env
    Для Mac: python3 -m venv env
    
4) Активировать виртуальное окружение:
    для Win: env\Scripts\activate
    для Mac: source env/bin/activate
    
5) Установить необходимые фреймворки:
    а) Selenium - pip install selenium
    б) Pytest - pip install pytest
    в) Pytest-repeat - pip install pytest-repeat
    г) Pytest-ordering - pip install pytest ordering
    
6) Установить последнюю версию chromedriver или geckodriver (в зависимости от используемого браузера, или можно оба сразу)
Для этого:
Если у Вас win: скопировать драйвер в папку с Python (например C:\Python36)
Если у Вас mac:
    а) Установите Homebrew - для этого откройте терминал и напишете следующую команду: 
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    б) Установить нужный драйвер с помощью Homebrew: brew cask install chromedriver
    
Готово! Теперь можно запускать тесты
Для того чтобы запустить один из тестов - выполните команду: pytest 'название файла' (например pytest test_reg.py)
Для того чтобы запустить все тесты сразу - находясь в папке с тестами, выполните следующую команду: pytest
