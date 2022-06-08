#topics: function, dict, import
#1) convert a list to a dict
#2) how to deal with multiple .py files


import utility as u
def main():
    states = ['VA,Virginia,Richmond','FL,Flordia,Tallahassee'] #len = 2
    #dict d = {'VA': ['Virginia', 'Richmond], 'FL': ['Florida', 'Tallahassee']}
    states_dict = u.create_dict(states) #sets var to for loop that returns key and value
    u.display(states_dict)
    user_abbr = input('Enter new abbreviation: ')
    user_full = input('Enter new full form: ')
    user_capital = input('Enter new capital: ')
    u.add_state(states_dict,user_abbr, user_full, user_capital)
    u.display(states_dict)
    #changing Richmond to Fairfax through list
    states_dict['VA'] = ['Virginia', 'Fairfax']
    #Another way is to change Richmond to Fairfax:
    #states_dict['VA][-1] = 'Fairfax'
    u.display(states_dict)
main()