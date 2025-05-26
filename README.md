# MCP Client

This project implements a client for the Model Context Protocol (MCP).

## Setup

1.  **Install `uv`**: If you don't have `uv` installed, you can install it using pip:
    ```bash
    pip install uv
    ```

2.  **Install Dependencies**: Install the project dependencies from `pyproject.toml` and `python-dotenv`:
    ```bash
    uv sync
    ```

3.  **Set up Google API Key**: Create a `.env` file in the root directory of the project and add your Google API Key:
    ```
    GOOGLE_API_KEY="your_google_api_key_here"
    ```

## How to Run

To run the project, execute the `main.py` file:

```bash
uv run main.py
```
This will run the MCP client, which interacts with the [`mcp-yahoo-finance`](https://pypi.org/project/mcp-yahoo-finance/) MCP server (Yahoo Finance interaction) to get the current price of Tesla stock.

## License

This project is licensed under the MIT License.
