import pygame

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #800*600 boyutunda 
pygame.display.set_caption("2 Kişilik Ping Pong") # başlık

# Renkler RGB
BEYAZ= (255, 255, 255)
SIYAH = (0, 0, 0)
KIRMIZI = (255, 0, 0)

# Oyun değişkenleri
raket_width, raket_height = 10, 100
ball_size = 15

# Raket pozisyonları
raket1 = pygame.Rect(20, HEIGHT//2 - raket_height//2, raket_width, raket_height)
raket2 = pygame.Rect(WIDTH - 30, HEIGHT//2 - raket_height//2, raket_width, raket_height)
ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)

# Hareket hızları
raket_speed = 6
ball_speed_x, ball_speed_y = 4, 4

# Skor
score1, score2 = 0, 0
font = pygame.font.Font(None, 50) # yazı tanımlamdı büyüklüğü 50

# Oyun döngüsü
running = True
while running:
    pygame.time.delay(20)
    screen.fill(SIYAH) # fill=doldurmak arka plan rengi siyah oldu
    
    # Eventleri kontrol et
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # X işaretine tıklandımı
            running = False # döngü sonlanacak oyun kapanacak
    
    # Tuş kontrolleri
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and raket1.top > 0: # yukayı
        raket1.y -= raket_speed
    if keys[pygame.K_s] and raket1.bottom < HEIGHT: #aşagı
        raket1.y += raket_speed
    if keys[pygame.K_UP] and raket2.top > 0: #yukarı
        raket2.y -= raket_speed
    if keys[pygame.K_DOWN] and raket2.bottom < HEIGHT: # aşağı
        raket2.y += raket_speed
    
    # Top hareketi
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Üst ve alt kenara çarpma
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1 
    
    # Raketlere çarpma
    if ball.colliderect(raket1) or ball.colliderect(raket2):
        ball_speed_x *= -1
    
    # Gol durumu
    if ball.left <= 0:
        score2 += 1 # score2 1 artacak
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        score1 += 1 # score1 1 artacak
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed_x *= -1
    
    # Skor çizimi
    text = font.render(f"{score1} - {score2}", True, BEYAZ)
    screen.blit(text, (WIDTH//2 - 30, 20))
    
    # Raket ve top çizimi
    pygame.draw.rect(screen, BEYAZ, raket1) # beyaz dikdörtgen cizildi
    pygame.draw.rect(screen, BEYAZ, raket2) # siyah dikdörtgen çizildi
    pygame.draw.ellipse(screen, KIRMIZI, ball) # kırmızı top çziizldi
    pygame.draw.aaline(screen, BEYAZ, (WIDTH//2, 0), (WIDTH//2, HEIGHT)) # ortadaki beyaz çizgi çizildi
    
    pygame.display.flip()

pygame.quit()
