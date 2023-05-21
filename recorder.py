import sounddevice as sd
import wavio as wv
import datetime
import os

def listen(stop_event, recordings_path):
    # Get the sample frequency of the sound device
    freq = sd.query_devices(None, 'input')['default_samplerate']

    # Set the duration of the recording
    duration = 5 # seconds

    print('Listening...')
    while not stop_event.is_set():
        ts = datetime.datetime.now()
        filename = ts.strftime("%Y-%m-%d_%H-%M-%S")

        # Start recorder with the given values of duration and sample frequency
        # PTL Note: I had to change the channels value in the original code to fix a bug
        recording = sd.rec(int(freq * duration), samplerate=freq, channels=2)

        # Record audio for the given number of seconds
        sd.wait()

        # Convert the NumPy array to audio file
        wv.write(os.path.join(recordings_path, f"{filename}.wav"), recording, freq, sampwidth=2)

    print('Stopped listening')