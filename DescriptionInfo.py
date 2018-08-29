class DescriptionInfo(object):

    def __init__(self):
        self.Id = str()
        self.Main = str()
        self.Description = str()
        self.Icon = str()

    def set_description_info(self, id_, main_, desc, icon):
        self.Id = id_
        self.Description = desc
        self.Main = main_
        self.Icon = icon
