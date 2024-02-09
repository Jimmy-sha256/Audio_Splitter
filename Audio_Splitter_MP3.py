from moviepy.editor import AudioFileClip

def split_audio_into_parts(input_file, output_prefix, duration_per_part):
    # Open the input audio file
    audio_clip = AudioFileClip(input_file)

    # Get the duration of the audio in seconds
    duration = audio_clip.duration  

    # Convert duration per part from minutes to seconds
    duration_per_part_sec = duration_per_part * 60  

    # Iterate over each part of the audio
    for i, start_time in enumerate(range(0, int(duration), duration_per_part_sec), start=1):
        # Calculate the end time for the current part
        end_time = min(start_time + duration_per_part_sec, duration)
        
        # Extract the part of the audio between start and end time
        part_audio = audio_clip.subclip(start_time, end_time)
        
        # Generate the output file name
        output_file = f"{output_prefix} {i}.mp3"
        
        # Write the part audio to an MP3 file
        part_audio.write_audiofile(output_file, codec='libmp3lame')
        
        # Print status message
        print(f"Part {i} saved as {output_file}")

# Example usage
input_file = "input_audio_file.mp3"
output_prefix = "part"
duration_per_part = 60  # Duration per part in minutes

split_audio_into_parts(input_file, output_prefix, duration_per_part)
