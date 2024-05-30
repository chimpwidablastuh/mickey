import rumps
import time
import random
import Quartz.CoreGraphics as CG
from i18n.translate import i18n


class ConcentrationModeApp(rumps.App):
    def __init__(self):
        super(ConcentrationModeApp, self).__init__(i18n("sneakyLabel"))
        self.timer = None
        self.active = False
        self.mouse_x, self.mouse_y = self.get_mouse_position()

    def toggle_active(self, sender):
        self.active = not self.active
        if self.active:
            self.start_mouse_movement()
            self.menu[i18n("enable")].state = 1
            self.menu[i18n("disable")].state = 0
        else:
            self.stop_mouse_movement()
            self.menu[i18n("enable")].state = 0
            self.menu[i18n("disable")].state = 1

    def start_mouse_movement(self):
        self.timer = rumps.Timer(self.move_mouse_and_return, 2)
        self.timer.start()

    def stop_mouse_movement(self):
        if self.timer:
            self.timer.stop()

    def get_mouse_position(self):
        event = CG.CGEventCreate(None)
        return CG.CGEventGetLocation(event)

    def move_mouse_and_return(self, _):
        # Mets à jour la position actuelle de la souris avec la position réelle de la souris
        self.mouse_x, self.mouse_y = self.get_mouse_position()

        # Conserve la position actuelle de la souris comme l'originale
        original_x, original_y = self.mouse_x, self.mouse_y

        # Calcule une nouvelle position qui est juste à un pixel de l'originale
        new_x = original_x + 1
        new_y = original_y + 1

        # Déplace la souris à la nouvelle position
        self.move_mouse_to(new_x, new_y)

        # Ramène immédiatement la souris à sa position originale
        self.move_mouse_to(original_x, original_y)

    def move_mouse_to(self, x, y):
        event = CG.CGEventCreateMouseEvent(
            None,
            CG.kCGEventMouseMoved,
            (x, y),
            CG.kCGHIDEventTap,
        )
        CG.CGEventPost(CG.kCGHIDEventTap, event)

        # Update the current mouse position
        self.mouse_x, self.mouse_y = x, y

    def move_mouse_smoothly(self, _):
        width, height = CG.CGDisplayPixelsWide(0), CG.CGDisplayPixelsHigh(0)
        random_x = random.randint(0, width)
        random_y = random.randint(0, height)

        steps = 1
        delay = 0.02

        for i in range(steps):
            progress = (i + 1) / steps
            new_x = int(self.mouse_x + (random_x - self.mouse_x) * progress)
            new_y = int(self.mouse_y + (random_y - self.mouse_y) * progress)

            event = CG.CGEventCreateMouseEvent(
                None,
                CG.kCGEventMouseMoved,
                (new_x, new_y),
                CG.kCGHIDEventTap,
            )
            CG.CGEventPost(CG.kCGHIDEventTap, event)
            time.sleep(delay)
        self.mouse_x, self.mouse_y = random_x, random_y


if __name__ == "__main__":
    app = ConcentrationModeApp()
    app.menu.add(rumps.MenuItem(i18n("enable"), callback=app.toggle_active, key="a"))
    app.menu.add(rumps.MenuItem(i18n("disable"), callback=app.toggle_active, key="i"))
    app.run()
