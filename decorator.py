
user1 = {
    'name': 'Sorna',
    'valid': True
}

def authenticated(fn):
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
        return fn(*args, **kwargs)
  return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)

user1 = {
    'name': 'Sorna',
    'valid': True 
}

def authenticated(fn):
  def wrap_func(*args, **kwargs):
    if args [0] ['valid']:
      return fn (*args, **kwargs)
  return wrap_func

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
