### Khởi tạo và cài đặt trò chơi:
import pygame, sys, time, random

# Cài đặt độ khó
# Dễ      ->  10
# Trung bình    ->  25
# Khó      ->  40
# Khó hơn    ->  60
# Không thể    ->  120
difficulty = 10

# Kích thước cửa sổ
frame_size_x = 720
frame_size_y = 480

# Kiểm tra lỗi khi khởi tạo
check_errors = pygame.init()
# Kết quả ví dụ của pygame.init() -> (6, 0)
# Số thứ hai trong tuple cho biết số lỗi
if check_errors[1] > 0:
    print(f'[!] Đã gặp {check_errors[1]} lỗi khi khởi tạo trò chơi, đang thoát...')
    sys.exit(-1)
else:
    print('[+] Trò chơi đã được khởi tạo thành công')


# Khởi tạo cửa sổ trò chơi
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Màu sắc (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Âm thanh
pygame.mixer.init()
beep_sound = pygame.mixer.Sound("beep.wav")
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
