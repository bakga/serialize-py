import pickle

# Сериализация объекта в файл
def serialize_object(obj, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(obj, file)

# Десериализация объекта из файла
def deserialize_object(file_path):
    with open(file_path, 'rb') as file:
        obj = pickle.load(file)
    return obj

# Пример использования
data = {'name': 'John', 'age': 30, 'city': 'New York'}
file_path = 'data.pickle'

# Сериализация объекта в файл
serialize_object(data, file_path)

# Десериализация объекта из файла
deserialized_data = deserialize_object(file_path)

print(deserialized_data)  # {'name': 'John', 'age': 30, 'city': 'New York'}
