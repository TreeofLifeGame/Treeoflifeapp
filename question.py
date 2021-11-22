import pygame
pygame.init()

# Window Information
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 800
BG_COLOR = pygame.Color('#aad2c5')
BG_LINES = pygame.image.load('assets/background_lines_decor.png')
BG_LINES = pygame.transform.scale(BG_LINES, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
# Clock
clock = pygame.time.Clock()

# Load other things such as images and sound files here
# image = pygame.image.load("foo.png").convert  # Use convert_alpha() for images with transparency



question_bank = {
    1: [
        {
            'text': "All living beings live on forever",
            'choices': ["True", "False"],
            'answer': 1,
            'bobby': "assets/expression_excited.png"
        },
        {
            'text': "When the living body is no longer alive, it breaks down naturally",
            'choices': ["True", "False"],
            'answer': 0,
            'bobby': "assets/expression_happy.png"
        },
        {
            'text': "Trees and plants cannot get nutrients from the soil",
            'choices': ["True", "False"],
            'answer': 1,
            'bobby': "assets/expression_smiley_teeth_eyes_closed.png"
        },
    ],
    2: [
        {
            'text': "Where do trees and plants get nutrients from?",
            'choices': ["Soil", "Coffins", "Chemicals"],
            'answer': 0,
            'bobby': "assets/expression_smiley_teeth    _eyes_open.png"
        },
        {
            'text': "Bacteria in the soil damages plants",
            'choices': ["True", "False"],
            'answer': 1,
            'bobby': "assets/expression_smiley_teeth_eyes_closed.png"
        },
        {
            'text': "Cremation is a process of wrapping the body with leaves for burial",
            'choices': ["True", "False"],
            'answer': 1,
            'bobby': "assets/expression_happy.png"
        }
    ],
    3: [
        {
            'text': "Cremation and traditional burial with coffins or caskets are good for planet Earth",
            'choices': ["Yes", "No", "Maybe"],
            'answer': 1,
            'bobby': "assets/expression_excited.png"
        },
        {
            'text': "Toxic chemicals leak into the soil from harmful burial methods",
            'choices': ["True", "False"],
            'answer': 0,
            'bobby': "assets/expression_happy.png"
        },
        {
            'text': "Planet Earth needs our help to make it better",
            'choices': ["Yes", "No"],
            'answer': 0,
            'bobby': "assets/expression_wink.png"
        },
    ],
}


# Main Class
class MainRun(object):
    def __init__(self, display_width, display_height):
        self.width = display_width
        self.height = display_height
        self.score = 0

        self.Main()

    def Main(self):
        # Put all variables up here
        stopped = False

        while not stopped:
            window.fill(BG_COLOR)  # Tuple for filling display... Current is white
            window.blit(BG_LINES, (0, 0))
            self.UpdateScore()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        stopped = True
                    else:
                        self.score += QuizGame(1).points_earned
                        self.score += QuizGame(2).points_earned
                        self.score += QuizGame(3).points_earned


            pygame.display.update()
            clock.tick(60)

    def UpdateScore(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        score_surface = font.render("SCORE: {}".format(self.score), True, '#FFFFFF')
        score_rect = score_surface.get_rect(topright=(self.width-10, 10))
        window.blit(score_surface, score_rect)


class QuizGame(object):
    def __init__(self, level):
        self.level = level
        self.level_data = question_bank[self.level]
        self.points_earned = 0
        self.buttons = []
        for question in self.level_data:
            self.draw(question)
        self.next_button()

        return

    def next_button(self):
        next_button = pygame.image.load('assets/blank_btn.png')
        next_button = pygame.transform.scale(next_button, (50, 50))
        window.blit(next_button, (DISPLAY_WIDTH-50, DISPLAY_HEIGHT-50))
        pygame.display.update()

        stopped = False
        while not stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()

                    if next_button.get_rect().move(DISPLAY_WIDTH-50, DISPLAY_HEIGHT-50).collidepoint(pos):
                        print("NEXT!")
                        stopped = True



    def draw(self, question):

        # redraw window
        window.fill(BG_COLOR)
        window.blit(BG_LINES, (0, 0))

        # draw bobby
        bobby = pygame.image.load(question['bobby'])
        bobby = pygame.transform.scale(bobby, (230,200))
        window.blit(bobby,(-25,625))

        # draw speech bubble
        ## text
        font = pygame.font.Font('freesansbold.ttf', 20)
        text_surface = font.render(question['text'],True,'#000000')
        text_rect = text_surface.get_rect(bottomleft=(100,600))
        ## Background
        background = text_rect.copy()
        background.inflate_ip(20,20)
        pygame.draw.rect(window, '#ffffff', background, border_radius=10)
        window.blit(text_surface,text_rect)
        ## Local Score
        font = pygame.font.Font('freesansbold.ttf', 20)
        score_surface = font.render("POINTS EARNED: {}".format(self.points_earned), True, '#FFFFFF')
        score_rect = score_surface.get_rect(topright=(DISPLAY_WIDTH-10, 10))
        window.blit(score_surface, score_rect)

        self.buttons = []

        for index, choice in enumerate(question['choices']):
            button_location = (100+((index%2)*160), 400-(80*(index//2)))
            self.buttons.append(Button(text=choice, correct_answer=(index == question['answer']),
                                       location=button_location))

        pygame.display.update()
        self.points_earned += self.get_answer()


    def get_answer(self):
        #Score

        stopped = False

        while not stopped:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.rect.collidepoint(pos):
                            print("CLICKED ON {}".format(button.text))
                            if button.correct_answer:
                                return 100
                            else:
                                return -25

            # print("GAME LOOP: LEVEL {}".format(self.level))


class Button(object):

    def __init__(self, text, correct_answer, location):
        self.text = text
        self.correct_answer = correct_answer # boolean
        self.location = location
        self.draw(self.location)

    def draw(self, location):

        # Text
        font = pygame.font.Font('freesansbold.ttf', 20)
        text_surface = font.render(self.text,True,'#ffffff')
        text_rect = text_surface.get_rect(topleft=self.location)
        text_rect = text_rect.move(40, 20)

        # Button background
        background = pygame.image.load('assets/blank_btn.png')
        background = pygame.transform.scale(background,(150,70))
        self.rect = background.get_rect()
        self.rect = self.rect.move(self.location)
        window.blit(background,self.location)

        window.blit(text_surface,text_rect)
        print([background.get_rect(), self.correct_answer])


class SignUp(object):
    # Sign Up Page here
    pass
















if __name__ == '__main__':
    window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    game = MainRun(DISPLAY_WIDTH, DISPLAY_HEIGHT)

# import pygame
# from pygame.locals import *
#
# BG_COLOR = pygame.Color('#aad2c5')
# PADDING = 50
# SCREEN_SIZE = (480,800)
# QUESTION_BANK = {
#     "1": ["YES", "NO", "MAYBE", 0],
#     "2": ["YES", "NO", 1],
# }
#
#
# class Screen(object):
#     def __init__(self,bg_color,screen_size):
#         self.bg_color = bg_color
#         self.screen_size = screen_size
#         self.bobby_location = [-25,625]
#         self.question_location = [60, 400]
#
#     def draw_bg(self):
#         pygame.init()
#         self.screen = pygame.display.set_mode(self.screen_size)
#         self.screen.fill(self.bg_color)
#         bg_lines = pygame.image.load('assets/background_lines_decor.png')
#         bg_lines = pygame.transform.scale(bg_lines, self.screen_size)
#         self.screen.blit(bg_lines, [0, 0])
#         # pygame.display.flip()
#         # return
#
#     def draw_bobby(self):
#         bobby = pygame.image.load('assets/expression_smiley_teeth_eyes_open.png')
#         bobby = pygame.transform.scale(bobby, (230,200))
#         self.screen.blit(bobby,self.bobby_location)
#         # pygame.display.flip()
#         # return
#
#     def draw_question(self,question_id):
#
#         choices = QUESTION_BANK[question_id]
#         # print(choices)
#
#         #create question bubble
#         question_bubble = pygame.image.load('assets/conversation_bubble.png')
#         question_bubble = pygame.transform.scale(question_bubble, (450,350))
#         self.screen.blit(question_bubble, self.question_location)
#
#         #draw question text
#         question_font = pygame.font.Font('freesansbold.ttf', 20)
#         question_text = question_font.render('Test Question?', True, '#000000', '#ffffff')
#         self.screen.blit(question_text,[location + PADDING for location in self.question_location])
#
#         #load button
#         answer_button = pygame.image.load('assets/blank_btn.png')
#         answer_button = pygame.transform.scale(answer_button,(150,70))
#
#         #dynamically generate button and text from word bank
#         for index, choice in enumerate(choices[:len(choices)-1]):
#             button_location = (100+((index%2)*160),250+(80*(index//2)))
#             text_location = (120 + ((index % 2) * 160), 270 + (80 * (index // 2)))
#             self.screen.blit(answer_button, button_location)
#             answer_font = pygame.font.Font('freesansbold.ttf', 18)
#             answer_text = answer_font.render(choice.encode('utf-8'), True, '#ffffff', '#1e6670')
#             text_rect = answer_text.get_rect()
#             text_rect.left = 150
#             self.screen.blit(answer_text, text_location)
#             # self.screen.blit(answer_text, (100+((index%2)*160),250+(80*(index//2))))
#             # pygame.draw.rect(self.screen, '#fffcf0', pygame.Rect(100+(index*160),250,150,50), 5, 3)
#             # return 100
#             # pygame.display.flip()
#             # return int(choices[-1])
#
#     # def get_answer(self,event):
#     #     if event.type == pygame.MOUSEBUTTONDOWN:
#     #         pos = pygame.mouse.get_pos()
#             # if answer
#
#
#
#
#
#
#
#
#
# #
# # Class Trivia(object):
# #     def __init__(self, filename):
# #         self.data = []
# #         self.current = 0
#
#
# my_q = Screen(BG_COLOR, SCREEN_SIZE)
#
#
# while 1:
#
#     my_q.draw_bg()
#     my_q.draw_bobby()
#     answer = my_q.draw_question("1")
#     # select = input("Select a choice: ")
#     # if int(select) == answer:
#     #     print("RIGHT")
#     #     break
#     # else:
#     #     print("WRONG")
#
#
