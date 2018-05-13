import pickle

name_lst = ['Touhid', 'Raisul', 'Bithy']

with open('pickle_file', 'wb') as pickle_name_lst:
    pickle.dump(name_lst, pickle_name_lst)
    print(name_lst)

with open('pickle_file', 'rb') as pickle_name_red:
    b = pickle.load(pickle_name_red)
    print(b)

print(name_lst == b)