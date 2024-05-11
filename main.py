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
# Logic chính
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Khi một phím được nhấn xuống
        elif event.type == pygame.KEYDOWN:
            # W -> Lên; S -> Xuống; A -> Trái; D -> Phải
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
                beep_sound.play()

            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
                beep_sound.play()

            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
                beep_sound.play()

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
                beep_sound.play()

            # Esc -> Tạo sự kiện để thoát trò chơi
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Đảm bảo con rắn không thể di chuyển ngược lại ngay lập tức
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Di chuyển con rắn
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Cơ chế tăng kích thước của con rắn
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Xuất hiện thức ăn trên màn hình
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True

    # Đồ họa
    game_window.fill(black)
    for pos in snake_body:
        # Cơ thể con rắn
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Thức ăn của con rắn
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Điều kiện kết thúc trò chơi
    # Rơi ra khỏi biên
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    # Chạm vào cơ thể của con rắn
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    # Cập nhật lại màn hình trò chơi
    pygame.display.update()
    # Tốc độ cập nhật
    fps_controller.tick(difficulty)


# Kết thúc trò chơi
