import os.path, urllib, gtk, gobject
from . import treeview

# FUNCTIONS {{{1

def text_trim(value, length=50): #{{{2
    if len(value) <= length: return value
    return value[:length-3] + '...'

def pixbuf_from_file(filename, size=None): #{{{2
    if not size: return gtk.gdk.pixbuf_new_from_file(filename)
    return gtk.gdk.pixbuf_new_from_file_at_size(filename, *size)

def pixbuf_from_url(url, size=None): #{{{2
    filename = urllib.urlretrieve(url)[0]
    return pixbuf_from_file(filename, size)

def get_icon_list(filename): #{{{2
    icon_list = []
    for size in 16, 32, 48, 64, 128:
        icon_list.append(pixbuf_from_file(filename, (size, size)))
    return icon_list


# CLASSES {{{1

class Dialog(gtk.Dialog): #{{{2

    def __init__(self, **kwargs):
        super(Dialog, self).__init__(**kwargs)

    def run(self):
        self.show_all()
        r = super(Dialog, self).run()
        self.hide()
        return r



class AboutDialog(gtk.AboutDialog): #{{{2

    def __init__(self, name=None, authors=None, website=None, license=None, logo=None, **kwargs):
        super(AboutDialog, self).__init__(**kwargs)
        if name: self.set_name(name)
        if authors: self.set_authors(authors)
        if website: self.set_website(website)
        if license: self.set_license(license)
        if logo: self.set_logo(pixbuf_from_file(logo, (100, 100)))

    def run(self):
        super(AboutDialog, self).run()
        self.hide()



class ModalDialog(Dialog): #{{{2

    def __init__(self, **kwargs):
        kwargs['flags'] = gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT
        super(ModalDialog, self).__init__(**kwargs)



class ConfirmDialog(ModalDialog): #{{{2

    def __init__(self, prompt, **kwargs):
        super(ConfirmDialog, self).__init__(**kwargs)
        self.vbox.pack_start(gtk.Label(prompt))
        self.add_button(gtk.STOCK_NO, gtk.RESPONSE_NO)
        self.add_button(gtk.STOCK_YES, gtk.RESPONSE_YES)



class StandardDialog(ModalDialog): #{{{2

    def __init__(self, **kwargs):
        super(StandardDialog, self).__init__(**kwargs)
        self.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        self.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)



class ProgressDialog(ModalDialog): #{{{2

    def __init__(self, label, **kwargs):
        super(ProgressDialog, self).__init__(**kwargs)
        self.vbox.pack_start(gtk.Label(label))
        self.progressbar = gtk.ProgressBar()
        self.vbox.pack_start(self.progressbar)
        self.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        self.connect('destroy', self.on_dialog_destroy)

    def pulse(self):
        self.progressbar.pulse()

    def set_text(self, text):
        self.progressbar.set_text(text)

    def run(self, generator):
        self.timer = gobject.idle_add(generator.next)
        return super(ProgressDialog, self).run()

    def on_dialog_destroy(self, widget=None):
        gobject.source_remove(self.timer)
        self.destroy()



class DirectoryChooser(gtk.FileChooserDialog): #{{{2

    def __init__(self, **kwargs):
        super(DirectoryChooser, self).__init__(**kwargs)
        self.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
        if 'title' not in kwargs: self.set_title('Choose Directory')
        self.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        self.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)

    def run(self):
        r = super(DirectoryChooser, self).run()
        self.hide()
        if r != gtk.RESPONSE_OK: return
        return self.get_filename() or self.get_current_folder()
