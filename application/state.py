MENU_LOADING = 0
MENU_NEWS = 1
MENU_TIMETABLE = 2
MENU_EMAIL = 3

from PySide6.QtCore import QObject, Signal

class ObservableList(QObject):
    changed = Signal()

    def __init__(self, items: list = []):
        super().__init__()
        self._list = items

    def append(self, item):
        self._list.append(item)
        self.changed.emit()

    def remove(self, item):
        self._list.remove(item)
        self.changed.emit()

    def pop(self):
        self._list.pop()
        self.changed.emit()

    def __iter__(self):
        return iter(self._list)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]

class AppState():
    def __init__(self):
        self.menustack: ObservableList = ObservableList([MENU_NEWS])

state = AppState()