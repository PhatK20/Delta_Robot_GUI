import os
def generate_and_save_data(begin, end, step, file_name):
    # Tạo danh sách các giá trị của x và y
    x_values = list(range(begin, end + step, step))
    y_values = [2 * x for x in x_values]

    # Kết hợp x và y thành danh sách các cặp (x, y)
    data = list(zip(x_values, y_values))
    folder = 'Gui_Delta'
    file_path = os.path.join(folder, file_name)
    # Ghi dữ liệu vào tệp
    with open(file_path, 'w') as file:
        # Thêm dòng đầu tiên
        file.write("x, y\n")
        
        for x, y in data:
            file.write(f"{x},{y}\n")

def read_and_print_data(file_name):
    # Đọc dữ liệu từ tệp
    folder = 'Gui_Delta'
    file_path = os.path.join(folder, file_name)
    with open(file_path, 'r') as file:
        # Bỏ qua dòng đầu tiên (chứa "x, y")
        header = next(file)
        
        # Đọc và in dữ liệu
        for line in file:
            x, y = line.strip().split(',')
            print(f"x: {x}, y: {y}")

# Gọi hàm để tạo dữ liệu và lưu vào tệp
generate_and_save_data(0, 10, 1, 'output1_data.txt')

# Gọi hàm để đọc và in dữ liệu từ tệp
read_and_print_data('output1_data.txt')
