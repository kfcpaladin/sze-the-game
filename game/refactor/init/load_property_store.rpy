init -1 python:
    from refactor.util import PropertyStore
    from refactor.util import ObservableProperty

    def load_property_store():
        store = PropertyStore()

        store.add("chaoPissed", ObservableProperty(False))
        store.add("delivery", ObservableProperty(False))
        store.add("electionPromise", ObservableProperty(False))
        store.add("hasDiary", ObservableProperty(False))
        store.add("metDerek", ObservableProperty(False))
        store.add("norton", ObservableProperty(False))
        store.add("stealWillisGirl", ObservableProperty(False))
        store.add("yangRant", ObservableProperty(False))

        store.add("moxCounter", ObservableProperty(0))
        store.add("timeTravelCounter", ObservableProperty(0))
        store.add("currentDay", ObservableProperty(0))
        store.add("suicideCount", ObservableProperty(0))
        store.add("currentDiaryPage", ObservableProperty(0))

        return store
