from field import water

def missle_test():
    # this is where we append
    missle_fired = water[1]
    #this is what we replace our string with
    missle_fired[0] = "M"
    print(water)
missle_test()