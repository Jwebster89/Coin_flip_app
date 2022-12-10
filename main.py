import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class FlipCoinApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.krarths_thumb = False
        self.result_label = Label(text="")
		

    def flip_coin(self,button):
        # If Krark's thumb is on, flip two coins instead of one
        num_coins = 2 if self.krarths_thumb else 1
        
        results = []
        for _ in range(num_coins):
            result = random.choice(["success", "fail"])
            results.append(result)

        # If any of the coins are "success" and Krark's thumb is on, update the result label with "success"
        if "success" in results:
            self.result_label.text = "success"
        else:
            self.result_label.text = ", ".join(results)

    def flip_until_fail(self,button):
        # If Krark's thumb is on, flip two coins instead of one
        num_coins = 2 if self.krarths_thumb else 1

        successes = 0
        while True:
            # Flip the specified number of coins
            result = [random.choice(["success", "fail"]) for _ in range(num_coins)]

            # If any of the coins failed, print the number of successes and return
            if num_coins == 1 and "fail" in result:
                self.result_label.text = f"{successes} successes"
                return

            # If all of the coins failed and Krark's thumb is on, print the number of successes and return
            if num_coins == 2 and result == ["fail", "fail"]:
                self.result_label.text = f"{successes} successes"
                break
            successes += 1

    def build(self):
        # Create a layout to hold the widgets
        layout = BoxLayout(orientation="vertical")

        # Create a label for the app
        app_label = Label(text="Coin Flipper App")

        # Create a button to flip a single coin
        single_coin_button = Button(
            text="Flip Coin",
            on_press=self.flip_coin,
        )

        # Create a button to flip coins until failure
        until_fail_button = Button(
            text="Flip Until Fail",
            on_press=self.flip_until_fail,
        )

        # Create a toggle button to enable Krark's thumb
        krarths_thumb_button = ToggleButton(
            text="Krark's Thumb",
            on_press=lambda btn: setattr(self, "krarths_thumb", btn.state == "down"),
        )

        # Add the widgets to the layout
        layout.add_widget(self.result_label)
        layout.add_widget(single_coin_button)
        layout.add_widget(until_fail_button)
        layout.add_widget(krarths_thumb_button)

        # Return the layout
        return layout


if __name__ == "__main__":
    FlipCoinApp().run()
