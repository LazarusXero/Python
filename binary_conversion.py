while True:
    key = raw_input("Input a number between 1 and 15:  ")

    try:
        key = int(key)
        bin_key = '{0:04b}'.format(key)
        
        if key > 0 and key < 16:
            print("Binary equivalent of {0} is {0:04b}" .format(key))
        else:
            print("Please enter a number 1 to 15!")
            raw_input("Press ENTER to continue.")
    except ValueError:
        print("A number needs to be pressed.")
        raw_input("Press ENTER to continue.")
        continue


