### Khởi tạo và cài đặt trò chơi:

# Các biến trò chơi
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

score = 0


### Hàm và biến cần thiết:
### Logic chính
# Xử lý sự kiện
# Đảm bảo con rắn không thể di chuyển ngược lại ngay lập tức
# Di chuyển con rắn
# Cơ chế tăng kích thước của con rắn
# Xuất hiện thức ăn trên màn hình
# Đồ họa
# Điều kiện kết thúc trò chơi
# Cập nhật và hiển thị màn hình
# Điều chỉnh tốc độ cập nhật
### Xử lý sự kiện bấm phím và phát âm thanh:
# Xử lý sự kiện nhấn phím
# Phát âm thanh khi nhấn phím

# Kết thúc trò chơi
