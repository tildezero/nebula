import traceback

""" misc utils functions """


def traceback_maker(err, advance: bool = True):
    """ 
    A way to debug your code anywhere 
    Source: https://github.com/AlexFlipnote/discord_bot.py/blob/master/utils/default.py
    """
    _traceback = ''.join(traceback.format_tb(err.__traceback__))
    error = ('```py\n{1}{0}: {2}\n```').format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"