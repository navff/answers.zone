class PageView(object):

    def __init__(self, objects, current_page=1, total_pages=1, total_objects_count=0):
        self.objects = objects
        self.current_page = current_page
        self.total_pages = total_pages
        self.total_objects_count = total_objects_count

