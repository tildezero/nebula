import traceback

""" misc utils functions, mostly skidded """


def traceback_maker(err, advance: bool = True):
    """ 
    A way to debug your code anywhere 
    Source: https://github.com/AlexFlipnote/discord_bot.py/blob/master/utils/default.py
    """
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"

def chunks(lst, n):
    """
    Yield successive n-sized chunks from lst.
    Source: https://stackoverflow.com/a/312464
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def calc(data):
    total = 0
    for item in data:
        total += int(data[item])
    return total