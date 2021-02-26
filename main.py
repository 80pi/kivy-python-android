from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

class Main(Screen):
    pass

class Form(Screen):

    # for check boxes
    def checkbox_click_sex(self,instance,value):
        pass
    def checkbox_click_fbs(self,instance,value):
        pass
    def checkbox_click_exong(self,instance,value):
        pass
    def checkbox_click_slope(self,instance,value):
        pass

    # for sliders
    def slide_it_age(self,*args):
        self.slide_age.text=str(int(args[1]))
    def slide_it_trp(self,*args):
        self.slide_trp.text=str(int(args[1]))
    def slide_it_cholestrol(self,*args):
        self.slide_cholestrol.text=str(int(args[1]))
    def slide_it_ecg(self,*args):
        self.slide_ecg.text=str(int(args[1]))
    def slide_it_thalaz(self,*args):
        self.slide_thalaz.text=str(int(args[1]))
    def slide_it_oldpeak(self,*args):
        self.slide_oldpeak.text=str(int(args[1]))
    pass
class Result(Screen):
    pass
class Manager(ScreenManager):
    pass
kv=Builder.load_file("pr.kv")
class Predection(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return kv      

if __name__ == '__main__':
    Predection().run()