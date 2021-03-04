from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
import pickle
import numpy as np
import warnings 
import re
warnings.simplefilter("ignore")
# from kivy.uix.list import MDList,ThreeLineListItem
class Main(Screen):
    pass

class Form(Screen):
    
    # for check boxes
    def checkbox_click_sex(self,instance,value,giv):
        self.sex=int(giv)
        pass
    def checkbox_click_fbs(self,instance,value,giv):
        self.fbs=int(giv)
        pass
    def checkbox_click_exong(self,instance,value,giv):
        self.exong=int(giv)
        pass
    def checkbox_click_slope(self,instance,value,giv):
        self.slope=int(giv)
        pass
    def checkbox_click_thal(self,instance,value,giv):
        self.thal=int(giv)
        pass


    # for sliders
    def slide_it_age(self,*args):
        self.slide_age.text=str(int(args[1]))
        self.age=(int(args[1]))        
    def slide_it_trp(self,*args):
        self.slide_trp.text=str(int(args[1]))
        self.trp=(int(args[1]))
    def slide_it_cholestrol(self,*args):
        self.slide_cholestrol.text=str(int(args[1]))
        self.cholestrol=(int(args[1]))
    def slide_it_ecg(self,*args):
        self.slide_ecg.text=str(int(args[1]))
        self.ecg=(int(args[1]))
    def slide_it_thalaz(self,*args):
        self.slide_thalaz.text=str(int(args[1]))
        self.thalaz=(int(args[1]))
    def slide_it_oldpeak(self,*args):
        self.slide_oldpeak.text=str(int(args[1]))
        self.oldpeak=(int(args[1]))
    def slide_it_cp(self,*args):
        self.slide_cheast.text=str(int(args[1]))
        self.cp=(int(args[1]))
    def slide_it_ca(self,*args):
        self.slide_ca.text=str(int(args[1]))
        self.ca=(int(args[1]))
    
    def calc(self):
        nn=ObjectProperty(None)
        op=ObjectProperty(None)
        
        try:
            l=[]
            if(re.match(r'^[a-zA-Z ]+$',self.nn.text)):
                l.extend([self.age,self.sex,self.cp,self.trp,self.cholestrol,self.fbs,self.ecg,self.thalaz,self.exong,self.op.text,self.slope])
                final_values=[np.array(l)]
                print(final_values)
                model = pickle.load(open('model.pkl', 'rb'))
                prediction=model.predict(final_values)
                print(prediction)
                Result.na=self.nn.text
                if prediction[0]==0:
                    Result.fin='You are not Diagnosed'
                else:
                    Result.fin='You are Diagnosed'

                sm.current='result'
            else:
                raise Exception("Name not corret")
        except:
            print("give all values")
            invalidLogin()
    pass


class Result(Screen):
    fin=""
    na=""
    def on_enter(self, *args):
        self.ini.text="Hi "+self.na
        self.rer.text = "Result be: " + self.fin
    pass
class Manager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please Fill all the columns in form'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


kv=Builder.load_file("pr.kv")
sm=Manager()
screen=[Main(name="main"),Form(name="form"),Result(name="result")]
for ss in screen:
    sm.add_widget(ss)
sm.current='main'
class Predection(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return sm      

if __name__ == '__main__':
    Predection().run()