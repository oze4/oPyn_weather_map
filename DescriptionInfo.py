class DescriptionInfo(object):
    Id = str()
    Main = str()
    Description = str()
    Icon = str()

    def __init__(self, id_, main_, description, icon):
        self.Id = id_
        self.Main = main_
        self.Description = description
        self.Icon = icon
