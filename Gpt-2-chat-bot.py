#imports
import openai

continues=1

#api key
openai.api_key = "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"


def chatbot():
  con=1
  while con == 1:

    user_input = input("You: ")

    if user_input.lower() == "exit":
      con =2
    elif user_input.lower() != "exit":
      try:
        response = openai.Completion.create(engine="text-davinci-002",prompt=user_input + " ",max_tokens=2048,temperature=0.5)
        reponse1=response["choices"][0]["text"]
        print("Chatbot: ",reponse1)
      except:
        print("Chatbat fallo en ejecucion")

#Zona de ejecucion...
chatbot()
