# Number Counter Animation

This Python script creates an animated number counter that counts from a starting number to a target number and saves the animation as an MP4 video file.

## Description

The script generates a visually appealing animation that counts upward from 100 to 100,000 (by default) with a golden-colored text display. The animation is saved as an MP4 video file that can be used for presentations, social media content, or any other purpose where a dynamic number counter is needed.

## Features

- Customizable start and target numbers
- Adjustable counting speed
- Configurable text appearance (color, size, position)
- MP4 video output
- Clean, minimal visual design

## Requirements

- Python 3.x
- Matplotlib library
- FFmpeg installed on your system

## Installation

1. Install the required Python packages:
   ```
   pip install matplotlib
   ```

2. Install FFmpeg on your system:
   - Windows: Download from https://ffmpeg.org/download.html
   - macOS: `brew install ffmpeg`
   - Linux: `sudo apt-get install ffmpeg`

## Usage

Run the script directly:
```
python test.py
```

The script will generate and save an MP4 file named `counter_1lakh.mp4` in the same directory.

## Customization

You can modify several aspects of the animation by editing the script:

- **Start number**: Change the initial `'100'` value in `ax.text()` and in the calculation formula
- **Target number**: Modify the `100000` value in both the cap condition and final text
- **Counting speed**: Adjust the multiplier `(frame * 500)` - larger values count faster
- **Animation duration**: Change the `frames=220` parameter
- **Text appearance**: Modify `fontsize`, `color`, and `fontweight` in `ax.text()`
- **Output filename**: Change `'counter_1lakh.mp4'` to your preferred name

## How It Works

1. Creates a matplotlib figure with a white background
2. Sets up text display in the center of the canvas
3. Uses matplotlib's animation framework to update the displayed number
4. Saves the animation as an MP4 video using FFmpeg

## Output

The script generates a video file showing a counting animation from the start number to the target number, ending with a "+" indicator (e.g., "100000+").