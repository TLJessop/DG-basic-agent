import os
import requests
import wave
import io
import time
import json
import threading
from datetime import datetime

from deepgram import (
  DeepgramClient,
  DeepgramClientOptions,
  AgentWebSocketEvents,
  AgentKeepAlive,
)
from deepgram.clients.agent.v1.websocket.options import SettingsOptions

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")


def main():
    """Main function to initialize and run the Deepgram voice agent."""
    if not DEEPGRAM_API_KEY:
        print("Error: DEEPGRAM_API_KEY environment variable is not set.")
        print("Please set it using 'export DEEPGRAM_API_KEY=your_api_key'")
        return
        
    print("Deepgram API key is configured successfully!")
    # Add your agent initialization and main logic here


if __name__ == "__main__":
    main()
