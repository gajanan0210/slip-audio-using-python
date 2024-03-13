from pydub import AudioSegment

def split_audio(input_file, output_folder, segment_length=30):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)

    # Get the length of the audio in milliseconds
    audio_length = len(audio)

    # Calculate the number of segments
    num_segments = int(audio_length / (segment_length * 1000))

    # Split the audio into segments
    for i in range(num_segments):
        start_time = i * segment_length * 1000
        end_time = (i + 1) * segment_length * 1000

        segment = audio[start_time:end_time]

        # Save each segment to the output folder
        segment.export(f"{output_folder}/segment_{i + 1}.mp3", format="mp3")

if __name__ == "__main__":
    input_file = r"C:\Users\gajan\Downloads\aaaabb.mpeg"
    output_folder = r"G:\Mcs"
    segment_length = 29  # in seconds

    split_audio(input_file, output_folder, segment_length)
