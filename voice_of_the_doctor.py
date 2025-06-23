# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# Suppress all warnings and pygame welcome message
import os
import sys
import warnings
from contextlib import redirect_stdout

# Suppress all warnings
warnings.filterwarnings("ignore")

# Hide pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Suppress stdout temporarily during pygame import
with open(os.devnull, 'w') as fnull:
    with redirect_stdout(fnull):
        import pygame
        pygame.mixer.init()


#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS
import pygame  # Add pygame import

# Initialize pygame mixer
pygame.mixer.init()

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hey I'm Hasrat Ali, I'm a good boy!"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")


#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
from elevenlabs import Voice, VoiceSettings
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    try:
        # Initialize the client
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        
        # Generate speech
        response = client.text_to_speech.convert(
            text=input_text,
            voice_id="21m00Tcm4TlvDq8ikWAM",  # Voice ID for "Rachel"
            model_id="eleven_turbo_v2",
            output_format="mp3_22050_32",
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.75,
                style=0.0,
                use_speaker_boost=True,
                speed=1.0
            )
        )
        
        # Save the audio
        with open(output_filepath, 'wb') as file:
            for chunk in response:
                if chunk:
                    file.write(chunk)
        
        print(f"Audio saved to: {output_filepath}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

#Step2: Use Model for Text output to Voice

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    
    try:
        # Play using pygame
        pygame.mixer.music.load(output_filepath)
        pygame.mixer.music.play()
        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi I'm Hasrat Ali, autoplay testing!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

import uuid

def text_to_speech_with_elevenlabs(input_text, output_filepath=None):
    try:
        client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
        
        if output_filepath is None:
            output_filepath = f"{uuid.uuid4()}.mp3"

        # Stop pygame playback and release file
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit()

        # Remove if file already exists
        if os.path.exists(output_filepath):
            os.remove(output_filepath)

        response = client.text_to_speech.convert(
            text=input_text,
            voice_id="MF3mGyEYCl7XYWbV9V6O",
            model_id="eleven_turbo_v2",
            output_format="mp3_22050_32",
            voice_settings=VoiceSettings(
                stability=0.5,
                similarity_boost=0.75,
                style=0.0,
                use_speaker_boost=True,
                speed=1.0
            )
        )

        with open(output_filepath, 'wb') as file:
            for chunk in response:
                if chunk:
                    file.write(chunk)

        # Play the file
        pygame.mixer.init()
        pygame.mixer.music.load(output_filepath)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        return output_filepath
        
    except Exception as e:
        print(f"An error occurred during generation: {str(e)}")
        return None

# Example usage
input_text = "Hi I'm Hasrat Ali, autoplay testing!"
# text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")

