from kasperdb.functions import Json
import kasperdb.config as config
import os
try:
  from colorama import Fore, init
  init()
except:
  os.system("pip install colorama")
  from colorama import Fore, init
  init()
data = {

}

def create(db_name):
    Json.set(f"{db_name}.json", data)
    if config.debug:
      print(Fore.GREEN + f"база данных {db_name} создана")

def get(db_name):
  try:
    data = Json.get(f"{db_name}.json")
    if config.debug:
      print(Fore.GREEN + "данные успешно получены")
    if data == {}:
      print(Fore.YELLOW + "база данных пустая")
      return
    else:
       return data
    
  except:
    print(Fore.RED + f"базы данных {db_name} не существует ")
    return

def set(db_name, data):
  try:
    Json.set(f"{db_name}.json", data)
    if config.debug:
      print(Fore.GREEN + "данные успешно обновлены")
    if data == None:
       print(Fore.YELLOW +"нечего добавлять.")
    else:
       return
    
  except:
    print(Fore.RED + f"базы данных {db_name} не существует ")
    return

def delete(db_name):
  try:
    os.remove(f"{db_name}.json")
    if config.debug:
      print(Fore.GREEN + f"база данных {db_name} успешно удалена")
    else:
       return data
  except:
    print(Fore.RED + f"базы данных {db_name} не существует ")
    return