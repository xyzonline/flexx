"""
This app should show 4 buttons named 'A', 'B', 'C' and 'OK'.
Click on the button that says 'OK'.
"""

from flexx import event, ui

class Test(ui.Widget):
    
    def init(self):
        self.b1 = ui.Button(text='A')
        self.b2 = ui.Button(text='B')
        self.b3 = ui.Button(text='OK')
        self.b4 = ui.Button(text='C')
    
    @event.connect('b3.mouse_click')
    def test_ok(self, *events):
        print('button test ok')
        self.emit('ok')
