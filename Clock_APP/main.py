from time import strftime
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class CLOCKApp(App):
    App.title = 'GUI Clock in Kivy'
    sw_started,sw_seconds,prompt = False,0,'Start'


    def on_start(self):
        Clock.schedule_interval(self.sw_count, 0)
    
    def sw(self):
        self.sw_started = bool(1-int(self.sw_started))
        self.prompt = 'Stop' if self.sw_started else 'Start'
        self.root.ids.sw.text = self.prompt

    def reset(self):
        self.sw_seconds = 0
        if self.sw_started:
            self.root.ids.sw.text = 'Start'
            self.sw_started = False  

    def sw_count(self, sleep):
        if self.sw_started:
            self.sw_seconds += sleep
        mins,secs = self.sw_seconds//60,self.sw_seconds%60
        self.root.ids.stopwatch.text = (str(int(mins))+':'+str(int(secs))+'.[size=45]'+str(int(secs* 100 % 100))+'[/size]')
        self.root.ids.clock_disp.text = strftime('[b]%H:%M[/b][size=45]:%S[/size]')
    
    

LabelBase.register(
    name='Digital',
    fn_regular= 'Let_s_go_Digital_Regular.ttf',
    fn_bold= 'Let_s_go_Digital_Regular.ttf'
)
Window.clearcolor = get_color_from_hex('#39107D')
CLOCKApp().run()

            # '%02d:%02d.[size=45]%02d[/size]'%
            # (int(mins), int(secs),
            #  int(secs* 100 % 100))