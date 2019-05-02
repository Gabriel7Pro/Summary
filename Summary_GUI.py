from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label


class WindowFileDropExampleApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        print(file_path)
        return

class WelcomeScreen(Window):
	def build(self):
		return Label(text = "Welcome")
		

class MyApp(App):
	def build(self):
		return WelcomeScreen()
		

if __name__ == '__main__':
    MyApp().run()