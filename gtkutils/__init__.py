import os.path, urllib
import gtk, gobject

from . import treeview

def text_trim(value, length=50):
    if len(value) <= length: return value
    return value[:length-3] + '...'

def pixbuf_from_file(filename, size=None):
    if not size: return gtk.gdk.pixbuf_new_from_file(filename)
    return gtk.gdk.pixbuf_new_from_file_at_size(filename, *size)

def pixbuf_from_url(url, size=None):
    filename = urllib.urlretrieve(url)[0]
    return pixbuf_from_file(filename, size)

def get_icon_list(filename):
    icon_list = []
    for size in 16, 32, 48, 64, 128:
        icon_list.append(pixbuf_from_file(filename, (size, size)))
    return icon_list


class Dialog(gtk.Dialog):

    def __init__(self, *args, **kwargs):
        gtk.Dialog.__init__(self, *args, **kwargs)

    def run(self):
        self.show_all()
        r = gtk.Dialog.run(self)
        self.hide()
        return r



class ModalDialog(Dialog):

    def __init__(self, *args, **kwargs):
        kwargs['flags'] = gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT
        Dialog.__init__(self, *args, **kwargs)



class ConfirmDialog(ModalDialog):

    def __init__(self, prompt, *args, **kwargs):
        ModalDialog.__init__(self, *args, **kwargs)
        self.vbox.pack_start(gtk.Label(prompt))
        self.add_button(gtk.STOCK_NO, gtk.RESPONSE_NO)
        self.add_button(gtk.STOCK_YES, gtk.RESPONSE_YES)



class StandardDialog(ModalDialog):

    def __init__(self, *args, **kwargs):
        ModalDialog.__init__(self, *args, **kwargs)
        self.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        self.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)



class ProgressDialog(ModalDialog):

    def __init__(self, label, *args, **kwargs):
        ModalDialog.__init__(self, *args, **kwargs)
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
        return ModalDialog.run(self)

    def on_dialog_destroy(self, widget=None):
        gobject.source_remove(self.timer)
        self.destroy()



class DirectoryChooser(gtk.FileChooserDialog):

    def __init__(self, *args, **kwargs):
        gtk.FileChooserDialog.__init__(self, *args, **kwargs)
        self.set_action(gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER)
        if 'title' not in kwargs: self.set_title('Choose Directory')
        self.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        self.add_button(gtk.STOCK_OK, gtk.RESPONSE_OK)

    def run(self):
        r = gtk.FileChooserDialog.run(self)
        self.hide()
        if r != gtk.RESPONSE_OK: return
        return self.get_filename() or self.get_current_folder()
