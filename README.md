AI project to summarize lessons at university from an audio. 
It uses whisper to trascrive the adio into text, and then g4f [https://github.com/xtekky/gpt4free.git] to summarize it using gemini.

**To use it follow step by step this guide:**

**open a terminal in "lessons_summarize" path, and follow below.**

*1 = use the following command to initialize a venv environment:  python -m venv venv*

*2 = use the following command to activate the venv environment:  ./venv/Scripts/activate*

*3 = use the following command to install the requirements:  pip install -r ./requirements.txt*

*4 = run using the .ps1 file, with left click, run as powershall. Or you can run first the file "to_make.py", and then the file "AI.py", by terminal with the command: "python to_nake.py" and after that with "python AI.py"*


**IMPORTANT**

Make sure that you have Nvidia graphic card, or you have to disable CUDA device from the line 9 in to_make.py file.
This script works only if you give at the audio file a name, followed by "_prg" or "_adc" or "_asd" beacuse these are my courses.
