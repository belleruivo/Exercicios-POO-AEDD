class ClubeMixin:
    
    def __init__(self, clube, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clube = clube
    
    def get_clube(self):
        return self.clube
