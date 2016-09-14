from flexx import event, app, ui


import button
import splitter

modules = [button, splitter]


class Tester(ui.Widget):
    
    def init(self):
        
        with ui.VBox() as self.box:
            
            with ui.HBox():
                self.skip = ui.Button(text='Skip this test', flex=1)
                self.fail = ui.Button(text='Mark this test as failed', flex=1)
            self.description = ui.Label(wrap=True)
            ui.Widget(style='background:#f88; min-height:10px;')
            self.cur = ui.Widget(flex=1)
    
    @event.prop
    def cur(self, v):
        return v
    
    @event.connect('skip.mouse_click', 'fail.mouse_down', 'cur.ok')
    def next(self, *event):
        self.cur.parent = None
        self.cur.dispose()
        
        if not modules:
            self.cur = ui.Label(parent=self.box, flex=1, text='All done!')
        else:
            m = modules.pop(0)
            self.description.text = m.__doc__
            Cls = type('Test_' + m.__name__, [m.Test], {})
            self.cur = Cls(parent=self.box, flex=1)


if __name__ == '__main__':
    m = app.launch(Tester)
    app.run()
