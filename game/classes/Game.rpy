python early:
    class Game:
        def __init__(self, options):
            self.iterableOptions = []
            self.options = []
            for option in options:
                val = options[option]
                setattr(self, option, val)
                self.options.append(option)
                if type(val) in (int, float):
                    self.iterableOptions.append(option)

        # Modify game state variables safely
        def gain(self, option, count=1):
            self._checkIterableOption(option)
            self._changeIterableOption(option, count)

        def loss(self, option, count=1):
            self._checkIterableOption(option)
            self._changeIterableOption(option, -count)

        def set(self, option, value):
            self._checkIterableOption(option)
            setattr(self, option, value)

        def _changeIterableOption(self, option, count):
            self._checkIterableOption(option)
            optionValue = getattr(self, option)
            setattr(self, option, optionValue + count)

        def _checkIterableOption(self, option):
            if option not in self.iterableOptions:
                raise AttributeError("{0} is not a valid option in {1}".format(option, self))


        """
            Used to debug the game state during execution
        """
        # describes the progress of the game
        def describe(self):
            sortedOptions = self._sortOptions()
            print("[Game Status]")
            for category in sortedOptions:
                print("{0}:".format(category))
                options = sortedOptions[category]
                for option in options:
                    print(" -{0}: {1}".format(option, options[option]))
            
        
        def _sortOptions(self):
            iterable = {}   # temporary dicts to categorise game variables
            boolean = {}
            other = {}
            for option in self.options:
                optionValue = getattr(self, option)
                valueType = type(optionValue)
                if valueType in (int, float):
                    iterable[option] = optionValue
                elif valueType is bool:
                    boolean[option] = optionValue
                else:
                    other[option] = optionValue
            return {"Iterable": iterable, "Boolean": boolean, "Other": other}
        