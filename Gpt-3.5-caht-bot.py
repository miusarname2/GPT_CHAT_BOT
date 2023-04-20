import openai
import os
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
  dos=input("you: ")
  if dos != "exit":
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": "You are a helpful assistant."
    },{
      "role": "user",
      "content": dos
    }])
    respuesta=response["choices"][0]["message"]["content"]
    print(f"Chatbot : {respuesta}")
  else:
    cont=2

