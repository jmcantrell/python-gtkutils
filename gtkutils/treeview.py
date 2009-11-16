import gtk

def column_pixbuf(name, pos, data_func): #{{{1
    cr = gtk.CellRendererPixbuf()
    column = gtk.TreeViewColumn(name, cr)
    column.set_sort_column_id(pos)
    column.set_cell_data_func(cr, data_func)
    return column

def column_text(name, pos): #{{{1
    column = gtk.TreeViewColumn(name, gtk.CellRendererText(), text=pos)
    column.set_sort_column_id(pos)
    column.set_resizable(True)
    return column

def column_markup(name, pos, data_func): #{{{1
    cr = gtk.CellRendererText()
    column = gtk.TreeViewColumn(name, cr)
    column.set_sort_column_id(pos)
    column.set_cell_data_func(cr, data_func)
    column.set_resizable(True)
    return column

def column_toggle(name, pos, callback): #{{{1
    cr = gtk.CellRendererToggle()
    cr.connect('toggled', callback)
    column = gtk.TreeViewColumn(name, cr, active=pos)
    column.set_sort_column_id(pos)
    return column
