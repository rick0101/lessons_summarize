# Lesson Summarizer

This is an AI project that summarizes lessons at the university from an audio recording. It uses Whisper to transcribe the audio into text, and then utilizes the GPT-4-Free (g4f) library to summarize the text using the Gemini model.

## Prerequisites

- Python 3.x
- NVIDIA GPU (optional, but recommended for better performance)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rick0101/lessons_summarize.git
```

2. Navigate to the project directory:

``` bash
cd lessons_summarize
```

3. Create and activate a virtual environment:

``` python
python -m venv venv
```
```
./venv/Scripts/activate
```

4. Install the required packages:

``` python
pip install -r requirements.txt
```

## Usage

1. Place your audio files (with filenames ending in _prg, _adc, or _asd) in the raw directory.
2. Run the script:

``` bash
python to_make.py
python AI.py
```

Alternatively, you can run the PowerShell script `run.ps1` by right-clicking on it and selecting "Run with PowerShell".

**Note:** If you don't have an NVIDIA GPU, you need to disable the CUDA device by commenting out or removing line 9 in the `to_make.py` file.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
