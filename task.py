first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

output = ''
for j in range(m):
    column = ''.join(matrix[i][j] for i in range(n))
    alphanumeric_chars = ''.join(c if c.isalnum() else ' ' for c in column)
    alphanumeric_chars = ' '.join(alphanumeric_chars.split())
    output += alphanumeric_chars

print(output)