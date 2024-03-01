simon_says = ["Hands on head", "Hands on ears",
              "Right hand up", "Left hand up",
              "Hands on shoulders"]

print("Pick a number between 0 and 4")
index = int(input())
instruction = simon_says[index]

print(f"Simon says...{instruction}")
