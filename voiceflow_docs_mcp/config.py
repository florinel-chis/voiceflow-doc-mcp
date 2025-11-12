"""
Configuration management for Multi-Source Documentation MCP
Supports: Voiceflow, Claude Code, and other documentation sources
"""

from pathlib import Path
import os
from dataclasses import dataclass
from typing import Dict


@dataclass
class Config:
    """Configuration for Multi-Source Documentation MCP server"""

    docs_paths: Dict[str, Path]  # source_name -> path mapping
    db_path: Path
    top_k: int = 5

    @classmethod
    def from_env(cls):
        """
        Load configuration from environment variables

        Environment variables:
            DOCS_PATH: Base path for all documentation directories
            VOICEFLOW_DOCS_PATH: Path to Voiceflow documentation (legacy support)
            CLAUDE_CODE_DOCS_PATH: Path to Claude Code documentation
            DOCS_DB_PATH: Path to SQLite database
            DOCS_TOP_K: Default number of search results

        Returns:
            Config instance
        """
        # Get base path or use current directory
        base_path_str = os.getenv('DOCS_PATH', str(Path.cwd()))
        base_path = Path(base_path_str).expanduser().resolve()

        # Build documentation paths dictionary
        docs_paths = {}

        # Voiceflow documentation
        vf_docs_path_str = os.getenv(
            'VOICEFLOW_DOCS_PATH',
            str(base_path / 'data' / 'voiceflow_docs')
        )
        vf_docs_path = Path(vf_docs_path_str).expanduser().resolve()
        if vf_docs_path.exists():
            docs_paths['voiceflow'] = vf_docs_path
        else:
            print(f"⚠️  Voiceflow docs not found at: {vf_docs_path}")

        # Claude Code documentation
        cc_docs_path_str = os.getenv(
            'CLAUDE_CODE_DOCS_PATH',
            str(base_path / 'data' / 'claude_code_docs')
        )
        cc_docs_path = Path(cc_docs_path_str).expanduser().resolve()
        if cc_docs_path.exists():
            docs_paths['claude-code'] = cc_docs_path
        else:
            print(f"⚠️  Claude Code docs not found at: {cc_docs_path}")

        if not docs_paths:
            raise FileNotFoundError(
                f"No documentation directories found!\n"
                f"Voiceflow path: {vf_docs_path}\n"
                f"Claude Code path: {cc_docs_path}\n"
                f"Run scrapers to download documentation."
            )

        # Database path
        db_path_str = os.getenv(
            'DOCS_DB_PATH',
            os.getenv('VOICEFLOW_DOCS_DB_PATH', '~/.mcp/multi-docs/database.db')
        )
        db_path = Path(db_path_str).expanduser()

        # Search parameters
        top_k = int(os.getenv('DOCS_TOP_K', os.getenv('VOICEFLOW_DOCS_TOP_K', '5')))

        return cls(
            docs_paths=docs_paths,
            db_path=db_path,
            top_k=top_k
        )

    def validate(self):
        """
        Validate configuration

        Raises:
            ValueError: If configuration is invalid
        """
        if not self.docs_paths:
            raise ValueError("No documentation paths configured")

        for source, path in self.docs_paths.items():
            if not path.exists():
                raise ValueError(f"{source} documentation path does not exist: {path}")

            if not path.is_dir():
                raise ValueError(f"{source} documentation path is not a directory: {path}")

        if self.top_k < 1:
            raise ValueError(f"top_k must be >= 1, got {self.top_k}")
