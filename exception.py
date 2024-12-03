x = 2
try:
    if type(x) is not str:
        # Raise error that being in python 
        raise TypeError("Only string are allowed.")
except NameError:
    print("There is an error")
# Check what error is
except Exception as error:
    print(error)
# If the exception is not catched 
else:
    print('No errors!')
# Even the error is catched or not 
finally:
    print('The end of the program!')