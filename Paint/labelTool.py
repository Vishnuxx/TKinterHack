import tkinter as T

def labelTool(parent , label="button" , command= None):
    btn = T.Label(text=label , borderwidth=0  , relief='solid')
    btn.bind("<Enter>", hover)
    btn.bind("<Leave>", leave)
    btn.bind("<Button-1>" , command)
    return btn


def hover( event):
    btn = event.widget
    print("sfd")
    btn.config(foreground="orange")

def leave( event):
    btn = event.widget
    print("sfd")
    btn.config(foreground='white')
   