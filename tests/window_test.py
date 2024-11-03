import pygame
pygame.init()

class Window:   
    def __init__(self, size: tuple[int, int] = (1080, 720), caption: str = "Window", bg_color: str = "black", fps: int = 120) -> None:
        # Window variables
        self.win: pygame.Surface = pygame.display.set_mode(size)
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
        Update objects and component of the window
        """

        # Refresh the screen
        self.win.fill(self.bg_color)

        # Update all other needed components of the window
        pygame.display.update()
        self.clock.tick(self.fps)
    
    def loop(self) -> None:
        """
        Loop all functionalities of the window
        """

        while not self.quit:
            # Play event
            self.event_loop()

            # Update components
            self.update()
    
        return

def test() -> Window:
    return Window()

def main() -> None:
    win: Window = Window()
    win.loop()
    exit()

if __name__ == '__main__':
    main()
