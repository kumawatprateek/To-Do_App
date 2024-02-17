from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.metrics import dp
import datetime
from datetime import date
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivy.core.window import Window
from kivymd.uix.snackbar import Snackbar

Window.size=(350,600)


class TodoCard(CommonElevationBehavior,MDFloatLayout):
    title=StringProperty()
    description=StringProperty()

class ToDoApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("font/Main.kv"))
        screen_manager.add_widget(Builder.load_file("font/AddTodo.kv"))

        return screen_manager

    def on_start(self):

        today=date.today()
        weekday=date.weekday(today)
        days=['Monday','Tuesday','Wednesday','Friday','Saturday','Sunday']
        year=str(datetime.datetime.now().year)
        month=str(datetime.datetime.now().strftime("%b"))
        day=str(datetime.datetime.now().strftime("%d"))
        # screen_manager.get_screen("main").date.text=f"{days[weekday]},{day} {month} {year}"


    def on_complete(self,checkbox,value,description,bar):
        if value:
            description.text=f"[s]{description.text}[/s]"
            bar.md_bg_color=0,179/255,0,1
        else:
            remove=["[s]","[/s]"]
            for i in remove:
                description.text=description.text.replace(i,"")
                bar.md_bg_color=1,170/255,23/255,1

    def on_delete(self, card, description, bar):
        # Implement your delete logic here
        screen_manager.get_screen("main").todo_list.remove_widget(card)
        Snackbar(text="Task deleted", snackbar_x="10dp", snackbar_y="10dp", size_hint_y=.08,
                 size_hint_x=(Window.width-(dp(10)*2))/Window.width, bg_color=(1, 0, 0, 1),
                 font_size="18sp").open()


    def add_todo(self, title,description):
        if title != "" and description != "" and len(title)<21 and len(description)<61:
            # current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # created_task = f"{title}\t{current_datetime}"

            screen_manager.current="main"
            screen_manager.transition.direction="right"
            screen_manager.get_screen("main").todo_list.add_widget(TodoCard(title=title,description=description))
            screen_manager.get_screen("add_todo").description.text=""
            # current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # created_task = f"{current_datetime}\nTitle: {title}\nDescription: {description}"
            #
            # screen_manager.current = "main"
            # screen_manager.transition.direction = "right"
            # screen_manager.get_screen("main").todo_list.add_widget(TodoCard(title=title, description=created_task))
            # screen_manager.get_screen("add_todo").description.text = ""

        elif description=="" and title=="":
            Snackbar(text="Title & Description is missing",snackbar_x="10dp",snackbar_y="10dp",size_hint_y= .08,
                     size_hint_x=(Window.width-(dp(10)*2))/Window.width,bg_color=( 1, 170/255, 23/255,1),
                     font_size="18sp").open()
        elif title=="":
            Snackbar(text="Title is missing",snackbar_x="10dp",snackbar_y="10dp",size_hint_y= .08,
                     size_hint_x=(Window.width-(dp(10)*2))/Window.width,bg_color=( 1, 170/255, 23/255,1),
                     font_size="18sp").open()
        elif description=="":
            Snackbar(text="Description is missing",snackbar_x="10dp",snackbar_y="10dp",size_hint_y= .08,
                     size_hint_x=(Window.width-(dp(10)*2))/Window.width,bg_color=( 1, 170/255, 23/255,1),
                     font_size="18sp").open()
        elif len(description)>=61 and len(title)>=21:
            Snackbar(text="Length is Title <21 & Description <61",snackbar_x="10dp",snackbar_y="10dp",size_hint_y= .08,
                     size_hint_x=(Window.width-(dp(10)*2))/Window.width,bg_color=( 1, 170/255, 23/255,1),
                     font_size="18sp").open()
        elif len(title)>=21:
            Snackbar(text="Title length is <21",snackbar_x="10dp",snackbar_y="10dp",size_hint_y= .08,
                     size_hint_x=(Window.width-(dp(10)*2))/Window.width,bg_color=( 1, 170/255, 23/255,1),
                     font_size="18sp").open()
        elif len(description)>=61:
            Snackbar(text="Description length is <61",snackbar_x="10dp",snackbar_y="10dp",size_hint_y= .08,
                     size_hint_x=(Window.width-(dp(10)*2))/Window.width,bg_color=( 1, 170/255, 23/255,1),
                     font_size="18sp").open()


if __name__ == "__main__":
    ToDoApp().run()