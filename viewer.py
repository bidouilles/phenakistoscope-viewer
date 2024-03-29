import os
import pygame
import sys
import argparse
import imageio
from pygame.locals import QUIT, KEYDOWN, K_UP, K_DOWN, K_SPACE, K_e

def load_and_scale_image(image_path, size=(1024, 1024)):
    """Load an image from the disk and scale it to the specified size."""
    image = pygame.image.load(image_path)
    return pygame.transform.scale(image, size)

class PhenakistoscopeViewer:
    def __init__(self, image_path, frame_count):
        pygame.init()
        self.image_path = image_path  # Store the image path
        self.frame_count = frame_count
        self.current_frame = 0
        self.running = True
        self.paused = False
        self.frame_rate = 12  # Initial frame rate
        self.frames = []  # Store frames for video export

        self.disk_image = load_and_scale_image(image_path)
        self.window_size = self.disk_image.get_rect().size
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption('Phenakistoscope Viewer')

        self.precomputed_frames = self._load_frames()

    def _load_frames(self):
        frames = []
        for i in range(self.frame_count):
            angle = 360 / self.frame_count * i
            rotated_image = pygame.transform.rotate(self.disk_image, angle)
            x = (rotated_image.get_width() - self.window_size[0]) // 2
            y = (rotated_image.get_height() - self.window_size[1]) // 2
            frames.append(rotated_image.subsurface(x, y, self.window_size[0], self.window_size[1]))
        return frames

    def export_animation(self):
        base_name = os.path.splitext(os.path.basename(self.image_path))[0]  # Extract base name without extension
        output_path = f"{base_name}_animation.mp4"  # Construct output filename
        writer = imageio.get_writer(output_path, fps=self.frame_rate)
        for frame in self.frames:
            writer.append_data(pygame.surfarray.array3d(frame))
        writer.close()
        print(f"Animation exported to {output_path}")

    def start(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.paused = not self.paused
                    elif event.key == K_UP:
                        self.frame_rate += 2  # Increase speed
                    elif event.key == K_DOWN:
                        self.frame_rate = max(self.frame_rate - 2, 1)  # Decrease speed
                    elif event.key == K_e:
                        self.export_animation()  # Export the animation

            if not self.paused:
                frame = self.precomputed_frames[self.current_frame]
                self.frames.append(frame)  # Store current frame for export
                self.screen.blit(frame, (0, 0))
                self.current_frame = (self.current_frame + 1) % self.frame_count
                pygame.display.flip()

            clock.tick(self.frame_rate)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Phenakistoscope Viewer')
    parser.add_argument('image_path', type=str, help='Path to the Phenakistoscope image file')
    parser.add_argument('frame_count', type=int, help='Number of frames in the Phenakistoscope image')
    args = parser.parse_args()

    viewer = PhenakistoscopeViewer(args.image_path, args.frame_count)
    viewer.start()