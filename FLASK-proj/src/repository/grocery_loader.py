import csv


# data = [{'name': 'John Doe', 'age': 30}, {'name': 'Jane Doe', 'age': 25}]
def write_list_of_dicts_to_csv(filename, data):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


# dict = { 'SKU': 'A123', ... }
def read_csv_to_dict(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


# data = [0, 1, 2, 3]
def main(filename):
    data = read_csv_to_dict(filename)
    for row in data:
        #print(row)
        #Print SKU
        sku_value = row['SKU']
        #print("SKU=" + sku_value)
        if sku_value == "A123":
            row['Price'] = 99999999

    # Guardar los cambios editados
    write_list_of_dicts_to_csv("grocery_edited.csv", data)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('sample_grocery.csv')