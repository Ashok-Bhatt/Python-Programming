class Food_Items:
    pass

apple = Food_Items()
apple.calories="100 per large"
apple.color="Red"
apple.nutritions=["Carbohydrate","Fibre","Water","Vitamin A"]
print("The calorie content for apple:",apple.calories)

ladoo = Food_Items()
ladoo.calories="250 per 100 gm"
ladoo.color="Yellow"
ladoo.nutritions=["Fat","Carbohydrates"]
print("The color of ladoo:",ladoo.color)

tomato = Food_Items()
tomato.calories = "120 per 100 gm"
tomato.color="Red"
tomato.nutritions=["carbohydrate","Water","Vitamin C"]
print("The nutritions available in tomato:",tomato.nutritions)

print(apple,tomato,ladoo)
print(apple.nutritions,ladoo.color,tomato.calories)