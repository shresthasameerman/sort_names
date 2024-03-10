'''5. Write a function to accept a list of names and return the sorted order of names back.'''
def sort_names():
    input_names = input("enter the list of names of your friends seperated by commas: ")
    names = input_names.split(',')
    sorted_names = sorted(names)
    print(sorted_names)
sort_names()
