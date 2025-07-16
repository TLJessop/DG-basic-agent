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
        
    print("Deepgram API key is configured successfully!")
    # Add your agent initialization and main logic here


if __name__ == "__main__":
    main()
