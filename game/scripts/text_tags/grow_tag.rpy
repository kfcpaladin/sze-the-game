init -1 python:
    
    def grow_tag(tag, argument, contents):
        """ Custom text tag for making text change size dynamically
        Usages: {grow}Hello world!{/grow}
                {grow=100}Custom end size{/grow}
                {grow=15...60}Custom range{/grow}
                {grow=60...15}Shrinking text{/grow}
        """
        texts = filter(lambda c: c[0] == renpy.TEXT_TEXT, contents)        
        total_characters = sum((len(text) for _, text in texts))
        start_size, end_size = range_from_args(argument)        
        gen = float_range(start_size, end_size, total_characters)

        rv = []
        for kind, text in contents:
            if kind is not renpy.TEXT_TEXT:
                rv.append((kind, text))
                continue

            for char in text:
                size = int(next(gen))
                rv.append((renpy.TEXT_TAG, u"size={}".format(size)))
                rv.append((renpy.TEXT_TEXT, char))
                rv.append((renpy.TEXT_TAG, u"/size"))

        return rv

    config.custom_text_tags["grow"] = grow_tag 

    class GrowTagException(Exception):
        def __init__(self, argument, msg=None):
            error = "Invalid grow tag argument '{0}'".format(argument)
            if msg is not None:
                error = "{0}. Reason: {1}".format(error, msg)
            Exception.__init__(self, error)

    def range_from_args(argument, start=22, end=40):
        """ Convert argument string into an integer range
        None = (start, end)
        "10" = (start, 10)
        "15...100" = (15, 100)
        """

        if not argument:
            return (start, end)

        try:
            # argument = integer
            end_size = int(argument)
            if end_size < 0:
                raise GrowTagException(argument, "Cannot have negative size")
            return (start, end_size)
        except ValueError:
            pass

        # argument = range x...y
        args = argument.split("...")
        if len(args) != 2:
            raise GrowTagException(argument, "Expected range start...end")
        
        try:
            start_size = int(args[0])
            end_size = int(args[1])
            return (start_size, end_size)
        except ValueError:
            raise GrowTagException(argument, "Expected start...end to be integers")


    def float_range(start, end, total):
        step = float(end-start)/float(total)
        value = start
        for _ in range(total):
            yield value 
            value += step