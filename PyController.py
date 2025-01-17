import pygame, pyautogui

# Initialize Pygame and joystick module
pygame.init()
pygame.joystick.init()
# Connect to the first joystick
if pygame.joystick.get_count() == 0:
    print("No joystick found.")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Connected to {joystick.get_name()}")

sensitivity = 50#int(input("Set sensitivity: "))
clock = pygame.time.Clock()
def move_mouse(x_movement, y_movement):
    # Get the current mouse position
    current_x, current_y = pyautogui.position()
    if abs(x_movement) < 0.6 and abs(y_movement) < 0.6:
        return 
    
    new_x = current_x + (x_movement * sensitivity)
    new_y = current_y + (y_movement * sensitivity)

    pyautogui.moveTo(new_x, new_y)

# Main loop to read controller input
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                button = event.button
                print(f"Button {button} pressed")
                pyautogui.click()
            elif event.type == pygame.JOYBUTTONUP:
                button = event.button
                print(f"Button {button} released")
            pygame.event.pump()
            
            x_axis = joystick.get_axis(0)  # Usually the horizontal axis
            y_axis = joystick.get_axis(1)  # Usually the vertical axis
            
            # Move the mouse based on joystick input
            move_mouse(x_axis, y_axis)
            
        clock.tick(178)
except KeyboardInterrupt:
    print("Exiting...")

# Cleanup
pygame.quit()
