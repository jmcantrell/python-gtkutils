import gtk

# CLASSES {{{1

class UI(object): #{{{2

    def __init__(self, ui):
        self.ui = gtk.Builder()
        self.ui.add_from_file(ui)

    def load_widgets(self, widgets):
        vars(self).update(dict((w, self.ui.get_object(w)) for w in widgets))



class Dialog(UI): #{{{2

    def __init__(self, ui='dialogs', dialog='dialog'):
        super(Dialog, self).__init__(ui)
        self.load_widgets([dialog])
        self.dialog = getattr(self, dialog)

    def run(self):
        self.dialog.show()
        r = self.dialog.run()
        self.dialog.hide()
        return r



class ConfirmDialog(Dialog): #{{{2

    def __init__(self, prompt, **kwargs):
        super(ConfirmDialog, self).__init__(**kwargs)
        self.load_widgets(['prompt'])
        self.prompt.set_text(prompt)



class ProgressDialog(Dialog): #{{{2

    def __init__(self, **kwargs):
        super(ProgressDialog, self).__init__(**kwargs)
        self.load_widgets(['label', 'progressbar'])
        self.ui.connect_signals(self)

    def pulse(self):
        self.progressbar.pulse()

    def set_text(self, text):
        self.progressbar.set_text(text)

    def run(self, generator):
        self.dialog.show()
        self.timer = gobject.idle_add(generator.next)

    def on_dialog_destroy(self, widget=None):
        gobject.source_remove(self.timer)
        self.dialog.hide()
