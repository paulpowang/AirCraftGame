import pygame

pygame.init()


object_rect = pygame.Rect(100, 500, 10, 50)
print("x-coordinate: %d, y-coordinate: %d" %
      (object_rect.x, object_rect.y))
print("width: %d, height: %d" %
      (object_rect.width, object_rect.height))
print("width: %d, height: %d" % object_rect.size)



pygame.quit()