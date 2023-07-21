import json

def generate_output():
    output = []
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            output.append("BIGBANG")
        elif num % 3 == 0:
            output.append("BIG")
        elif num % 5 == 0:
            output.append("BANG")
        else:
            output.append(str(num))
    return output

def save_to_json(output, filename):
    with open(filename, 'w') as f:
        json.dump(output, f)

if __name__ == "__main__":
    output_array = generate_output()
    save_to_json(output_array, "output.json")
