class PageElements:
    def __init__(self, element):
        self.element = element

    def get_dimensions(self):
        class dimensions:
            x = self.element.location['x']
            y = self.element.location['y']
            width = self.element.size['width']
            height = self.element.size['height']
        return dimensions
