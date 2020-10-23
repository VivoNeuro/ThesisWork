from tkinter import *
import os
import time

version = "#Pyt_TonRew.t0.20200918.0"

parNam = ["Frequency(Hz): reward:",
          "_________punishment:",
          "_________neutral:","Tone length(ms):","Gap length(ms):","Stimulus length(ms):",
          "Time inter trial(s):","Diffusion factor(s):","Number of trail:"]
initVal = [400,200,100,1000,500,250,
            10,5,2]

class Table:
    def __init__(self,master):
        self.parFrame = Frame(master,bg='black',bd=5,relief="ridge",width=200,height=200)
        self.parFrame.grid(column=0,row=0,sticky="NW")

        self.disFrame = Frame(master,bg='yellow',bd=5,relief="ridge",width=200,height=200)
        self.disFrame.grid(column=1,row=0,sticky="NW")

class Diary:
    dirname = os.path.dirname(os.path.abspath(__file__))
    current_time = time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime())
    dataFile = open(dirname+'/diary/'+current_time+'.txt','w')
    dataFile.write(version[1:]+'\n')
    def write_ard_version(self,vers_ard):
        self.dataFile.write(vers_ard+'\n\n')
    def title(self,title_value):
        self.dataFile.write(title_value+'\n\n')
    def close_diary(self):
        self.dataFile.close()
        time.sleep(3)
"""
def readOrder():
    order = struct.unpack('<B',connector.ser.read(1))[0]
    return order

def writeOrder(n):
    connector.ser.write(struct.pack('<B',int(n)))
    if readOrder()!=int(n):
        print('Incorrect order-transfer!')

def readValue():
    return struct.unpack('<H',connector.ser.read(2))[0]
    
def writeValue(n):
    connector.ser.write(struct.pack('<H',int(n)))
    if readValue()!=int(n):
        print('Incorrect value-transfer!')
"""
def update_parameters(event,i):
    if parVal[i].value!=parVal[i].spn.get() and parVal[i].spn.get().isnumeric():
        parVal[i].value=parVal[i].spn.get()
        writeOrder(i+10)
        writeValue(parVal[i].value)
        print(parNam[i],parVal[i].spn.get())
        diary.dataFile.write(parNam[i]+parVal[i].spn.get()+'\n')
        parHist.lsb.insert(0,str(parNam[i])+' '+parVal[i].spn.get())
    else:
        parVal[i].spn['value'] = parVal[i].value
    if parHist.lsb.size()>30:
        parHist.lsb.delete(END)

class Parameters:
    def __init__(self,master,k):
        frame = Frame(master,bg='black',bd=0)
        frame.pack(fill=X)

        self.lbl = Label(frame,text=parNam[k],font=('Times New Roman Greek',10),anchor='w',width=20,bg='#9CB99C')
        self.lbl.grid(column=0,row=0)

        self.spn = Spinbox(frame,width=5,bd=2,justify='right',disabledbackground='black')
        self.spn.bind("<FocusOut>",lambda event, a=k :update_parameters(event,a))
        self.spn.bind("<Return>",lambda event, a=k :update_parameters(event,a))
        self.spn.grid(column=1,row=0)
        self.spn['value'] = initVal[k]

        self.value = str(initVal[k])

        #writeOrder(k+10)
        #writeValue(initVal[k])

class History:
    def __init__(self,master):
        lbf = LabelFrame(master,height=60,text="History:",font=('Times New Roman Greek',10),bg='#9CB99C')
        lbf.pack(fill=X,expand=YES)

        self.srb = Scrollbar(lbf,bg="blue",bd=2,width=14)
        self.srb.pack(side=RIGHT,fill=Y)

        self.lsb = Listbox(lbf,yscrollcommand=self.srb.set,bg='#9CB99C',width=30)
        self.lsb.insert(END,"Ready")
        self.lsb.pack(side=LEFT,fill=BOTH)
        
        self.srb.config(command=self.lsb.yview)

class Buttons:
    def start_trials(self):
        print("Start trials!")
        writeOrder(2)
        writeValue(0)

    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()

        self.start = Button(self.frame,text="Start",command=self.start_trials)
        #self.start.pack(side=LEFT)
        self.start.grid(column=0,row=0)

        self.stop = Button(self.frame,text="Stop")
        self.start.grid(column=1,row=0)

        self.reStart = Button(self.frame,text="Restart")
        self.start.grid(column=2,row=0)

class Modifiers:
    def __init__(self,master):
        def sel():
            print("Method: "+str(self.mVar.get()))
        
        def sel2():
            print("Stimulus: ")
            if self.S1var==0:
                parVal[0].spn.config(state='DISABLED')
        
        frame = Frame(master,width=400,height=200)
        frame.pack()

        self.meth = LabelFrame(frame,height=60,width=200,text="Method:",font=('Times New Roman Greek',10),bg='#9CB99C')
        self.meth.pack(side=LEFT,fill=Y)

        self.mVar = IntVar()
        self.R1 = Radiobutton(self.meth,text="training",variable=self.mVar,value=1,bg='#9CB99C',command=sel)
        self.R1.grid(column=0,row=0,sticky="NW")
        self.R2 = Radiobutton(self.meth,text="random",variable=self.mVar,value=2,bg='#9CB99C',command=sel)
        self.R2.grid(column=0,row=1,sticky="NW")

        self.stim = LabelFrame(frame,height=60,width=200,text="Stimulus:",font=('Times New Roman Greek',10),bg='#9CB99C')
        self.stim.pack(side=LEFT,fill=Y)

        self.S1var = IntVar()
        self.S2var = IntVar()
        self.S3var = IntVar()
        self.C1 = Checkbutton(self.stim,text="reward",variable=self.S1var,bg='#9CB99C',command=sel2)
        self.C1.grid(column=0,row=0,sticky="NW")
        self.C2 = Checkbutton(self.stim,text="punishment",variable=self.S2var,bg='#9CB99C')
        self.C2.grid(column=0,row=1,sticky="NW")
        self.C3 = Checkbutton(self.stim,text="neutral",variable=self.S3var,bg='#9CB99C')
        self.C3.grid(column=0,row=2,sticky="NW")

class Version_ID:
    def __init__(self,mester,id):
        self.lbl = Label(mester,text=id,font=('Times New Roman Greek',8),bg='#9CB99C')
        self.lbl.pack(fill=X)

window = Tk()
window.geometry('640x410+20+20')
window.minsize(200,200)
window.title('Tone-Reward trials')

kernel = Table(window)

parVal =[]
for i in range(len(parNam)):
    parVal.append(Parameters(kernel.parFrame,i))

parHist = History(kernel.parFrame)

Modifiers(kernel.disFrame)

Buttons(kernel.disFrame)

Version_ID(kernel.parFrame,version[1:])
Ard_vers = "#Ard_ToneRew.2.20200918.0"
Version_ID(kernel.disFrame,Ard_vers[1:])

window.mainloop()