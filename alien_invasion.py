import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.get_dims()))
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(screen, 'Play')
    stats = GameStats(settings)
    sb = Scoreboard(settings, screen, stats)
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings, screen, ship, aliens)
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)
            bullets.update()
        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
