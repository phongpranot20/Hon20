def number_operations():
    numbers = []
    

    print("Enter 10 numbers:")
    for i in range(10):
        while True:
                num = float(input(f"Number {i + 1}: "))
                numbers.append(num)
                break
            
    

    print(f"\nOriginal numbers: {numbers}")
    
    
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]
    
    
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    
    above_average = [n for n in numbers if n > average]
    
   
    print(f"\nEven numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Numbers greater than average ({average}): {above_average}")
    print("\nStatistics:")
    print(f"Sum: {total}")
    print(f"Average: {average}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")

   #("Phongpranot Boonmak 6730251174 sec 870")

if __name__ == "__main_":
    number_operations()
