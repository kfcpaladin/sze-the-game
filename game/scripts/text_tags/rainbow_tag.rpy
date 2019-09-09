init -2 python:
    from util.colours import RainbowColour

    def rainbow_tag(tag, argument, contents):
        """ Custom text tag which makes text change colour for each character 
            inside the tag
        Usage:  {rainbow}Default rainbow text!{/rainbow}
                {rainbow=10}Slower rainbow transition{/rainbow}
                {rainbow=200}Faster rainbow transition{/rainbow}
        """
        if not argument:
            argument = 100

        rate = int(argument)
        rainbow = RainbowColour()

        rv = []
        for kind, text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    rv.append((renpy.TEXT_TAG, u"color={}".format(rainbow)))
                    rv.append((renpy.TEXT_TEXT, char))
                    rv.append((renpy.TEXT_TAG, u"/color"))
                    rainbow.update(rate)
            else:
                rv.append((kind, text))
        
        return rv
    
    config.custom_text_tags["rainbow"] = rainbow_tag
    
    

        
