import speech_recognition as sr
from pytube import YouTube

def youtube_link_to_text(youtube_link):
    """
    Function to transcribe audio from a YouTube video to text.

    Parameters:
        youtube_link (str): The YouTube link of the video with audio to transcribe.

    Returns:
        str: The transcribed text.
    """
    # Download the YouTube video
    video = YouTube(youtube_link)

    # Get the highest resolution audio stream available (assuming it's the audio only)
    audio_stream = video.streams.filter(only_audio=True).highest_resolution()

    # Download the audio stream
    audio_file = f"{video.title}.{audio_stream.subtype}"
    audio_stream.download()

    # Transcribe the downloaded audio to text
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as audio:
        audio_data = recognizer.record(audio)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Transcription could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"
        finally:
            # Remove the downloaded audio file
            import os
            os.remove(audio_file)

# Example usage:
if __name__ == "__main__":
    youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace this with your desired YouTube link

    transcribed_text = youtube_link_to_text(youtube_link)
    print("Transcribed Text:")
    print(transcribed_text)
