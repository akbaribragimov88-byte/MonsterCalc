from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

# Oyna o'lchamini va rangini sozlaymiz
Window.clearcolor = (0.05, 0.05, 0.05, 1) # Qora fon

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical", spacing=5, padding=10)
        
        # Sonlar chiqadigan katta oq ekran
        self.solution = Label(
            text="0", pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=50, halign="right", valign="middle",
            size_hint=(1, 0.3), text_size=(Window.width - 40, Window.height * 0.3)
        )
        main_layout.add_widget(self.solution)
        
        # Tugmalar joylashuvi
        buttons = [
            ["AC", "/", "*", "C"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            [".", "0", "00", "MASTER AMIN"]
        ]
        
        for row in buttons:
            h_layout = BoxLayout(spacing=5)
            for label in row:
                button = Button(
                    text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5},
                    background_normal='', background_color=(0.2, 0.2, 0.2, 1) # To'q kulrang
                )
                # Maxsus ranglar
                if label in ["AC", "C"]: button.background_color = (0.8, 0.3, 0, 1) # To'q sariq
                if label == "=": button.background_color = (0, 0.5, 0.2, 1) # Yashil
                if label == "MASTER AMIN": button.background_color = (0.4, 0.2, 0.1, 1) # Jigarrang
                
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "AC":
            self.solution.text = "0"
        elif button_text == "C":
            self.solution.text = current[:-1] if len(current) > 1 else "0"
        elif button_text == "=":
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"
        else:
            if current == "0":
                self.solution.text = button_text
            else:
                self.solution.text += button_text

if __name__ == "__main__":
    CalculatorApp().run()