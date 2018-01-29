try:
    with open('webapp') as fh:
        file_data = fh.read()
    print(file_data)

except FileNotFoundError as e:
    print('The data file is missing.', e.strerror)
except PermissionError as e:
    print('This is not allowed.', e.strerror)
except Exception as e:  # handle all possible exceptions
    print('Some other error occurred.', str(e))
finally:
    print("It's finally block.")


