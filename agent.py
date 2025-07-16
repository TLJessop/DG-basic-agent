import os
from pathlib import Path
import requests
import wave
import io
import time
import json
import threading
from datetime import datetime
from dotenv import load_dotenv

from deepgram import (
  DeepgramClient,
  DeepgramClientOptions,
  AgentWebSocketEvents,
  AgentKeepAlive,
)
from deepgram.clients.agent.v1.websocket.options import SettingsOptions

# Load environment variables from .env file
load_dotenv()


DEEPGRAM_API_KEY = os.getenv("DEEPGRAM-API-KEY")

def main():
    """Main function to initialize and run the Deepgram voice agent."""
    if not DEEPGRAM_API_KEY:
        print("Error: DEEPGRAM_API_KEY environment variable is not set.")
        return
        
    config_options = DeepgramClientOptions(options={"keepalive": "true"})

    # Init client
    dg_client = DeepgramClient(DEEPGRAM_API_KEY, config_options)

    # Configure the Agent
    options = SettingsOptions()
    # Audio input configuration
    options.audio.input.encoding = "linear16"
    options.audio.input.sample_rate = 24000
    # Audio output configuration
    options.audio.output.encoding = "linear16"
    options.audio.output.sample_rate = 24000
    options.audio.output.container = "wav"
    # Agent configuration
    options.agent.language = "en"
    options.agent.listen.provider.type = "deepgram"
    options.agent.listen.provider.model = "nova-3"
    options.agent.think.provider.type = "open_ai"
    options.agent.think.provider.model = "gpt-4o-mini"
    options.agent.think.prompt = "You are a friendly AI assistant."
    options.agent.speak.provider.type = "deepgram"
    options.agent.speak.provider.model = "aura-2-thalia-en"
    options.agent.greeting = "Hello! How can I help you today?"

    # Send Keep Alive messages
    def send_keep_alive():
        while True:
            time.sleep(5)
            print("Sending keep alive...")
            connection.send(str(AgentKeepAlive()))

    # Start keep-alive in a separate thread
    keep_alive_thread = threading.Thread(target=send_keep_alive, daemon=True)
    keep_alive_thread.start()




    
if __name__ == "__main__":
    main()
