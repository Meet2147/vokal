🎤 vocals

vocals is a Python library that separates vocals and instruments from audio files using Demucs, a state-of-the-art deep learning model for music source separation. This tool is perfect for music enthusiasts, researchers, and audio engineers who want to isolate vocals for remixing, analysis, or karaoke tracks.

Features

	•	Separate vocals and accompaniment from audio files with ease.
	•	High-quality output using Demucs’ advanced deep learning models.
	•	Simple, reusable interface for integration into other projects.

Installation

	1.	Clone this repository or install it via pip:

pip install vocals


	2.	Ensure you have Demucs installed. You can install it via pip:

pip install demucs



Usage

Here’s how you can use the library to separate vocals and instruments:

from vocals.separator import VocalSeparator

# Initialize the separator with a specific output directory
separator = VocalSeparator(output_directory="separated_tracks")

# Separate vocals from an audio file
input_audio_path = "/path/to/audio/file.mp3"  # Replace with your file path
try:
    output_path = separator.separate_vocals(input_audio_path)
    print(f"Separation complete. Files saved in {output_path}")
except Exception as e:
    print(f"An error occurred: {e}")

Requirements

	•	Python 3.7 or higher
	•	Demucs
	•	Other dependencies are automatically installed via pip.

Example

Input file: song.mp3
Output directory: separated_tracks/

After running the script, you’ll find two files in the output directory:
	1.	vocals.wav - Isolated vocals.
	2.	no_vocals.wav - Accompaniment without vocals.

Contributing

We welcome contributions! If you have ideas or want to improve this library:
	1.	Fork the repository.
	2.	Create a new branch (git checkout -b feature-name).
	3.	Commit your changes (git commit -m "Add feature").
	4.	Push to the branch (git push origin feature-name).
	5.	Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Support

If you encounter any issues or have questions, feel free to open an issue on GitHub.

Acknowledgments

This library uses the incredible Demucs model for source separation.
