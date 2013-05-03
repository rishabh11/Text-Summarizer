import wx
import summarize

class autosum(wx.Frame):
	""" Basic gui class whic calls summarize.py for all summarization related tasks."""

	sum=summarize.summarize()	
		
	box1=None
	box2=None
	box3=None
	
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'Text Summarizer',size=(600,600))
		panel=wx.Panel(self,-1)
		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        	font.SetPointSize(12)
		
		vbox = wx.BoxSizer(wx.VERTICAL)
		
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)		
		self.box1 = wx.TextCtrl(panel)
		label1 = wx.StaticText(panel,label="Title:")
		label1.SetFont(font)
		hbox1.Add(label1, flag=wx.RIGHT, border=8)
		hbox1.Add(self.box1,proportion=1)
		vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))
	
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		label2 = wx.StaticText(panel,label="Text:")
		label2.SetFont(font)
		hbox2.Add(label2)
		vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)
		vbox.Add((-1, 10))
	
		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		self.box2 = wx.TextCtrl(panel,style=wx.TE_MULTILINE)
		hbox3.Add(self.box2, proportion=1, flag=wx.EXPAND)
      		vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
		vbox.Add((-1, 25))

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		label3 = wx.StaticText(panel,label="Summary:")
		label3.SetFont(font)
		hbox4.Add(label3)
		vbox.Add(hbox4, flag=wx.LEFT | wx.TOP, border=10)
		vbox.Add((-1, 10))
	
		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		self.box3 = wx.TextCtrl(panel,style=wx.TE_MULTILINE)
		hbox5.Add(self.box3, proportion=1, flag=wx.EXPAND)
      		vbox.Add(hbox5, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
		vbox.Add((-1, 25))		
		
		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		button1=wx.Button(panel,label="Train",size=(90,30))     
		button2=wx.Button(panel,label="Summarize",size=(120,30))
		button3=wx.Button(panel,label="Clear",size=(90,30))
		hbox6.Add(button1)
		hbox6.Add(button2)
		hbox6.Add(button3,flag=wx.CENTRE|wx.BOTTOM, border=5)		
		vbox.Add(hbox6, flag=wx.ALIGN_CENTRE|wx.CENTRE, border=10)

		self.Bind(wx.EVT_BUTTON,self.train,button1)
		self.Bind(wx.EVT_BUTTON,self.summarize,button2)
		self.Bind(wx.EVT_BUTTON,self.clear,button3)
     		
		panel.SetSizer(vbox)
        
	def clear(self,event):
		self.box1.Clear()
		self.box2.Clear()
		self.box3.Clear()

	def train(self,event):
		self.sum.train(self.box1.GetValue(),self.box2.GetValue(),self.box3.GetValue())
	
	def summarize(self,event):
		self.box3.SetValue(self.sum.generate_summary(self.box1.GetValue(),self.box2.GetValue()))

	def closewindow(self,event):
        	self.Destroy()

if __name__=='__main__':
	app=wx.App()
	frame=autosum(parent=None,id=-1)
	frame.Show()
	app.MainLoop()
    
