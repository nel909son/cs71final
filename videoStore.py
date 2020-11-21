import os
import time
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk

path = "./"
db = Database(path+"database.db")
root = tk.Tk()

root.title = ("Nels Retro VHS Store")

root.geometry("800x650")
root['background']='#49A19A'
labelTitle = Label(root, text = "Nels Retro VHS Store", font=("Helvetica",16))

treev = ttk.Treeview(root,selectmode ='browse' )

treev.pack(side = 'bottom', fill='x')



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
    return

#clear the fieldsss. they will come.
def clearField():
    return

#show all the movies in the database
def showAll():
    return

#exit the simulation..err program

def exit():
    return

#update a films info
def updateMovie():
    return

#loading film data
def loadFilmData():
    return


#add a movie to the database
def addMovie():
    return


#the BUTTONS give em somethin to click
buttonAdd = Button(root, text = "Add Movie", command = addMovie )
buttonUpdate = Button(root, text = "Update a Film", command = updateMovie)
buttonDelete = Button(root, text = "Delete a Film", command = deleteMovie)
buttonClear = Button(root, text = "Clear Fields", command = clearField)
buttonShowAll = Button(root, text = "Show all Films", command = showAll)
buttonExit = Button(root, text = "Exit", command = exit )

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


#TODO!
#treeviewDisplay.place()

root.mainloop()

#columns = ("1","2","3","4","5","6")
