import gtk

def pixbuf_column(name, pos, data_func):
    cr = gtk.CellRendererPixbuf()
    column = gtk.TreeViewColumn(name, cr)
    column.set_sort_column_id(pos)
    column.set_cell_data_func(cr, data_func)
    return column

def text_column(name, pos):
    column = gtk.TreeViewColumn(name, gtk.CellRendererText(), text=pos)
    column.set_sort_column_id(pos)
    column.set_resizable(True)
    return column

def markup_column(name, pos, data_func):
    cr = gtk.CellRendererText()
    column = gtk.TreeViewColumn(name, cr)
    column.set_sort_column_id(pos)
    column.set_cell_data_func(cr, data_func)
    column.set_resizable(True)
    return column

def toggle_column(name, pos, callback):
    cr = gtk.CellRendererToggle()
    cr.connect('toggled', callback)
    column = gtk.TreeViewColumn(name, cr, active=pos)
    column.set_sort_column_id(pos)
    return column
