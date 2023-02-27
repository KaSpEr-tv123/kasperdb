# kasperdb

Упрощённая в использовании база данных для python. ЛОКАЛЬНАЯ БАЗА ДАННЫХ

# пример кода:

<p>

from kasperdb import db, config

import random

confi.debug = True#логи в консоли о действиях дб можно убрать.

db.create("t")#создать базу данных под названием t

data = db.get("t")#получаем то что у нас в базе

print(data)#выводим базу

f = ["you gay!", "you not gay!"]#список хрени

data["you gay?"] = random.choice(f)#записуем в переменную базы данных хандом херню из списка

db.set("t", data)#записуем новые данные

print(db.get("t"))#выводим результат добавления данных

db.delete("t")#удаляем базу данных t</p>
