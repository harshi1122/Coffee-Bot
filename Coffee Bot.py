def print_message():
  print ("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def coffee_bot():
  size=get_size()
  drink_type = get_drink_type()
  print("Welcome to the cafe!")
  print('Alright, that\'s a {} {}!'.format(size, drink_type))
  name=input("Can I get your name please?")
  print('Thanks, {}! Your drink will be ready shortly.'.format(name))
  
def get_size():
  res = input('What size drink can I get for you? Select a/b/c \n[a] Small \n[b] Medium \n[c] Large \n> ')
  if res=='a':
    return 'Small'
  elif res=='b':
    return 'Medium'
  elif res=='c':
    return 'Large'
  else:
    print_message()
    get_size()
    
def get_drink_type():
  res=input('What drink type do you prefer? Select a/b/c \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ')
  if res=='a':
    return 'Brewed Coffee'
  elif res=='b':
    return 'Mocha'
  elif res=='c':
    return order_latte()
  else:
    print_message()
    get_drink_type()

def order_latte():
  res=input('And what kind of milk for your latte? /n[a] 2% milk /n[b] Non-fat milk /n[c] Soy milk')
  if res=='a':
    return 'Latte'
  elif res=='b':
    return 'Non Fat Latte'
  elif res=='c':
    return 'Soy Latte'
  else:
    print_message()
    order_latte()
coffee_bot()
