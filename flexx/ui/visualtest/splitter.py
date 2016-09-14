"""
This app should show 3 widgets separated by two splitters (one
horizontal and one vertical). Move both splitters to < 25% to mark this
test a success.
"""

from flexx import event, ui

class Test(ui.Widget):
    
    def init(self):
        with ui.SplitPanel(orientation='vertical'):
            ui.Widget(style='background:#f77')
            with ui.SplitPanel(orientation='horizontal'):
                ui.Widget(style='background:#7f7')
                ui.Widget(style='background:#77f')
    
    @event.connect('children**.value')
    def test_ok(self, *events):
        print('found', ev.new_value)
        # self.emit('ok')
