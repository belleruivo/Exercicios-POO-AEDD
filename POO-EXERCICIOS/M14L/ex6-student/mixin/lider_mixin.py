class LiderMixin:
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.lider = True
    
    def is_lider(self):
        return self.lider
