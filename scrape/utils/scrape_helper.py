

class ScrapeHelper:

    @staticmethod
    def elementFind(callback, **params):
        callback(params)
        
    @staticmethod
    def defer(callback, *args, **kwargs):
        return lambda: callback(*args, **kwargs)