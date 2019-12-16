import arcade

import settings


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu", settings.WIDTH/2, settings.HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_key_press(self, key, modifiers):
        self.director.next_view()


if __name__ == "__main__":
    window = arcade.Window(settings.WIDTH, settings.HEIGHT, "Menu")
    window.show_view(MenuView())
    arcade.run()