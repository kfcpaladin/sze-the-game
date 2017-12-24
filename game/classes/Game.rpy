python early:
    class Game:
        def __init__(self, options):
            self.options = []
            self._baseOptions = {
                "currentTime": {}
            }
            # Adding base options
            self.addOptions(self._baseOptions)
            self.addOptions(options)

        """
            Used to handle adding options to the game
        """
        # Add a dictionary of options with values to the game
        def addOptions(self, options):
            if type(options) is not dict:
                raise TypeError("Expected dict for game options")
            for option, value in options.iteritems():
                setattr(self, option, value)
                self.options.append(option)

        """
            Methods to handle adding, checking and modifying the game time
        """
        def addTimes(self, times):
            if type(times) is not dict:
                raise TypeError("Expected a dict for times, not {0}".format(type(timeStates)))
            for key, time in times.iteritems():
                self.currentTime[key] = time 

        def checkTime(self, time):
            if time in self.currentTime:
                return self.currentTime[time]
            else:
                return False

        # Toggle desired time to true
        def setTime(self, desiredTime):
            if desiredTime in self.currentTime:
                for time in self.currentTime:
                    self.currentTime[time] = False
                self.currentTime[desiredTime] = True
            else:
                raise AttributeError("{0} is not a valid timestate".format(desiredTime))

        """
            Allow for the modification of iterable game state variables
            These options will be checked to see if they can be done
        """
        # Modify game state variables safely
        def gain(self, option, count=1):
            self._checkIterableOption(option)
            self._changeIterableOption(option, count)

        def loss(self, option, count=1):
            self._checkIterableOption(option)
            self._changeIterableOption(option, -count)

        def set(self, option, value):
            setattr(self, option, value)

        """
            Used to increment game state variables if they are iterable,
            and check if the attribute is iterable
        """
        def _changeIterableOption(self, option, count):
            self._checkIterableOption(option)
            value = getattr(self, option)
            setattr(self, option, value + count)

        def _checkIterableOption(self, option):
            if option not in self.options:
                raise AttributeError("{0} is not a game option".format(option))
            if type(getattr(self, option)) not in (int, float):
                raise TypeError("{0} is not an iterable game option".format(option))
            return True

        """
            Used to debug the game state during execution
        """
        # describes the progress of the game
        def describe(self):
            options = self._sortOptions()
            print("[Game Status]")
            for category, option in options.iteritems():
                print("{0}:".format(category))
                for option, value in options.iteritems():
                    print(" -{0}: {1}".format(option, value))

        # Sorts a dictionary into distinct catergories
        def _sortOptions(self):
            iterable = {}   # temporary dicts to categorise game variables
            boolean = {}
            other = {}
            for option in self.options:
                value = getattr(self, option)
                valueType = type(value)
                if valueType in (int, float):
                    iterable[option] = value
                elif valueType is bool:
                    boolean[option] = value
                else:
                    other[option] = value
            return {"Iterable": iterable, "Boolean": boolean, "Other": other}
        
