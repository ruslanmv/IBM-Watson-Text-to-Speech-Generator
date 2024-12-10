import os
import gradio as gr
from typing import Union
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

RESULTS_FOLDER = "audio_results"

class VoiceGenerator:
    def __init__(self, api_key: str = None, url: str = None):
        """Initialization for Text-to-Speech service"""
        load_dotenv()
        self.url = url or os.environ.get("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
        self.api_key = api_key or os.environ.get("WATSONX_APIKEY")
        if not self.api_key:
            raise ValueError("API Key not provided. Set WATSONX_APIKEY in .env or pass it as a parameter.")

        # Authenticate
        self.client = TextToSpeechV1(authenticator=IAMAuthenticator(self.api_key))
        self.client.set_service_url(self.url)

    def generate_voice(self, text: str, output_name: str = "output", voice: str = "en-US_AllisonV3Voice", format: str = "mp3") -> str:
        """Generates voice audio from input text"""
        if not os.path.exists(RESULTS_FOLDER):
            os.makedirs(RESULTS_FOLDER)

        output_path = os.path.join(RESULTS_FOLDER, f"{output_name}.{format}")
        with open(output_path, "wb") as audio_file:
            audio_file.write(
                self.client.synthesize(
                    text, voice=voice, accept=f"audio/{format}"
                ).get_result().content
            )
        return output_path

def generate_audio(text: str, voice: str, format: str):
    generator = VoiceGenerator()
    try:
        output_path = generator.generate_voice(text, "generated_audio", voice, format)
        return f"Audio generated successfully! File saved at: {output_path}", output_path
    except Exception as e:
        return f"Error: {str(e)}", None

# Gradio Application
def main():
    with gr.Blocks() as app:
        gr.Markdown("""# IBM Watson Text-to-Speech Generator
        Convert your text to speech using IBM Watson Text-to-Speech API. Configure the voice and output format as needed.
        """)

        with gr.Row():
            text_input = gr.Textbox(label="Input Text", placeholder="Enter text to synthesize...")
            voice_input = gr.Dropdown(
                choices=["en-US_AllisonV3Voice", "en-US_MichaelV3Voice", "en-GB_KateV3Voice"],
                label="Select Voice",
                value="en-US_AllisonV3Voice",
            )
            format_input = gr.Dropdown(
                choices=["mp3", "wav", "ogg"],
                label="Select Audio Format",
                value="mp3",
            )

        output_message = gr.Textbox(label="Status", interactive=False)
        audio_output = gr.Audio(label="Generated Audio", interactive=False)

        def generate(text, voice, format):
            message, path = generate_audio(text, voice, format)
            if path:
                return message, path
            return message, None

        generate_button = gr.Button("Generate Audio")
        generate_button.click(
            generate,
            inputs=[text_input, voice_input, format_input],
            outputs=[output_message, audio_output],
        )

    app.launch()

if __name__ == "__main__":
    main()
