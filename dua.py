random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 4.5, "AI"]

# Fungsi untuk memeriksa apakah nilai merupakan integer
def is_integer(item):
    return isinstance(item, int)

# Fungsi untuk memeriksa apakah nilai merupakan float
def is_float(item):
    return isinstance(item, float)

# Fungsi untuk memeriksa apakah nilai merupakan string
def is_string(item):
    return isinstance(item, str)

# Menggunakan filter dan lambda untuk memisahkan nilai sesuai dengan jenisnya
int_values = dict((item, (item // 100, (item // 10) % 10, item % 10)) for item in filter(is_integer, random_list))
float_values = tuple(filter(is_float, random_list))
string_values = list(filter(is_string, random_list))

# Menampilkan hasil pemisahan
print("Integer Values:")
for key, value in int_values.items():
    print(f"{key}: {value}")

print("Float Values:", float_values)
print("String Values:", string_values)