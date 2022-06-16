# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

user2 = {
        'name': 'Spammer McSpam',
        'valid': False
}

def authenticated(fn):
  def wrapper(user):
      if user['valid'] == True:
          fn(user)
      else:
          user_name = user['name']
          print(f'{user_name} is not a valid user')
  return wrapper


@authenticated
def message_friends(user):
    print('Message has been sent')


# test a valid user
message_friends(user1)  # should return Message has been sent

# test an invalid user
message_friends(user2) # Spammer McSpam is not a valid user
