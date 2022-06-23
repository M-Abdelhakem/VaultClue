from kivy.app import App
from kivymd.app import MDApp
# from kivy.graphics import Color, Line
# from kivy.graphics.texture import Texture
# from kivy.properties import ObjectProperty, ListProperty
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.relativelayout import RelativeLayout
from random import sample, shuffle
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup
from time import sleep
# from kivy.base import EventLoop
Window.clearcolor = (10/255, 45/255, 80/255, 1)
# EventLoop.window.clear_color = (1, 0, 0, 1)
Window.size = (360, 780)


class Popup1Box(Popup):
    def func(self):
        NumBad.clear()


class Popup2Box(Popup):
    def func(self):
        NumBad.clear(self)


class NumBad(Screen):
    ###############################################################################################
    def number1_pressed(self):
        self.ids.one.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.one.font_size += 10
    def number1_released(self):
        self.ids.one.color = (183/255, 177/255, 210/255)
        self.ids.one.font_size -= 10

    def number2_pressed(self):
        self.ids.two.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.two.font_size += 10
    def number2_released(self):
        self.ids.two.color = (183/255, 177/255, 210/255)
        self.ids.two.font_size -= 10

    def number3_pressed(self):
        self.ids.three.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.three.font_size += 10
    def number3_released(self):
        self.ids.three.color = (183/255, 177/255, 210/255)
        self.ids.three.font_size -= 10

    def number4_pressed(self):
        self.ids.four.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.four.font_size += 10
    def number4_released(self):
        self.ids.four.color = (183/255, 177/255, 210/255)
        self.ids.four.font_size -= 10

    def number5_pressed(self):
        self.ids.five.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.five.font_size += 10
    def number5_released(self):
        self.ids.five.color = (183/255, 177/255, 210/255)
        self.ids.five.font_size -= 10

    def number6_pressed(self):
        self.ids.six.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.six.font_size += 10
    def number6_released(self):
        self.ids.six.color = (183/255, 177/255, 210/255)
        self.ids.six.font_size -= 10

    def number7_pressed(self):
        self.ids.seven.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.seven.font_size += 10
    def number7_released(self):
        self.ids.seven.color = (183/255, 177/255, 210/255)
        self.ids.seven.font_size -= 10

    def number8_pressed(self):
        self.ids.eight.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.eight.font_size += 10
    def number8_released(self):
        self.ids.eight.color = (183/255, 177/255, 210/255)
        self.ids.eight.font_size -= 10

    def number9_pressed(self):
        self.ids.nine.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.nine.font_size += 10
    def number9_released(self):
        self.ids.nine.color = (183/255, 177/255, 210/255)
        self.ids.nine.font_size -= 10

    def number0_pressed(self):
        self.ids.zero.color = (0.7176470588235294, 0.2823529411764706, 0.9764705882352941)
        self.ids.zero.font_size += 10
    def number0_released(self):
        self.ids.zero.color = (183/255, 177/255, 210/255)
        self.ids.zero.font_size -= 10


    def clear_pressed(self):
        self.ids.cross.source = "data/png/cross.png"
    def clear_released(self):
        self.ids.cross.source = "data/png/cross1.png"

    def enter_pressed(self):
        self.ids.check.source = "data/png/check.png"
    def enter_released(self):
        self.ids.check.source = "data/png/check1.png"


    nums_list = []
    listlen = 1
    letters = sample('0123456789', 3)
    number = ''.join(letters)
    counter = 0

    def bagels(self):
        self.listlen = len(self.nums_list)
        if len(self.nums_list) == 0:
            self.listlen = 1
        try:

            the_num = str(str(self.nums_list[0]) + str(self.nums_list[1]) + str(self.nums_list[2]))
            print(the_num)
        except:
            pass

        ##############################################################

        guesses = 10

        if self.letters[0] == '0':
            self.letters.reverse()

        print(self.number)

        try:
            guess = the_num
            self.counter += 1
            self.ids.trials.text = str(self.counter)

            clues = []
            for index in range(3):
                if guess[index] == self.number[index]:
                    clues.append('fermi')
                elif guess[index] in self.number:
                    clues.append('pico')

            shuffle(clues)
            if len(clues) == 0:
                self.ids.result.text = 'Bagels'
            else:
                self.ids.result.text = ' '.join(clues)

            if guess == self.number:
                Popup1Box().open()
                print('You got it!')
                sleep(1)
                self.back()

                #self.ids.trials.text = '0'
                #self.clear()

                #PopupBox().open()





            elif self.counter == guesses:
                Popup2Box().open()
                print('You ran out of guesses. The answer was', self.number)
                self.nums_list = []
                letters = sample('0123456789', 3)
                self.number = ''.join(letters)
                self.counter = 0
                sleep(1)
                self.ids.trials.text = '0'
                self.clear()

            # print(clues)
            # print(self.counter)
            # print(self.ids.trials.height)
        except:
            pass
        self.listlen = len(self.ids.result.text.split(' '))
        self.ids.result.font_size = (self.height*.09)/(self.listlen)
        ###############################################################

    def clear(self):
        self.ids.num1.text = '_'
        self.ids.num2.text = '_'
        self.ids.num3.text = '_'
        self.nums_list.clear()
        self.ids.result.text = 'Hint'
        self.ids.result.font_size = (self.height * .1)

    def back(self):
        self.ids.num1.text = '_'
        self.ids.num2.text = '_'
        self.ids.num3.text = '_'
        self.nums_list.clear()
        self.ids.result.text = 'Hint'
        self.ids.result.font_size = (self.height * .1)
        self.nums_list = []
        letters = sample('0123456789', 3)
        self.number = ''.join(letters)
        self.counter = 0
        self.ids.trials.text = str(self.counter)

    def nums(self, num):
        self.nums_list.append(num)
        try:
            self.ids.num1.text = str(self.nums_list[0])
        except:
            pass
        try:
            self.ids.num2.text = str(self.nums_list[1])
        except:
            pass
        try:
            self.ids.num3.text = str(self.nums_list[2])
        except:
            pass


class MainMenu(Screen):
    textsize = 0
    def fontsize(self, x, y):
        # x, y = self.width, self.height
        if x > y:
            self.textsize = y
        elif x < y:
            self.textsize = x


class Credits(Screen):
    pass


class ScreenManager(ScreenManager):
    pass


kv = Builder.load_file('main.kv')


class KivyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    KivyApp().run()
