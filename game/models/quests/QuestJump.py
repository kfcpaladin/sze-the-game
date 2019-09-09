from util import RenpyCallbacks

class QuestJump:
    def __init__(self, label):
        self._label = label

    def __call__(self, quest):
        RenpyCallbacks.get_instance().call_label(self._label)