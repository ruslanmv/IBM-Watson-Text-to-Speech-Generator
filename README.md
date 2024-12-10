# IBM Watson Text-to-Speech Generator

This project is a Gradio-based application that uses IBM Watson's Text-to-Speech API to convert text into speech. Users can input text, select a voice, and specify an audio format to generate audio files.

## Features
- Converts text to audio using IBM Watson's Text-to-Speech API.
- Supports multiple voices and audio formats (MP3, WAV, OGG).
- Provides a user-friendly interface built with Gradio.
- Saves generated audio files to a local folder.

## Requirements
- Python 3.8+
- IBM Cloud account with access to the Text-to-Speech service.
- `.env` file with the following keys:
  ```env
  WATSONX_APIKEY=your_ibm_cloud_api_key
  WATSONX_URL=https://us-south.ml.cloud.ibm.com
  ```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Environment**:
   Create a `.env` file in the root directory and add your IBM Watson API credentials:
   ```env
   WATSONX_APIKEY=your_ibm_cloud_api_key
   WATSONX_URL=https://us-south.ml.cloud.ibm.com
   ```

## Running the Application

1. **Start the Application**:
   ```bash
   python3 main.py
   ```

2. **Access the Interface**:
   Open your browser and go to:
   ```
   http://127.0.0.1:7860
   ```

3. **Generate Audio**:
   - Enter the text you want to convert into speech.
   - Select a voice and audio format.
   - Click "Generate Audio" to generate and download the audio file.

## Folder Structure
- `audio_results/`: Stores the generated audio files.
- `.env`: Contains your API credentials.
- `main.py`: The main Python script for running the application.

## Example Usage
After starting the application:
1. Enter `Hello, world!` in the text input field.
2. Choose `en-US_AllisonV3Voice` as the voice.
3. Select `mp3` as the audio format.
4. Click "Generate Audio" and listen to/download the generated file.

## Notes
- Ensure you have an active IBM Cloud account and a valid API key.
- The `audio_results/` folder will be created automatically if it doesn't exist.

## Dependencies
- `gradio`
- `ibm-watson`
- `python-dotenv`

Install them with:
```bash
pip install gradio ibm-watson python-dotenv
```



## Contributing
Feel free to submit issues and pull requests for improvements or new features.



