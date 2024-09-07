from openai import OpenAI
client = OpenAI(api_key="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")



response = client.chat.completions.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
      "role": "user",
      "content": "write a birthday message to friend"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
