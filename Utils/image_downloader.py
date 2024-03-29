from simple_image_download import simple_image_download as sp

response = sp.simple_image_download

non_invasive_turtles = "river cooter, peninsula cooter, florida red bellied cooter, alligator snapping turtle, common musk turtle, european pond turtle, false map turtle, map turtle, mississippi map turtle, mud turtle, razorback musk turtle, snake necked turtle, spiny softshell turtle, spotted turtle"

# response().download(keywords = "Threskiornis aethiopicus", limit = 50) # <-- Sacred Ibis
# response().download(keywords = "Trachemys scripta", limit = 50) # <-- Terrapins
# response().download(keywords = "red-eared slider terrapin, yellow-bellied slider terrapin, Cumberland slider terrapin, common slider terrapin", limit = 102)
response().download(keywords = non_invasive_turtles , limit = 503)