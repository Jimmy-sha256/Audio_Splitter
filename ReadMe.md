# Audio_Splitter_MP3

Audio_Splitter_MP3 is a Python script that allows you to split an audio file into parts of specified durations and save each part as a separate MP3 file.

## Usage

1. Install the necessary dependencies:
   ```bash
   pip install moviepy
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/your-username/audio-splitter-mp3.git
   ```

3. Navigate to the project directory:
   ```bash
   cd Audio_Splitter_mp3
   ```

4. Run the script:
   ```bash
   python Audio_Splitter_MP3.py
   ```

   Replace `input_audio_file.mp3` with the path to your input audio file.

## Parameters

- `input_file`: Path to the input audio file.
- `output_prefix`: Prefix to be used for naming the output files.
- `duration_per_part`: Duration (in minutes) of each part into which you want to split the audio.

## Example

```python
input_file = "input_audio_file.mp3"
output_prefix = "part"
duration_per_part = 60  # Duration per part in minutes
split_audio_into_parts(input_file, output_prefix, duration_per_part)
```

## Dependencies

- [MoviePy](https://github.com/Zulko/moviepy) - Python library for video editing: cutting, concatenations, title insertions, video compositing (a.k.a. non-linear editing), video processing, and creation of custom effects.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
