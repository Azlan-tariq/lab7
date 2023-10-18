# Function to get user data and store it in a set
def get_user_data():
    data_set = set()
    while True:
        user_input = input("Enter data (or 'done' to finish): ")
        if user_input == 'done':
            break
        data_set.add(user_input)
    return data_set

# Function to save the data set to a file
def save_data_to_file(data_set, filename):
    with open(filename, 'w') as file:
        for item in data_set:
            file.write(f"{item}\n")

if __name__ == "__main__":
    data = get_user_data()
    file_name = "user_data.txt"
    save_data_to_file(data, file_name)
    print(f"Data saved to {file_name}")