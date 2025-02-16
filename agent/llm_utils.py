from openai import OpenAI

def summarize_text(text: str) -> str:
    """ Calls an LLM API to summarize the given text. """
    client = OpenAI(api_key="your_openai_api_key")

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Summarize the following text"},
                  {"role": "user", "content": text}]
    )
    return response.choices[0].message.content.strip()

