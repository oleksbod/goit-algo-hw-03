import turtle

def koch_snowflake(turtle, order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(turtle, order-1, size/3)
            turtle.left(angle)

def closed_koch_snowflake(turtle, order, size):
    for _ in range(3):
        koch_snowflake(turtle, order, size)
        turtle.right(120)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))

    # Створення вікна та об'єкта черепашки
    window = turtle.Screen()
    window.bgcolor("white")
    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)  # Найвища швидкість

    # Розміщення черепашки у правильному місці
    snowflake_turtle.penup()
    snowflake_turtle.goto(-150, 90)
    snowflake_turtle.pendown()

    # Виклик функції для створення сніжинки Коха
    closed_koch_snowflake(snowflake_turtle, level, 300)

    # Закриття вікна при кліку
    window.exitonclick()

if __name__ == "__main__":
    main()