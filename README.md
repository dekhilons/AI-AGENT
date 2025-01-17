AI Researcher and Speech Generator
This project is a simple yet powerful demonstration of how to use AI for automated research and speech generation. The application combines DuckDuckGo Search for web-based research and Hugging Face Transformers for generating human-like keynote speeches. It is modular, extensible, and ready to run with minimal setup.

Features
Automated Research:

Fetches real-time data from DuckDuckGo on a given query.
Summarizes up to 5 search results, including titles, snippets, and links.
AI-Generated Speech:

Uses a pre-trained Hugging Face model (bigscience/bloom-560m) to craft professional speeches.
Includes an inspiring introduction, detailed body, and a forward-looking conclusion.
Customizable:

Adjust the number of search results, truncation limits, and output token length.
Easily switch to alternative Hugging Face models.
How It Works
Researcher:

Performs a DuckDuckGo search for the provided query.
Retrieves and formats search results into a concise summary.
Writer:

Accepts the research summary as input.
Generates a keynote speech based on the summary using an AI text-generation model.
Main Workflow:

Executes the research task.
Passes the research results to the writer to generate the speech.
