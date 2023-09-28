# kegiatan 1

# pertambahan
def add(angka1, angka2):
    return angka1+angka2

# fungsi Pengurangan
def minus(angka1, angka2):
    return angka1-angka2

# fungsi Perkalian
def mult(angka1, angka2):
    return angka1*angka2

# fungsi Pembagian
def div(angka1, angka2):
    if angka2 == 0:
        raise ValueError("Tidak terdefinisi")
    return angka1/angka2


def tree(node):
    if type(node) in (int, float):
        return node
    elif type(node) is tuple and len(node) == 3:
        operator, left_operand, right_operand = node
        if operator == '+':
            return add(tree(left_operand), tree(right_operand))
        elif operator == '-':
            return minus(tree(left_operand), tree(right_operand))
        elif operator == '*':
            return mult(tree(left_operand), tree(right_operand))
        elif operator == '/':
            return div(tree(left_operand), tree(right_operand))
    else:
        raise ValueError("Invalid expression tree node")

print("Kegiatan 1")
expression_tree = ('*', ('+', 2, 3), ('-', 5, 1))
result = tree(expression_tree)
print("Hasil Evaluasi Pohon Ekspresi:", result)