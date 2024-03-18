from g4f.client import Client
import os
import time
from groq import Groq

path1 = "txt\\prg\\" 
path2 = "txt\\asd\\" 
path3 = "txt\\adc\\" 
list_file_prg = os.listdir(path1)
list_file_asd = os.listdir(path2)
list_file_adc = os.listdir(path3)

to_make_prg = []
to_make_asd = []
to_make_adc = []
# Check done and not done
def check (f, materia):
  with open ("txt\\logs.txt", "r") as d:
    if "_summ" in f:
      return
    if f not in d.read():
      if materia == "prg":
        to_make_prg.append(f)
      elif materia == "asd":
        to_make_asd.append(f)
      elif materia == "adc":
        to_make_adc.append(f)


for f in list_file_prg:
  check(f, "prg")
for f in list_file_asd:
  check(f, "asd")
for f in list_file_adc:
  check(f, "adc")

# Modelling all the text and split to the right amount of tokens
def AI (materia, f):
  path = "txt"+ "\\" + materia + "\\" + f
  text = ""
  try:
    with open (path, "r") as d:
      text += d.read()
  except:
    return
  text = text.split("\n\n\n\n")

  text1 = []
  for t in text:
    if t == "" or t == "\n":
      continue

    text1.append(t[:int((len(t) / 4))])
    text1.append(t[int((len(t) / 4)): int((len(t) / 4))*2])
    text1.append(t[int((len(t) / 4))*2: int((len(t) / 4))*3])
    text1.append(t[int((len(t) / 4))*3:])

    # text1.append(t[:int((len(t) / 3))])
    # text1.append(t[int((len(t) / 3)): int((len(t) / 3))*2])
    # text1.append(t[int((len(t) / 3))*2:int((len(t)))])

    # text1.append(t[:int((len(t) / 2))])
    # text1.append(t[int((len(t) / 2)):])


  with open (path.replace(".", "_summ."), "w") as d:
    pass

#_______________________________________________________________________________________
  # for t in text1:
  #   client = Groq(
  #       api_key="YOUR_API_KEY",
  #   )

  #   chat_completion = client.chat.completions.create(
  #       messages=[
  #           {
  #               "role" :"system",
  #               "content" : "You get a full day lesson, and summarize it in ITALIAN, not in english, with a full-complete summary of the lesson as long as possible"
  #           },
  #           {
  #               "role": "user",
  #               "content": t,
  #           }
  #       ],
  #       model="mixtral-8x7b-32768",
  #       stream=True,
  #       max_tokens=32768,  # Change the value to an integer
  #   )
  #   response = ""
  #   for chunk in chat_completion:
  #       print(chunk.choices[0].delta.content or "", end="")
  #       response += chunk.choices[0].delta.content or ""
  #   response += "\n\n\n\n\n"
    
  #   with open (path.replace(".", "_summ."), "a", encoding="utf-8") as d:
  #     d.write(response)
  #     d.write("\n\n\n\n\n")
  #   # time.sleep(3)

  # with open (r"\txt\logs.txt", "a", encoding="utf-8") as p:
  #   p.write(f + "\n")

#_______________________________________________________________________________________
  for t in text1:
    client = Client()
    response = client.chat.completions.create(
    model="gemini-pro",
    messages=[{"role": "user", "content": "Fai un riassunto della seguente lezione:\n" + t}]
    )
    print(response.choices[0].message.content)
    response = response.choices[0].message.content
    
    with open (path.replace(".", "_summ."), "a", encoding="utf-8") as d:
      d.write(response)
      d.write("\n\n\n\n\n")
    # time.sleep(3)

  with open (r"\txt\logs.txt", "a", encoding="utf-8") as p:
    p.write(f + "\n")


for f in to_make_prg:
  AI ("prg", f)


for f in to_make_asd:
  AI ("asd", f)


for f in to_make_adc:
  AI ("adc", f)

