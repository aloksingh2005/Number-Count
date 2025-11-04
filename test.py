# Import necessary libraries for plotting and animation
import matplotlib.pyplot as plt  # For creating figures and axes (the canvas for our animation)
import matplotlib.animation as animation  # For creating animated plots
from matplotlib.animation import FFMpegWriter  # For saving the animation as an MP4 video file (requires ffmpeg installed)

# Create a figure and axis object – this is like setting up a blank white canvas
fig, ax = plt.subplots()  # fig is the overall window, ax is the plot area inside it

# Set the x-axis limits: From 0 to 110000 – this makes space for large numbers (like 100000) without clipping
ax.set_xlim(0, 110000)  # Adjust this if your target number is bigger/smaller (e.g., for 1 million, set to 1100000)
ax.set_ylim(0, 1)  # Y-limits are narrow (0 to 1) because we only need vertical space for the text, not a full graph

# Set the background color of the plot area to white
ax.set_facecolor('white')  # Change to any color if needed, e.g., 'black' for dark mode

# Turn off the axes (no ticks, labels, or borders – we want a clean look)
ax.axis('off')  # This hides x/y axes completely

# Create the text object that will display the counter
# Position: x=55000 (center of xlim 0-110000), y=0.5 (middle of ylim 0-1)
# Initial text: '100', horizontal align center, vertical align center, font size 48, color golden (#efbe06), bold
text = ax.text(55000, 0.5, '100', ha='center', va='center', fontsize=48, color='#efbe06', fontweight='bold')
# To change: Update '100' for start number, fontsize for bigger/smaller text, color for new hex/RGB

# Define the update function – this runs for every frame of the animation
# 'frame' is the current frame number (starts from 0)
def update(frame):
    # Counting phase: If frame < 200, increment the number
    if frame < 200:  # 200 is the number of frames for counting – increase for slower animation, decrease for faster
        # Calculate current number: Start at 100, add (frame * increment_per_frame)
        # Here, increment_per_frame = 500 – this makes it speed up to ~100000 in 200 frames
        num = 100 + (frame * 500)  # Change 100 to your start number; change 500 to adjust speed (bigger = faster count)
        # Cap the number at target (100000) to avoid overshooting
        if num > 100000:  # Change 100000 to your target number
            num = 100000
        # Update the text with the new number (convert to int and string)
        text.set_text(str(int(num)))  # For decimals, remove int() if needed
    else:
        # After counting (frame >= 200), show the final text like '100000+'
        text.set_text('100000+')  # Change this to whatever end text you want, e.g., '1L+' or 'Done!'
    # Return the text object – matplotlib needs this for blitting (efficient animation)
    return text,

# Create the animation object
# FuncAnimation: Takes figure, update function, total frames=220 (200 count + 20 hold at end), interval=20ms between frames
ani = animation.FuncAnimation(fig, update, frames=220, interval=20, blit=True)
# blit=True makes it faster by only updating changed parts; frames=220: adjust for longer/shorter video
# interval=20: Smaller = faster playback; e.g., 10 for super fast

# Set up the video writer for saving as MP4
# fps=50: Frames per second (higher = smoother, but bigger file)
# metadata: Optional info like artist name
# bitrate=1800: Video quality (higher = better quality, bigger file)
writer = FFMpegWriter(fps=50, metadata=dict(artist='Me'), bitrate=1800)
# Note: ffmpeg must be installed on your system (Google "install ffmpeg" for your OS)

# Save the animation as 'counter_1lakh.mp4' – change filename if you want
ani.save('counter_1lakh.mp4', writer=writer)  # This creates the MP4 file in your current folder

# Optional: Show a preview window of the animation (closes after it plays)
plt.show()  # Remove this line if you don't want the popup window