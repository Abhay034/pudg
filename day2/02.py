def get_array_input():
    while True:
        try:
            arr = list(map(int, input("Enter elements of the array separated by spaces: ").split()))
            return arr
        except ValueError:
            print("Please enter valid integers separated by spaces.")

def main():
    arrays = []
    
    while True:
        print("\n1. Add a new array")
        print("2. Finish and show final combined array")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            array = get_array_input()
            arrays.append(array)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    # Combine all arrays
    final_array = [item for sublist in arrays for item in sublist]
    
    print("\nFinal combined array:")
    print(final_array)

if __name__ == "__main__":
    main()
