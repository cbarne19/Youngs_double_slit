#Double_slit_experiment 
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox 
import matplotlib

res = 0.001
h= 0.01
a0 = '17.4' #Screen_dstance 
an = '584'#wavelength 
bn = "9.6e-4" #slitseperation 
nm = 1e-9 

a0=[a0]
an=[an]
bn=[bn]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

def func(a0,an,bn):
    rect= matplotlib.patches.Rectangle((-0.06,1), 0.12, h, 
            color = (0,0,0,1))    
    ax.add_patch(rect) 
    x = [] 
    nm = 1e-9
    for i in range(-5,6):
        x.append(i*((eval(a0)*eval(an)*nm)/eval(bn)))     
    diff = abs(x[len(x)-1]-x[len(x)-2])
    n = int((diff/2)/res) 
    bdiff = abs(x[0]-x[len(x)-1])
    bn = int((bdiff/2)/(res))
    for i in range(len(x)):
        rect= matplotlib.patches.Rectangle((x[i],1), res, h, 
            color = (1-(1*abs((i)/bn)),0,0,1))    
        ax.add_patch(rect) 
        for k in range(-n,n):
            rect= matplotlib.patches.Rectangle((x[i]+res*k,1), res, h, 
                color = (1-(1*abs((k)/n)),0,0,1))    
            ax.add_patch(rect) 

func(a0[0],an[0],bn[0])
ax.set_aspect('equal') 
fig.subplots_adjust(bottom=0.35)
ax.relim()
ax.set_title('Youngs Double Slit')
ax.set_facecolor((0,0,0,1))
ax.autoscale_view()

def submit(expression):
    an.append(expression)
    func(a0[len(a0)-1],expression,bn[len(bn)-1])
    ax.relim
    
def submit2(expression):
    bn.append(expression)
    func(a0[len(a0)-1],an[len(an)-1],expression)
    ax.relim

def submit3(expression):
    a0.append(expression)
    func(expression,an[len(an)-1],bn[len(bn)-1])
    ax.relim
    
axbox3 = fig.add_axes([0.1, 0.4, 0.2, 0.055],xlabel = 'D (m)')
text_box3 = TextBox(axbox3, "")
text_box3.on_submit(submit3)
text_box3.set_val('17.4') 

axbox = fig.add_axes([0.4, 0.4, 0.2, 0.055],xlabel = '$\lambda$ (nm)')
text_box = TextBox(axbox, "")
text_box.on_submit(submit)
text_box.set_val('584')  

axbox2 = fig.add_axes([0.7, 0.4, 0.2, 0.055],xlabel = 'd (m)')
text_box2 = TextBox(axbox2, "")
text_box2.on_submit(submit2)
text_box2.set_val("9.6e-4")  