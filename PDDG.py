"""def play_music(file_path, loop=True):
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)

        # Set the playback to loop indefinitely if loop is True
        pygame.mixer.music.play(loops=-1 if loop else 0)

        # Keep the program running while the music is playing
        while pygame.mixer.music.get_busy():
            continue

    except pygame.error as e:
        print(f"Error: {e}")

    finally:
        pygame.mixer.quit()

def stop_music():
    pygame.mixer.music.stop()

# Function to start or resume the music
def start_music():
    mp3_file_path = "Music_PeDnevnik/piano-bar-cocktail-lounge-music-180082.mp3"
    play_music(mp3_file_path, loop=True)

    import threading
import subprocess
import pygame"""

"""def music_player():
    mp3_file_path = "Music_PeDnevnik/piano-bar-cocktail-lounge-music-180082.mp3"
    play_music(mp3_file_path, loop=True)

# STARTA MJUUUZU
music_thread = threading.Thread(target=music_player)
music_thread.start() DELETE IF YOU WANT MUSIC"""

#music_thread.join()
