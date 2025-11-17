import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, HORIZONTAL_ROAD_RECT, VERTICAL_ROAD_RECT
from resources import load_car_collections, load_center_images
from ui import create_button, render_multiline, render_label
from lane import Lane, SpawnConfig
from traffic_controller import TrafficController, Mode

# Movement functions for lanes
def move_r1_1(car): car.rect.x += car.speed
def move_r1_2(car): car.rect.x += car.speed
def move_r2_1(car): car.rect.y += car.speed
def move_r2_2(car): car.rect.y += car.speed
def move_r3_1(car): car.rect.x -= car.speed
def move_r3_2(car): car.rect.x -= car.speed
def move_r4_1(car): car.rect.y -= car.speed
def move_r4_2(car): car.rect.y -= car.speed

# Exit checks
def exit_r1_1(car) -> bool: return car.rect.x >= 575
def exit_r2_1(car) -> bool: return car.rect.y >= 325
def exit_r3_1(car) -> bool: return car.rect.x < 850
def exit_r4_1(car) -> bool: return car.rect.y < 625
def exit_generic_right(car) -> bool: return car.rect.x > WINDOW_WIDTH
def exit_generic_bottom(car) -> bool: return car.rect.y > WINDOW_HEIGHT
def exit_generic_left(car) -> bool: return car.rect.x < -100
def exit_generic_top(car) -> bool: return car.rect.y < -100

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Four-Way Traffic Road")
    clock = pygame.time.Clock()

    # Load assets
    V_car_images, H_car_images, V1_car_images, H1_car_images = load_car_collections()
    r1_image, r2_image, r3_image, r4_image = load_center_images()

    # UI
    font_med = pygame.font.SysFont("comicsansms", 40)
    Forward = create_button(font_med, "Forward", (325, 200), (350, 400), (135, 206, 235), (0, 0, 139))
    Backward = create_button(font_med, "Backward", (350, 825), (450, 400), (135, 206, 235), (0, 0, 139))
    Mode_btn = create_button(font_med, "Change Mode", (1175, 100), (650, 203), (135, 206, 235), (0, 0, 139))
    Auto_btn = create_button(font_med, "Auto Mode", (1175, 300), (650, 203), (135, 206, 235), (0, 0, 139))
    Manual_btn = create_button(font_med, "Manual Mode", (1175, 300), (650, 203), (135, 206, 235), (0, 0, 139))

    # Road overlays and labels (re-using your Show_Road idea via ui.render_multiline)
    Road1 = render_multiline(font_med, "Top->R1\nStop->R2\nStop->R3\nRear->R4", (0,0,139), 1175, 700)
    Road2 = render_multiline(font_med, "Top->R2\nStop->R3\nStop->R4\nRear->R1", (0,0,139), 1175, 700)
    Road3 = render_multiline(font_med, "Top->R3\nStop->R4\nStop->R1\nRear->R2", (0,0,139), 1175, 700)
    Road4 = render_multiline(font_med, "Top->R4\nStop->R1\nStop->R2\nRear->R3", (0,0,139), 1175, 700)

    R1_label = render_label(pygame.font.SysFont("timesnewroman", 30), 'R1', (255,255,255), (50,350))
    R2_label = render_label(pygame.font.SysFont("timesnewroman", 30), 'R2', (255,255,255), (900,50))
    R3_label = render_label(pygame.font.SysFont("timesnewroman", 30), 'R3', (255,255,255), (1450,675))
    R4_label = render_label(pygame.font.SysFont("timesnewroman", 30), 'R4', (255,255,255), (600,950))

    # Create lanes with SpawnConfig and exit checks
    lane_r1_1 = Lane(SpawnConfig(SPAWN_CHANCE_INV := 100, (-100, 425), move_r1_1, H_car_images), exit_r1_1)
    lane_r1_2 = Lane(SpawnConfig(SPAWN_CHANCE_INV, (850, 425), move_r1_2, H_car_images), exit_generic_right)
    lane_r2_1 = Lane(SpawnConfig(SPAWN_CHANCE_INV, (775, 0), move_r2_1, V_car_images), exit_r2_1)
    lane_r2_2 = Lane(SpawnConfig(SPAWN_CHANCE_INV, (775, 600), move_r2_2, V_car_images), exit_generic_bottom)
    lane_r3_1 = Lane(SpawnConfig(SPAWN_CHANCE_INV, (1500, 550), move_r3_1, H1_car_images), exit_r3_1)
    lane_r3_2 = Lane(SpawnConfig(SPAWN_CHANCE_INV, (575, 550), move_r3_2, H1_car_images), exit_generic_left)
    lane_r4_1 = Lane(SpawnConfig(SPAWN_CHANCE_INV, (675, 900), move_r4_1, V1_car_images), exit_r4_1)
    lane_r4_2 = Lane(SpawnConfig(SPAWN_CHANCE_INV, (675, 350), move_r4_2, V1_car_images), exit_generic_top)

    # group all lanes for convenience
    lanes = [lane_r1_1, lane_r1_2, lane_r2_1, lane_r2_2, lane_r3_1, lane_r3_2, lane_r4_1, lane_r4_2]

    # Traffic controller with callback (you can hook logging or UI updates into on_rotate)
    def on_rotate_cb():
        # called whenever the traffic_controller rotates
        pass

    traffic = TrafficController(on_rotate_cb)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Let controller handle the rotate event
            traffic.handle_event(event)

            if event.type == pygame.MOUSEBUTTONUP:
                pos = event.pos
                if Mode_btn[1].collidepoint(pos):
                    traffic.toggle_mode()
                elif traffic.mode == Mode.MANUAL:
                    if Forward[1].collidepoint(pos):
                        traffic.forward()
                    elif Backward[1].collidepoint(pos):
                        traffic.backward()

        # Spawn logic
        for lane in lanes:
            lane.maybe_spawn()

        # Update lanes
        for lane in lanes:
            lane.update()

        # Drawing
        screen.fill((135, 206, 235))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(*HORIZONTAL_ROAD_RECT))
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(*VERTICAL_ROAD_RECT))

        # UI draw
        screen.blit(Forward[0], Forward[1]); screen.blit(Backward[0], Backward[1]); screen.blit(Mode_btn[0], Mode_btn[1])
        screen.blit(Auto_btn[0], Auto_btn[1]) if traffic.mode == Mode.AUTO else screen.blit(Manual_btn[0], Manual_btn[1])
        screen.blit(R1_label[0], R1_label[1]); screen.blit(R2_label[0], R2_label[1]); screen.blit(R3_label[0], R3_label[1]); screen.blit(R4_label[0], R4_label[1])

        # Route overlays & centers
        if traffic.road == "R1":
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(850, 525, 100, 100))
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(750, 305, 100, 100))
            for s, r in zip(*Road1): screen.blit(s, r)
            screen.blit(r1_image, (650, 410))
        elif traffic.road == "R2":
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(650, 625, 100, 100))
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(850, 525, 100, 100))
            for s, r in zip(*Road2): screen.blit(s, r)
            screen.blit(r2_image, (650, 409))
        elif traffic.road == "R3":
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(550, 405, 100, 100))
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(650, 625, 100, 100))
            for s, r in zip(*Road3): screen.blit(s, r)
            screen.blit(r3_image, (650, 409))
        elif traffic.road == "R4":
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(750, 305, 100, 100))
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(550, 405, 100, 100))
            for s, r in zip(*Road4): screen.blit(s, r)
            screen.blit(r4_image, (650, 409))

        # Draw lanes (each lane draws its sprites)
        for lane in lanes:
            lane.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
