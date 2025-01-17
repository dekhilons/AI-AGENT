from transformers import pipeline
from duckduckgo_search import DDGS

# Initialize DuckDuckGo search tool
class Researcher:
    def __init__(self, max_results=5, region="wt-wt", safesearch="Moderate", timelimit="y"):
        self.max_results = max_results
        self.region = region
        self.safesearch = safesearch
        self.timelimit = timelimit

    def search(self, query):
        """Perform a DuckDuckGo search and return formatted results."""
        research_summary = []
        with DDGS() as ddgs:
            results = ddgs.text(query, region=self.region, safesearch=self.safesearch, timelimit=self.timelimit)
            for result in results:
                title = result.get("title", "No Title")
                snippet = result.get("body", "No Snippet")
                link = result.get("href", "No Link")
                research_summary.append(f"- {title}: {snippet} ({link})")
                if len(research_summary) >= self.max_results:
                    break
        return "\n".join(research_summary)

# Initialize Hugging Face LLM pipeline
class Writer:
    def __init__(self, model="bigscience/bloom-560m", max_new_tokens=200):
        self.pipeline = pipeline("text-generation", model=model)
        self.max_new_tokens = max_new_tokens

    def truncate_input(self, text, max_length=512):
        """Truncate input text to fit within the model's maximum input length."""
        return text[:max_length]

    def generate_speech(self, research_summary):
        """Generate a keynote speech based on the research summary."""
        prompt_template = """
        Write a keynote speech based on the following research summary:
        {research_summary}

        Include:
        - An inspiring introduction
        - A detailed body covering the research examples
        - A conclusion that ties the advancements to a broader vision of the future.
        """
        prompt = prompt_template.format(research_summary=research_summary)
        truncated_prompt = self.truncate_input(prompt, max_length=512)  # Truncate input
        response = self.pipeline(truncated_prompt, max_new_tokens=self.max_new_tokens, truncation=True)
        return response[0]["generated_text"]

# Main AI Agent Logic
def main():
    # Step 1: Perform Research
    print("Researcher Task Output:")
    researcher = Researcher(max_results=5)
    research_query = "promising AI research 2025"
    research_output = researcher.search(research_query)
    print(research_output)

    # Step 2: Write Speech
    print("\nWriter Task Output:")
    writer = Writer(max_new_tokens=200)
    speech_output = writer.generate_speech(research_output)
    print(speech_output)

# Entry point
if __name__ == "__main__":
    main()
