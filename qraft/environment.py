
from .all_imports import *

class Scene:

    def __init__(self, name, width, height, background_color=(0.2, 0.2, 0.3, 1.0), FPS=60):
        self.name = name
        self.width = width
        self.height = height
        self.background_color = background_color

        self.window = pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
        pygame.display.set_caption('Qraft')
        pygame.display.set_icon(pygame.image.load('qraft/assets/icon.png'))

        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)

        self.objects = []

    def update(self):
        glClearColor(*self.background_color)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    
    def render(self, camera, light_vector):
        position = -camera.position.morphed(*camera.unit_vectors)
        unit_vectors = camera.unit_vectors
        relative_light_vector = light_vector.morphed(*camera.unit_vectors)

        glBegin(GL_TRIANGLES)
        [obj.render(position, unit_vectors, relative_light_vector) for obj in self.objects]
        glEnd()

    def set_FOV(self, FOV):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(FOV, self.width/self.height, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)


class Camera:

    def __init__(self, position, unit_vectors, field_of_view):
        self.position = position
        self.velocity = Q([0,0,0])
        self.unit_vectors = unit_vectors
        self.field_of_view = field_of_view
    
    def translate_rel(self, offset):
        self.velocity += offset.demorphed(*self.unit_vectors)

    def translate_abs(self, offset):
        self.position += offset
    
    def rotate(self, axis, angle):
        self.unit_vectors.rotate(axis, angle)

    def update(self, mouse, keyboard):

        self.rotate(Q([0, 1, 0]), mouse.delta_position[0]/500)
        self.rotate(Q([1, 0, 0]), mouse.delta_position[1]/500)
        
        if keyboard.state[pygame.K_w]: self.translate_rel(Q([0, 0, -1])*0.08)
        if keyboard.state[pygame.K_s]: self.translate_rel(Q([0, 0, 1])*0.08)
        if keyboard.state[pygame.K_a]: self.translate_rel(Q([-1, 0, 0])*0.08)
        if keyboard.state[pygame.K_d]: self.translate_rel(Q([1, 0, 0])*0.08)
        if keyboard.state[pygame.K_SPACE]: self.translate_rel(Q([0, 1, 0])*0.08)
        if keyboard.state[pygame.K_LSHIFT]: self.translate_rel(Q([0, -1, 0])*0.08)

        self.position += self.velocity / 60


class Mouse:
    
    def __init__(self, width=600, height=400):
        self.half_width, self.half_height = width // 2, height // 2

        self.pressed = pygame.mouse.get_pressed(5)
        self.focused = False
        self.update()
    
    def update(self):
        
        new_pressed = pygame.mouse.get_pressed(5)
        self.downclicks = tuple((not self.pressed[i] and new_pressed[i] for i in range(5)))
        self.upclicks = tuple((self.pressed[i] and not new_pressed[i] for i in range(5)))
        self.pressed = new_pressed

        if self.downclicks[1]:
            self.focused = not self.focused
            pygame.mouse.get_rel()
            if self.focused: self.hide()
            else:            self.show()

        if self.focused:
            temp_position = pygame.mouse.get_pos()
            self.delta_position = temp_position[0]-self.position[0], temp_position[1]-self.position[1]
            pygame.mouse.set_pos((self.half_width, self.half_height))
            self.position = (self.half_width, self.half_height)

        elif not self.focused:
            self.position = pygame.mouse.get_pos()
            self.delta_position = pygame.mouse.get_rel()

    def hide(self):
        pygame.mouse.set_visible(False)

    def show(self):
        pygame.mouse.set_visible(True)


class Keyboard:

    def __init__(self):
        self.state = pygame.key.get_pressed()
    
    def update(self):
        new_state = pygame.key.get_pressed()
        self.downs = pygame.key.ScancodeWrapper((now and not then for (now, then) in zip(new_state, self.state)))
        self.ups = pygame.key.ScancodeWrapper((not now and then for (now, then) in zip(new_state, self.state)))
        self.state = new_state
