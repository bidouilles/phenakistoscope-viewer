# Phenakistoscope Viewer 🌀

## Overview

The Phenakistoscope is one of the earliest forms of moving image entertainment, predating the modern film and animation techniques we're familiar with today. Invented in the early 19th century by Belgian physicist Joseph Plateau, this fascinating device created the illusion of motion through a series of spinning discs. Each disc featured a sequence of drawings around its edge, which, when spun and viewed through a mirror via slits in the disc, appeared to be a single, animated scene. This project brings the magic of the Phenakistoscope into the digital age, allowing users to explore historical animations through a modern Python application. 🇧🇪✨

## Setup

Before diving into the world of 19th-century animation, you'll need to ensure your environment is prepared. Follow these steps to get started:

1. **Install Python**  
   Make sure Python 3.8 or higher is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**  
   This project relies on `pygame`, `imageio`, and `imageio-ffmpeg` for rendering animations and exporting them to video. Install these with pip:

   ```bash
   pip install pygame imageio imageio-ffmpeg
   ```

## Usage

To bring historical animations to life on your screen, follow these simple steps:

1.  **Run the Viewer**  
    Launch the Phenakistoscope Viewer with a command in the terminal. You'll need to provide the path to your Phenakistoscope image and the number of frames it contains:
    
    ```
    python phenakistoscope_viewer.py path_to_your_image.png number_of_frames
    ```
    
    For example:
    
    ```
    python phenakistoscope_viewer.py my_phenakistoscope.png 12
    ```
    
2.  **Control the Animation**
    
    -   **Start/Stop**: Press the spacebar to pause or resume the animation.
    -   **Adjust Speed**: Use the up and down arrow keys to control the speed of the animation.
    -   **Export to Video**: Press 'E' to export the animation as an MP4 video file. The file will be named after your original image, keeping your digital collection organized.

## Acknowledgments

-   Joseph Plateau, for his pioneering work in the field of motion pictures.
-   The open-source community, for providing the tools and libraries that made this project possible.

Embark on a journey back in time and experience the birth of animation with the Phenakistoscope Viewer! 🎥🕰️