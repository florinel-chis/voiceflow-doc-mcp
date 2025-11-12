"""
Voiceflow Documentation MCP Server

A Model Context Protocol server for searching Voiceflow documentation locally.
"""

from .server import mcp, main, initialize_server
from .parser import VoiceflowDocsParser
from .db_manager import VoiceflowDocsDB
from .config import Config

__all__ = [
    'mcp',
    'main',
    'initialize_server',
    'VoiceflowDocsParser',
    'VoiceflowDocsDB',
    'Config',
]

__version__ = "0.1.0"
