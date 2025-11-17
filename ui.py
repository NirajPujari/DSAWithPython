import pygame

def create_button(font, text, center_pos, size, bg_color, text_color):
    w, h = size
    surf = pygame.Surface((w, h), pygame.SRCALPHA)
    rect = surf.get_rect(center=center_pos)
    surf.fill(bg_color)
    text_s = font.render(text, True, text_color)
    surf.blit(text_s, text_s.get_rect(center=surf.get_rect().center))
    return surf, rect

def render_multiline(font, text, color, center_x, start_y, line_spacing=40):
    lines = text.split('\n')
    surfaces = []
    rects = []
    for i, line in enumerate(lines):
        s = font.render(line, True, color)
        r = s.get_rect(center=(center_x, start_y + i * line_spacing))
        surfaces.append(s)
        rects.append(r)
    return surfaces, rects

def render_label(font, text, color, pos):
    surf = font.render(text, True, color)
    rect = surf.get_rect(center=pos)
    return surf, rect
