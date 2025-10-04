def count_words(text):
    return len(text.split())

def count_file_words(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    return count_words(text)

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    print(f"Word count: {count_file_words(file_path)}")
