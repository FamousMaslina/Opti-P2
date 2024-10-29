import os
import pygame
from op2api import *

# Check for the audio device
if os.path.exists('idsound.py'):
    pass
else:
    print("Audio Device not found!")
    exit()

# Define compatible audio extensions
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.ogg', '.flac']

# Initialize pygame mixer for audio control
pygame.mixer.init()

# Find audio files in the current directory
def find_audio_files():
    files = os.listdir(os.getcwd())
    return [file for file in files if any(file.endswith(ext) for ext in AUDIO_EXTENSIONS)]

# Define control functions
def play_song(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    print(f"Playing: {song}")

def pause_song():
    pygame.mixer.music.pause()
    print("Paused")

def unpause_song():
    pygame.mixer.music.unpause()
    print("Resumed")

def stop_song():
    pygame.mixer.music.stop()
    print("Stopped")

# Stylish display function
def display_screen(song_name, status="Stopped", show_menu=False, audio_files=None):
    clear()
    print("="*40)
    print("  ______   __   _______     _______     ")
    print(" |  __  \\ |  | |   _   |   |   _   |    ")
    print(" | |  \\  ||  | |  |_|  |   |  |_|  |    ")
    print(" | |__/ / |  | |       |   |       |    ")
    print(" |  __  \\ |  | |   _   |   |   _   |    ")
    print(" | |  \\  ||  | |  | |  |   |  | |  |    ")
    print(" |_|   \\____| |_| |_| |_| |_| |_| |_|   ")
    print("="*40)
    
    # Display screen information
    print(f"==[ Status: {status} ]" + "="*18)
    print(f"==[ Now Playing: {song_name} ]" + "="*10)
    print("="*40)
    
    # Show menu if requested
    if show_menu:
        print("Available songs:")
        for idx, song in enumerate(audio_files):
            print(f"{idx + 1}. {song}")
        print("Choose a song number, or enter 'q' to quit")

# Main playback loop
def main():
    audio_files = find_audio_files()
    if not audio_files:
        display_screen("N/A", "No compatible audio files found")
        return

    current_index = None  # Track the current song's index

    while True:
        if current_index is None:
            display_screen("N/A", "Stopped", show_menu=True, audio_files=audio_files)
            
            # User selects a song
            choice = input("Enter the number of the song to play (or 'q' to quit): ")
            if choice.lower() == 'q':
                break
            try:
                current_index = int(choice) - 1
                if current_index < 0 or current_index >= len(audio_files):
                    print("Invalid choice. Please try again.")
                    current_index = None
                    continue
                play_song(audio_files[current_index])
                display_screen(audio_files[current_index], "Playing")
            except ValueError:
                print("Invalid input. Please enter a number.")
                current_index = None
                continue

        # Control loop for current song
        command = input("Enter 'p' to pause, 'r' to resume, 's' to stop, or 'n' for next song: ").lower()
        if command == 'p':
            pause_song()
            display_screen(audio_files[current_index], "Paused")
        elif command == 'r':
            unpause_song()
            display_screen(audio_files[current_index], "Playing")
        elif command == 's':
            stop_song()
            display_screen("N/A", "Stopped", show_menu=True, audio_files=audio_files)
            current_index = None  # Reset to allow new song selection
        elif command == 'n':
            stop_song()
            current_index = (current_index + 1) % len(audio_files)  # Move to the next song in the list
            play_song(audio_files[current_index])
            display_screen(audio_files[current_index], "Playing")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
