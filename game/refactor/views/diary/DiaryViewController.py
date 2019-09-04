class DiaryViewController(object):
    def __init__(self):
        self._pages = [] 
        self._index = 0
        self._is_visible = False

    @property
    def current_page_number(self):
        return self._index

    @current_page_number.setter 
    def current_page_number(self, value):
        new_index = value % len(self._pages)
        old_index = self._index
        self._index = new_index
        if old_index != new_index and self._is_visible:
            old_page = self.get_page(old_index)
            new_page = self.get_page(new_index)
            old_page.hide()
            new_page.show()
    
    def select_page(self, page_number):
        self.current_page_number = page_number

    @property
    def pages(self):
        return self._pages

    @property
    def total_pages(self):
        return len(self._pages)

    @property
    def current_page(self):
        return self._pages[self._index]

    @property
    def is_open(self):
        return self._is_visible

    def get_page(self, number):
        return self._pages[number % len(self._pages)]

    def append_page(self, page):
        if page not in self._pages:
            self._pages.append(page)
    
    def insert_page(self, page, index):
        if page not in self._pages:
            self._pages.insert(index, page)

    def open(self):
        self._is_visible = True
        self.current_page.show()

    def close(self):
        self._is_visible = False
        self.current_page.hide()    


