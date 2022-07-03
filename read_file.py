import pandas as pd


def add_to_dictionary():
    pan = pd.read_excel('http://asbadrah.ir/tele-bot/NNS/novin.xlsx?id=1')
    df = pd.DataFrame(pan, )
    name = df['name'].tolist()
    code = df['code'].tolist()
    dict = {}
    for i in range(0, len(name)):
        dict[code[i]] = name[i]
    return dict

def list_of_products_by_code():
  pan = pd.read_excel('http://asbadrah.ir/tele-bot/NNS/novin.xlsx')
  df = pd.DataFrame(pan, )
  codes = df['code'].tolist()
  names = df['name'].tolist()
  products = list(zip(codes, names))
  str = ""
  for code, name in products:
    str += f'{code}: {name}\n'
  print(str)
  return str

def list_of_products_by_name():
  pan = pd.read_excel('http://asbadrah.ir/tele-bot/NNS/novin.xlsx')
  df = pd.DataFrame(pan, )
  names = df['name'].tolist()
  products = ', '.join(names)
  return products
