import subprocess
import os


class VocalSeparator:
    """
    A class to handle vocal and instrument separation using Demucs.
    """

    def __init__(self, output_directory="output"):
        """
        Initializes the separator with a default output directory.

        Args:
            output_directory (str): Path to save the separated tracks.
        """
        self.output_directory = output_directory
        os.makedirs(self.output_directory, exist_ok=True)

    def separate_vocals(self, input_audio_path):
        """
        Separates vocals and instruments from an audio file.

        Args:
            input_audio_path (str): Path to the input audio file.

        Returns:
            str: Path to the output directory with separated files.
        """
        if not os.path.isfile(input_audio_path):
            raise FileNotFoundError(f"Input audio file not found: {input_audio_path}")

        try:
            subprocess.run([
                "demucs",
                input_audio_path,
                "--out", self.output_directory,
                "--two-stems", "vocals"  # Separate into vocals and accompaniment
            ], check=True)
            return self.output_directory
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Error occurred during vocal separation: {e}")