from shapes import circle_area,rec_area,tri_area,sq_area

from cars import Honda, Toyota

h1=Honda("City")
t1=Toyota("Corolla")
h2=Honda("Civic")
t2=Honda("Camry")

h1.display()
t2.display()

print(sq_area(4))
print(rec_area(length=2,width=5))
print(tri_area(base=6,height=10))
print(circle_area(7))