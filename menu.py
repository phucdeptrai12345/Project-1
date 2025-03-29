import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 448
SCREEN_HEIGHT = 640  # Tăng chiều cao để thêm menu dưới
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 162, 232)
YELLOW = (255, 215, 0)
BUTTON_HEIGHT = 40
FONT = pygame.font.SysFont("Arial", 18)

# Level definitions
LEVELS = [
    "Level 1",
    "Level 2",
    "Level 3",
    "Level 4",
    "Level 5",
    "Level 6"
]

BUTTON_COUNT = len(LEVELS)
BUTTON_PADDING = 5
BUTTON_WIDTH = (SCREEN_WIDTH - (BUTTON_COUNT + 1) * BUTTON_PADDING) // BUTTON_COUNT

# Hàm vẽ nút menu dưới cùng
def draw_level_buttons(surface, selected_level):
    padding_from_bottom = 10
    menu_y = SCREEN_HEIGHT - BUTTON_HEIGHT - padding_from_bottom

    for index, text in enumerate(LEVELS):
        x = BUTTON_PADDING + index * (BUTTON_WIDTH + BUTTON_PADDING)
        color = YELLOW if selected_level == index + 1 else BLUE
        pygame.draw.rect(surface, color, (x, menu_y, BUTTON_WIDTH, BUTTON_HEIGHT), border_radius=6)

        label = FONT.render(text, True, BLACK)
        label_rect = label.get_rect(center=(x + BUTTON_WIDTH // 2, menu_y + BUTTON_HEIGHT // 2))
        surface.blit(label, label_rect)

# Hàm xử lý click chuột để chọn level
def handle_level_click(pos):
    mouse_x, mouse_y = pos
    padding_from_bottom = 10
    menu_y = SCREEN_HEIGHT - BUTTON_HEIGHT - padding_from_bottom

    for index in range(BUTTON_COUNT):
        x = BUTTON_PADDING + index * (BUTTON_WIDTH + BUTTON_PADDING)
        if x <= mouse_x <= x + BUTTON_WIDTH and menu_y <= mouse_y <= menu_y + BUTTON_HEIGHT:
            return index + 1  # level_id
    return None


# Hàm show_menu không còn cần nếu menu nằm trong game luôn
# Bạn có thể xóa hoặc để đó nếu muốn giữ menu riêng bên ngoài