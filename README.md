# Ifrita Kowaldi

**Важно!** Скрипт в самой первой версии, должным образом не тестировался. Был написан на скорую руку, в переспективе будет развиваться и улучшаться.

Скрипт вытаскивает с сайта codeforces примеры входных/выходных для каждой задачи,
и проверяет соответсвующие программы на выполнение примеров.


### Как пользоваться

В *CONTEST* поместить номер интересующего соревнования. 
Номер можно увидеть в адресной строке браузера
В словарь *programs* добавить элементы *key*, *value*, где
*key* - номер задачи, как в адресной строке
*value* - путь к исполняемому файлу, для соответствующей задачи

#### Пример:

```python
CONTEST = 928

programs = {
    "A": "./a",
    "B": "./b",
    "C": "./c",
    "D": "./d",
}
```

Вывод скрипта:

```
Problem A

    Test1: OK! 

    Test2: OK! 

    Test3: OK! 

    Test4: OK! 

    Test5: OK! 

    Test6: OK! 

Problem B

    Test1: OK! 

    Test2: OK! 

    Test3: OK! 

Problem C

    Test1: OK! 

    Test2: OK! 

    Test3: OK! 

Problem D

    Test1: FAIL
        Input: snow affects sports such as skiing, snowboarding, and snowmachine travel. snowboarding is a recreational activity and olympic and paralympic sport.
        Output: 141
        Your answer: Yes

    Test2: FAIL
        Input: 'co-co-co, codeforces?!'
        Output: 25
        Your answer: Yes

    Test3: FAIL
        Input: thun-thun-thunder, thunder, thunder thunder, thun-, thunder thun-thun-thunder, thunder thunder, feel the thunder lightning then the thunder thunder, feel the thunder lightning then the thunder thunder, thunder
        Output: 183
        Your answer: Yes
```
