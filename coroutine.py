def search_in_this_list():
    import time
    str = ['thid is a string']
    time.sleep(4)

    while True:
        text = (yield)
        if text in str:
            print('it is there')
        else:
            print('not in there')

search = search_in_this_list()
next(search)
search.send('is')
search.close()
