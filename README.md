# KasperDB

`KasperDB` - это упрощенная в использовании локальная база данных для `Python`. Он предоставляет простой и интуитивно понятный интерфейс для хранения и управления данными в вашем приложении.

# Пример использования
```python
from kasperdb import db, config
import random

config.debug = True #логи в консоли о действиях дб можно убрать.

db.create("t") #создать базу данных под названием t

data = db.get("t") #получаем то, что у нас в базе
print(data) #выводим базу

f = ["you're gay!", "you're not gay!"] #список "хрени"
data["you're gay?"] = random.choice(f) #записываем в переменную базы данных хандом херню из списка
db.set("t", data) #записываем новые данные

print(db.get("t")) #выводим результат добавления данных

db.delete("t") #удаляем базу данных t
```

# Как установить
напишите в консоль комманду `pip install kasperdb`

# Особенности KasperDB

- Простота в использовании
- Локальное хранение данных
- Поддержка хранения различных типов данных, таких как строки, списки и словари
- Возможность создания нескольких баз данных
- Логирование действий базы данных

`KasperDB` - отличное решение для управления данными в небольших проектах `Python`. Его простота в использовании и локальное хранение данных делают его идеальным выбором для быстрого и эффективного хранения и управления вашими данными.
