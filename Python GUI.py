import wx

class Frame(wx.Frame):
    #added title parameter
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(300,200))
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Exit", size=(100,40), pos=(100,30))
        button.Bind(wx.EVT_BUTTON, self.exit)
        #Create menu bar
        menuBar = wx.MenuBar()
        #Create the menus
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        self.SetMenuBar(menuBar)
        # Add fileMenu and editMenu to menuBar
        menuBar.Append(fileMenu, "File")
        menuBar.Append(editMenu, "Edit")
        #Add items to FileMenu
        fileMenu.Append(wx.NewId(), "New File", "Create a new file")
        fileMenu.Append(wx.NewId(), "Open", "Open an existing file")
        exitItem = fileMenu.Append(wx.NewId(), "Exit", "Exit the program")
        #Bind exit menu item to exit function
        self.Bind(wx.EVT_MENU, self.exit, exitItem)
        
        #Create Status Bar
        self.CreateStatusBar()
    

    def exit(self, event):
        self.Destroy()


app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()

