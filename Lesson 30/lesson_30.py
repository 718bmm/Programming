def plus(num=0):
    try:
        if num: # False
            return int(num) + 5
        else:
            return 'please enter a number'
    except ValueError as err:
        return err
    

if __name__ == "__main__":
    # assert plus(5) == 0, 'Code is not working!'
    # assert plus('a') == 10, 'Code is not working!'
    print(plus(5))
    print(plus('5'))
    print(plus('-1'))
    print(plus('a'))