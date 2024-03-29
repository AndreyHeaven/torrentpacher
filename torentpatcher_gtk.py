#! /usr/bin/python
# -*- coding: utf-8 -*-

# To change this template, choose Tools | Templates
# and open the template in the editor.
import pygtk
pygtk.require('2.0')
import gtk
import ini
import tp_config;
from inifile import INIFile;

__author__="araygorodskiy"
__date__ ="$16.02.2009 12:56:01$"

# function to track the motion of the cursor while dragging
def motion_cb(wid, context, x, y, time):
   print "motion"
   context.drag_status(gtk.gdk.ACTION_COPY, time)
   return True

# function to print out the mime type of the drop item
def drop_cb(wid, context, x, y, time):
   l.set_text('\n'.join([str(t) for t in context.targets]))
   context.finish(True, False, time)
   return True

# Create a GTK window and Label, and hook up
# drag n drop signal handlers to the window
w = gtk.Window()
w.set_size_request(200, 150)
w.drag_dest_set(0, [], 0)
w.connect('drag_motion', motion_cb)
w.connect('drag_drop', drop_cb)
w.connect('destroy', lambda w: gtk.main_quit())
l = gtk.Label();
c = gtk.combo_box_new_text();
c.set_title("Города")
w.add(c)
w.add(l)
ini = INIFile();
for i in ini.cites.values():
    c.append_text(i.name);
w.show_all()

# Start the program
if __name__ == "__main__":
    items = tp_config.get_config()
    gtk.main()
