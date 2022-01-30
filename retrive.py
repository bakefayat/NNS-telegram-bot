def remove_non_numerics(key):
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  list_key = [i for i in str(key) if i in numbers]
  key = ''.join(list_key)
  if key:
    return int(key)
  return False

def retrive_nns(dictionary, key):
  if dictionary.get(key):
      return dictionary.get(key)
  return False