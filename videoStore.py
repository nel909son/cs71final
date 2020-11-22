import os
import time
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from videoDb import Database




root = tk.Tk()
path = "C:/Users/nelso/Desktop/python/71final/"

db = Database(path+'Movie.db')

root.title = ("Nels Retro VHS Store")

root.geometry("800x650")
root['background']='#49A19A'
labelTitle = Label(root, text = "Nels Retro VHS Store", font=("Helvetica",16))

#treev = ttk.Treeview(root,selectmode ='browse' )

#treev.pack(side = 'bottom', fill='x')



#Labels that show what the entry boxes are for
labelMovieID = Label(root, text = "Film ID")
labelMovieName = Label(root, text = "Film Title")
labelMovieGenre = Label(root, text = "Genre")
labelMovieYear = Label(root, text = "Release Year")

#cooresponding entry boxes
entryMovieID = Entry(root)
entryMovieName = Entry(root)
entryMovieGenre = Entry(root)
entryMovieYear = Entry(root)



#the functions



#delete a movie from the database
#should probably add a confirmation
def deleteMovie():
    if entryMovieID.get() =='':
        mb.showinfo('Information', "select movie to delete")
        return
    msgBox = mb.askquestion('Delete Record', 'Are you sure!! what if you miss it when its gone!', icon='warning')
    if msgBox == 'yes':
        db.remove(entryMovieID.get())
        clearField()
        loadFilmData()

#clear the fieldsss. they will come.
def clearField():
    entryMovieID.delete(0,END)
    entryMovieName.delete(0,END)
    entryMovieGenre.delete(0,END)
    entryMovieYear.delete(0,END)

def validate_entry():
    if entryMovieName.get() == "":
        mb.showinfo('Information', "Please enter movie name")
        entryMovieName.focus_set()
        return
    if entryMovieID.get() == "":
        mb.showinfo('Information', "Please enter movie ID")
        entryMovieID.focus_set()
        return
    if entryMovieGenre.get() == "":
        mb.showinfo('Information', "Please enter movie genre")
        entryMovieGenre.focus_set()
        return
    if entryMovieYear.get() == "":
        mb.showinfo('Information', "Please enter movie year")
        entryMovieYear.focus_set()
        return
    else:
        return

#show all the movies in the database
def showAll():
    return

#exit the simulation..err program

def exit():
    msgBox = mb.askquestion('Exiting...', 'ARE YOU SUUUURE!?', icon='warning')
    if msgBox == 'yes':
        root.destroy()

#update a films info
def updateMovie():
    validate_entry()

    db.update(entryMovieID.get(),entryMovieName.get(),entryMovieGenre.get(),entryMovieYear.get())
    clearField()
    loadFilmData()
    
#kvs5N3rpHq3

#loading film data on program open/update. REFRESSHHHHHing
def loadFilmData():
    for row in treeviewMovie.get_children():
        treeviewMovie.delete(row)
    for row in db.fetch():
        movieID = row[1]
        movieName = row[2]
        movieGenre = row[3]
        movieYear = row[4]
        treeviewMovie.insert("",'end',text=movieID,values=(movieID,movieName,movieGenre,movieYear))



#add a movie to the database
def addMovie():
    validate_entry()
    db.insert(entryMovieID.get(),entryMovieName.get(),entryMovieGenre.get(),entryMovieYear.get())

    clearField()
    loadFilmData()
    return

#for stuff to show in treeview
def show_selected_movie(event):
    clearField()
    for clicked_on in treeviewMovie.selection():
        item = treeviewMovie.item(clicked_on)
        global movie_id
        movie_id, movie_name,movie_genre,movie_year = item["values"][0:6]
        entryMovieID.insert(0,movie_id)
        entryMovieName.insert(0,movie_name)
        entryMovieGenre.insert(0,movie_genre)
        entryMovieYear.insert(0,movie_year)

    return movie_id

#the BUTTONS give em somethin to click
buttonAdd = Button(root, text = "Add Movie", command = addMovie )
buttonUpdate = Button(root, text = "Update a Film", command = updateMovie)
buttonDelete = Button(root, text = "Delete a Film", command = deleteMovie)
buttonClear = Button(root, text = "Clear Fields", command = clearField)
buttonShowAll = Button(root, text = "Show all Films", command = showAll)
buttonExit = Button(root, text = "Exit", command = exit )

#treeview widget

columns = ("#1","#2","#3","#4")

treeviewMovie = ttk.Treeview(root, show="headings", height ="5",column=columns)

treeviewMovie.heading('#1', text='Moive ID', anchor='center')
treeviewMovie.column('#1', width=60, anchor='center', stretch = False)

treeviewMovie.heading('#2', text='Movie Name', anchor='center')
treeviewMovie.column('#2', width=10, anchor='center',stretch = True)

treeviewMovie.heading('#3', text='Moive Genre', anchor='center')
treeviewMovie.column('#3', width=10, anchor='center',stretch = True)

treeviewMovie.heading('#4', text='Release Year', anchor='center')
treeviewMovie.column('#4', width=10, anchor='center',stretch = True)

vertical_scroll_bar = ttk.Scrollbar(root, orient=VERTICAL, command= treeviewMovie.yview)

horizontal_scroll_bar = ttk.Scrollbar(root, orient=HORIZONTAL, command= treeviewMovie.xview)

#place the labels we made earlier
labelTitle.place(x=280, y=5, height = 27, width=300)
labelMovieID.place(x=175, y = 40, height=23, width=100)
labelMovieName.place(x=175, y = 70, height=23,width=100)
labelMovieGenre.place(x=175, y=100, height=23, width = 100)
labelMovieYear.place(x=175, y =130, height=23, width= 100)

#place entry boxes
entryMovieID.place(x=400, y = 40, height = 23, width=100)
entryMovieName.place(x=400, y = 70, height = 23, width=100)
entryMovieGenre.place(x=400, y = 100, height = 23, width=100)
entryMovieYear.place(x=400, y = 130, height = 23, width=100)

#place BUTTONS
buttonAdd.place(x=300, y = 250, height = 21, width = 187)
buttonUpdate.place(x = 50, y = 250, height = 21, width = 187)
buttonClear.place(x = 550 , y = 250, height = 21, width = 187)
buttonDelete.place(x = 50, y=350, height= 21, width = 187)
buttonShowAll.place(x = 300, y = 350, height= 21, width = 187)
buttonExit.place(x = 550, y = 350, height = 21, width = 187)

#place scrollbars
vertical_scroll_bar.place(x=40+640 +1 , y = 390, height=180 + 20)
treeviewMovie.configure(yscroll=vertical_scroll_bar.set)
horizontal_scroll_bar.place(x=40, y=390+200+1, width=620+20)
treeviewMovie.configure(xscroll=horizontal_scroll_bar.set)

treeviewMovie.bind("<<TreeviewSelect>>", show_selected_movie)
treeviewMovie.place(x=40, y=390, height= 200, width= 640)
#TODO!
#treeviewDisplay.place()

root.mainloop()

