# LazyBomberman
Another try at bombermaning, now with Python and Cocos2d

## Как работать с GitHub.com

"Течение GitHub" (GitHub flow, workflow) - процесс работы с GitHub, описанный с помощью презентации и краткого справочника, требует незначительных навыков работы с Git, а также следования идеям:
* В ветке master всегда находится текущая **работающая** версия
* Общее планирование и проектирование проводится в wiki
* Для предложения новой функциональности или пачта создается задание issue, в котором ведется обсуждение будущей работы
* Для разработки новой функциональности или патча на основе задания issue создается своя ветвь разработки
* В ветке ведется разработка, состояния commit фиксируются и комментируются
* После окончания разработки ветви, ее сливают с главной веткой master посредством pull request, в котором обсуждается проведенная работа и любые шаги для доработки до приемлемого состояния
* Закрытие задания случается, когда в ветке master после pull request оказывается commit с комментарием, содержащим `fixed #n`, n - номер issue

Презентация: https://guides.github.com/introduction/flow/

Справочник: https://help.github.com/articles/github-flow-in-the-browser/

## Правила ведения документации в Python

В Python существует четыре вида комментариев:

1. Простой комментарий - используется в середине кода для улучшения понимания, зачастую заменяется на вменяемые названия функций и переменных, а также на помогающие функции
2. Комментарий для функции/метода - ставится на следующей строке после `def func():`, используется для явного указания на действие функции/метода. Может быть использован для автоматической генерации документации, а также доступен как строка внутри программы по имени `func.__doc__` и с помощью `help(func)`
3. Комментарий для класса - ставится на следующей строке после `class C:`, используется для описания переменных класса и объекта ("внутреннего состояния") и краткой справки по методам класса. Также как и предыдущий, может быть использован для автоматической генерации документации, а также доступен как строка внутри программы по имени `C.__doc__` и с помощью `help(C)`
4. Комментарий для модуля - ставится на первой строке модуля (файла), используется для описания функциональности модуля (что может сделать этот модуль). Также как и предыдущий, может быть использован для автоматической генерации документации, а также доступен как строка внутри программы по имени `name.__doc__` и с помощью `help(name)`

Последние три типа комментариев следует считать обязательными, вне зависимости ни от каких внешних и внутренних обстоятельств.

Писать комментарии можно на русском языке, с примерами можно ознакомиться в файле `template.py`. Форматирование не обязательно.

Особые правила:
* Все параметры метода `__init__` обязательно должны быть задокументированы
* Если у функции/метода есть возвращаемое значение, его тип обязательно должен быть указан в комментарии
* Если функция/метод могут выбросить исключение, его тип обязательно должен быть указан в комментарии
* Если у модуля/класса/метода/функции нет комментария - его надо написать сейчас