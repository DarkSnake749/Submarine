import pygame
from landscape import *

pygame.init()

class Window:   
    def __init__(self, size: list | tuple = (1080, 720), caption: str = "Window", bg_color: str = "black", fps: int = 120) -> None:
        # Window variables
        self.win: pygame.Surface = pygame.display.set_mode(size)
        self.size: pygame.math.Vector2 = pygame.math.Vector2(size[0], size[1])
        pygame.display.set_caption(caption)

        self.quit: bool = False
        self.bg_color: str = bg_color

        # Framerate variables
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.fps: int = fps
    
    def event_loop(self) -> None:
        """
        Loop through each event of the window
        """

        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                self.quit = True
    
    def update(self) -> None:
        """
        Update omponent of the window
        """

        # Update all other needed components of the window
        pygame.display.update()
        self.clock.tick(self.fps)
    
    def loop(self) -> None:
        """
        Loop all functionalities of the window
        """

        map: Map = Map([54, 36])
        map.generate_wm(.01)
        map.generate_pm()

        while not self.quit:
            # Play event
            self.event_loop()

            # Refresh the screen
            self.win.fill(self.bg_color)

            for y in range(len(map.map)):
                for x in range(len(map.map[y])):
                    rect: pygame.Rect = pygame.Rect(x * 20, y * 20, 20, 20)
                    color: tuple = (255 * map.map[y][x], 255 * map.map[y][x], 255 * map.map[y][x],)
                    pygame.draw.rect(self.win, color, rect)

            # Update components
            self.update()
    
        return

def main() -> None:
    win: Window = Window(bg_color="#3e4048")
    win.loop()

if __name__ == '__main__':
    main()