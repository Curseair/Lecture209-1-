def create_dict(states):
    d = {}
    for state in states:
        abbr, full, capital = state.split(",")
        #adding an item (key-value pair) to the dictionary
        d[abbr] = [full, capital]
    return d

def display(d): #takes dictionary and prints it in a format
    for k,v in d.items():
        print('{}--{}'.format(k, '--'.join(v))) #.join function converts a list to a string

def add_state(d,user_abbr, user_full, user_capital):
    d[user_abbr] = [user_full, user_capital] #adds user key, values or abbr, full/capital to the dict