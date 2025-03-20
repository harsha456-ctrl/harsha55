def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def reverse_both(text):
    reversed_chars = reverse_characters(text)
    reversed_words = reverse_words(text)
    return reversed_chars, reversed_words

def main():
    while True:
        print("\nText Reverser Menu:")
        print("1. Reverse character order")
        print("2. Reverse word order")
        print("3. Reverse both")
        print("4. Exit")
        
        choice = input("Choose an option (1/2/3/4): ")
        
        if choice == '4':
            print("Exiting program. Goodbye!")
            break
        
        text = input("Enter text: ")
        if not text.strip():
            print("Error: Input cannot be empty. Please enter valid text.")
            continue
        
        if choice == '1':
            print("Reversed characters:", reverse_characters(text))
        elif choice == '2':
            print("Reversed words:", reverse_words(text))
        elif choice == '3':
            reversed_chars, reversed_words = reverse_both(text)
            print("Reversed characters:", reversed_chars)
            print("Reversed words:", reversed_words)
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
