import openai
import sys

try:
  openai.api_key = "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"
except KeyError:
  sys.stderr.write("""
  We have a problem...
  """)
  exit(1)

cont=1
while cont==1:
  toDo=input("you: ")
  response = openai.ChatCompletion.create(
  model=
  "gpt-3.5-turbo",  # only available if OpenAI has given you early access, otherwise use: "gpt-3.5-turbo"
  # 32K context gpt-4 model: "gpt-4-32k"
  messages=[{
    "role": "system",
    "content": "You are a helpful assistant."
  },{
    "role": "user",
    "content": toDo
  }])
  respuesta=response["choices"][0]["message"]["content"]
  print(f"Chatbot : {respuesta}")

