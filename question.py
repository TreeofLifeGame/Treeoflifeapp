import pygame
import smtplib
import os
import time
from getpass import getpass






# email = input("Please enter your Email Address: \n")
# password = getpass("Please enter your password: \n")
#
# # user = auth.create_user_with_email_and_password(email,password)
#
#
#
# print("Success ......")






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
            'text': "When the living body is no longer \nalive, it breaks down naturally",
            'choices': ["True", "False"],
            'answer': 0,
            'bobby': "assets/expression_happy.png"
        },
        {
            'text': "Trees and plants cannot get \nnutrients from the soil",
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
            'bobby': "assets/expression_smiley_teeth_eyes_open.png"
        },
        {
            'text': "Bacteria in the soil damages plants",
            'choices': ["True", "False"],
            'answer': 1,
            'bobby': "assets/expression_smiley_teeth_eyes_closed.png"
        },
        {
            'text': "Cremation is a process of wrapping \nthe body with leaves for burial",
            'choices': ["True", "False"],
            'answer': 1,
            'bobby': "assets/expression_happy.png"
        }
    ],
    3: [
        {
            'text': "Cremation and traditional burial \nwith coffins or caskets are good \nfor planet Earth",
            'choices': ["Yes", "No", "Maybe"],
            'answer': 1,
            'bobby': "assets/expression_excited.png"
        },
        {
            'text': "Toxic chemicals leak into the soil \nfrom harmful burial methods",
            'choices': ["True", "False"],
            'answer': 0,
            'bobby': "assets/expression_happy.png"
        },
        {
            'text': "Planet Earth needs our help to make \nit better",
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
                        self.score += QuizGame(3).points_earned
                        # self.score += QuizGame(2).points_earned
                        # self.score += QuizGame(3).points_earned
                        SignUp()
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

        #Button Background
        next_button = pygame.image.load('assets/blank_btn.png')
        next_button = pygame.transform.scale(next_button, (next_button.get_width()*.3, next_button.get_height()*.4))
        window.blit(next_button, (DISPLAY_WIDTH-80, DISPLAY_HEIGHT-50))

        #Button Text
        font = pygame.font.Font('freesansbold.ttf', 14)
        text_surface = font.render('NEXT', True, '#ffffff')
        window.blit(text_surface,(DISPLAY_WIDTH-65, DISPLAY_HEIGHT-40))



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

                    if next_button.get_rect().move(DISPLAY_WIDTH-80, DISPLAY_HEIGHT-50).collidepoint(pos):
                        print("NEXT!")
                        stopped = True



    def draw(self, question):

        # redraw window
        window.fill(BG_COLOR)
        window.blit(BG_LINES, (0, 0))

        # draw bobby
        bobby = pygame.image.load(question['bobby'])
        bobby = pygame.transform.scale(bobby, (bobby.get_width()*.6, bobby.get_height()*.6))
        window.blit(bobby,(-25,625))

        # draw speech bubble
        ## text
        # font = pygame.font.Font('freesansbold.ttf', 20)
        # text_surface = font.render(question['text'],True,'#000000')
        # text_rect = text_surface.get_rect(bottomleft=(100,600))

        ## Background
        # background = text_rect.copy()
        # background.inflate_ip(20,20)
        # pygame.draw.rect(window, '#ffffff', background, border_radius=10)
        # window.blit(text_surface,text_rect)

        ## Local Score
        font = pygame.font.Font('freesansbold.ttf', 20)
        score_surface = font.render("POINTS EARNED: {}".format(self.points_earned), True, '#FFFFFF')
        score_rect = score_surface.get_rect(topright=(DISPLAY_WIDTH-10, 10))
        window.blit(score_surface, score_rect)

        self.blit_text(question['text'], 100, 600, 24)

        self.buttons = []

        for index, choice in enumerate(question['choices']):
            button_location = (100+((index%2)*160), 400-(80*(index//2)))
            self.buttons.append(Button(text=choice, correct_answer=(index == question['answer']),
                                       location=button_location))

        pygame.display.update()
        self.points_earned += self.get_answer()

    def blit_text(self, text, x, y, line_height):

        lines = text.split('\n')  # 2D array where each row is a list of words.
        font = pygame.font.Font('freesansbold.ttf', line_height-4)

        for index, line in enumerate(lines[::-1]):
            line_surface = font.render(line,True, '#ffffff')
            line_rect = line_surface.get_rect(bottomleft=(x,y-(line_height*index)))
            window.blit(line_surface,line_rect)


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
        self.draw()

    def draw(self):

        # Text
        font = pygame.font.Font('freesansbold.ttf', 20)
        text_surface = font.render(self.text,True,'#ffffff')
        text_rect = text_surface.get_rect(topleft=self.location)
        text_rect = text_rect.move(40, 20)

        # Button background
        background = pygame.image.load('assets/blank_btn.png')
        background = pygame.transform.scale(background,(background.get_width()*.7, background.get_height()*.7))
        self.rect = background.get_rect()
        self.rect = self.rect.move(self.location)
        window.blit(background,self.location)

        window.blit(text_surface,text_rect)
        print([background.get_rect(), self.correct_answer])


class SignUp(object):

    # Sign Up Page here

    def __init__(self):
        self.text = ''
        self.draw()

    def draw(self):
        window.fill(BG_COLOR)
        window.blit(BG_LINES, (0, 0))

        #Sign Up Button
        sign_up_button = pygame.image.load('assets/sign_up_btn.png')
        sign_up_button = pygame.transform.scale(sign_up_button,(sign_up_button.get_width()*.5, sign_up_button.get_height()*.5))
        sign_up_button_rect = sign_up_button.get_rect(center= (DISPLAY_WIDTH/2, (DISPLAY_HEIGHT/2)+100))

        #Log In Button
        log_in_button = pygame.image.load('assets/log_in_btn.png')
        log_in_button = pygame.transform.scale(log_in_button, (log_in_button.get_width()*.5, log_in_button.get_height()*.5))
        log_in_button_rect = log_in_button.get_rect(center=(DISPLAY_WIDTH / 2, (DISPLAY_HEIGHT / 2) + 160))

        #About Button
        about_button = pygame.image.load('assets/About_btn.png')
        about_button = pygame.transform.scale(about_button, (about_button.get_width()*.5, about_button.get_height()*.5))
        about_button_rect = about_button.get_rect(center=(DISPLAY_WIDTH / 2, (DISPLAY_HEIGHT / 2) + 220))

        #Bobby Image
        bobby_image = pygame.image.load('assets/sign_up_prompt.png')
        bobby_image = pygame.transform.scale(bobby_image, (bobby_image.get_width()*.66, bobby_image.get_height()*.66))
        bobby_image_rect = bobby_image.get_rect(midbottom=(DISPLAY_WIDTH / 2, (DISPLAY_HEIGHT / 2)+110))

        #Menu Image
        menu_image = pygame.image.load('assets/menu_btn.png')
        menu_image = pygame.transform.scale(menu_image, (menu_image.get_width()*.5, menu_image.get_height()*.5))
        menu_image_rect = menu_image.get_rect(topleft=(20, 20))

        #little Tree Image
        little_tree_image = pygame.image.load('assets/sparkly_tree.png')
        little_tree_image = pygame.transform.scale(little_tree_image, (little_tree_image.get_width()*.175, little_tree_image.get_height()*.175))
        little_tree_image_rect = little_tree_image.get_rect(topright=(DISPLAY_WIDTH-10, 10))
        print("About Button Rect:")
        print("\t{}".format(about_button_rect))
        print("Login Button Rect:")
        print("\t{}".format(log_in_button_rect))
        print("Signup Button Rect:")
        print("\t{}".format(sign_up_button_rect))


        window.blit(little_tree_image, little_tree_image_rect)
        window.blit(menu_image, menu_image_rect)
        window.blit(bobby_image, bobby_image_rect)
        window.blit(sign_up_button, sign_up_button_rect)
        window.blit(log_in_button, log_in_button_rect)
        window.blit(about_button, about_button_rect)

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
                    # print(event)
                    # print(pos)
                    if sign_up_button.get_rect().move(DISPLAY_WIDTH/2-(sign_up_button.get_width()*.5),
                                            ((DISPLAY_HEIGHT/2)+100)-(sign_up_button.get_height()*.5)).collidepoint(pos):
                        self.draw_sign_up()
                        stopped = True
                        print("Sign Up!")
                    elif log_in_button.get_rect().move(DISPLAY_WIDTH/2-(log_in_button.get_width()*.5),
                                                       ((DISPLAY_HEIGHT/2)+160)-(log_in_button.get_height()*.5)).collidepoint(pos):

                        self.draw_log_in()
                        print("Log In!")
                        stopped = True
                    elif about_button.get_rect().move(DISPLAY_WIDTH/2-(about_button.get_width()*.5),
                                                      ((DISPLAY_HEIGHT/2)+220)-(about_button.get_height()*.5)).collidepoint(pos):
                        print("About")
                        stopped = True
                    elif menu_image.get_rect().move((20, 20)).collidepoint(pos):
                        print("Menu")
                        stopped = True


    def draw_sign_up(self):
        window.fill(BG_COLOR)
        window.blit(BG_LINES, (0, 0))


        # Text Box
        # text_box = pygame.Surface(((DISPLAY_WIDTH//3)*2-60, 30))
        # text_box_rect = pygame
        # text_box.fill('#1E6670')
        # text_box_rect.move_ip(5.0,0.0)


        #Bobby_image
        bobby_image = pygame.image.load('assets/expression_excited2.png')
        bobby_image = pygame.transform.scale(bobby_image,
                                             (bobby_image.get_width() * .66, bobby_image.get_height() * .66))
        bobby_image_rect = bobby_image.get_rect(midbottom=(DISPLAY_WIDTH / 2, (DISPLAY_HEIGHT / 2) - 50))

        # Draw Background
        background = pygame.Surface(((DISPLAY_WIDTH//3)*2,DISPLAY_WIDTH//8))
        background_rect = background.get_rect(topleft=bobby_image_rect.bottomleft)
        background_rect.move_ip(-40.0,-5.0)
        # background.set_alpha(128)
        background.fill('#FFFCF5')

        #Text Surface
        text_font = pygame.font.Font('freesansbold.ttf', 20)
        text_surface = text_font.render(self.text, True, '#FFFFFF', '#1E6670')
        text_rect = text_surface.get_rect(topleft=bobby_image_rect.bottomleft)
        text_rect.move_ip(0,25.0)

        # Message Face
        message_font = pygame.font.Font('freesansbold.ttf', 20)
        message_surface = message_font.render("Enter your email below:", True, '#1E6670')
        # message_rect = pygame.Rect((text_rect.x,text_rect.y + 100),(text_rect.width,text_rect.height))
        message_rect = text_rect.copy()
        message_rect.move_ip(0,-25.0)







        window.blit(bobby_image,bobby_image_rect)
        window.blit(background, background_rect)
        # window.blit(text_box,text_box_rect)
        window.blit(text_surface,text_rect)
        window.blit(message_surface,message_rect)

        pygame.display.update()
        stopped = False
        while not stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    print(event)
                    if event.key == pygame.K_ESCAPE:
                        self.text = ''
                        pygame.QUIT
                        return
                    elif event.key == 8:
                        self.text = self.text[:-1]
                        text_surface = text_font.render(self.text, True, '#FFFFFF', '#1E6670')
                        window.blit(background, background_rect)
                        window.blit(text_surface, text_rect)
                        window.blit(message_surface, message_rect)
                        pygame.display.update()

                    elif event.key == pygame.K_RETURN:
                        # send out email
                        content = "Hi there,\n\tThank you for signing up to the\
Tree Of Life App! We hope you enjoy learning about ways\
to preserve our environment even after we are gone."
                        print(content)
                        s_user = None # Company Email here
                        s_pass = None # Company Email password here
                        print("Success......") # TODO: Switch to token authentication
                        print("Sending email to: {}\nSender:\n\tUser: {}\n\tPass: {}".\
                              format(self.text,s_user,s_pass))

                        with smtplib.SMTP(host="smtp.gmail.com", port=587, timeout=10) as connection:
                            connection.starttls()
                            connection.login(s_user, s_pass)
                            connection.sendmail(from_addr=s_user,
                                                to_addrs=self.text,
                                                msg=f"Subject:Thanks for Signing Up to TreeOfLife! \n\n{content}")
                        self.text = ''
                        message_surface = message_font.render("Thank you for signing up!", True, '#1E6670')
                        window.blit(background, background_rect)
                        window.blit(message_surface, message_rect)
                        pygame.display.update()
                        stopped = False

                        while not stopped:
                            for subevent in pygame.event.get():
                                if subevent.type == pygame.KEYDOWN:
                                    if subevent.key == pygame.K_ESCAPE:
                                        pygame.QUIT
                                        stopped = True
                                elif subevent.type == pygame.QUIT:
                                    pygame.QUIT
                                    stopped = True
                        return
                    elif event.type == pygame.KEYDOWN:
                        self.text += event.unicode
                        print(self.text)
                        text_surface = text_font.render(self.text, True, '#FFFFFF', '#1E6670')
                        window.blit(text_surface, text_rect)
                        pygame.display.update()

    def draw_log_in(self):
        window.fill(BG_COLOR)
        window.blit(BG_LINES, (0, 0))

        # Draw Background
        background = pygame.Surface(((DISPLAY_WIDTH // 3) * 2, (DISPLAY_WIDTH // 8) * 5))
        background_rect = background.get_rect(center=(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2))
        background.set_alpha(128)
        background.fill('#FFFCF5')

        # User Text Box
        user_text_box = pygame.Surface(((DISPLAY_WIDTH // 3) * 2 - 60, 30))
        user_text_box_rect = background_rect.copy()
        # text_box_rect.size()
        user_text_box_rect.move_ip(5.0, 0.0)

        user_font = pygame.font.Font('freesansbold.ttf', 20)
        user_text_surface = user_font.render(self.text, True, '#000000', '#FFFFFF')
        user_text_rect = user_text_box_rect.copy()
        user_text_rect.inflate_ip(-10, -10)

        # Pass Text Box
        pass_text_box = pygame.Surface(((DISPLAY_WIDTH // 3) * 2 - 60, 30))
        pass_text_box_rect = background_rect.copy()
        # text_box_rect.size()
        pass_text_box_rect.move_ip(5.0, 50.0)

        pass_font = pygame.font.Font('freesansbold.ttf', 20)
        pass_text_surface = pass_font.render(self.text, True, '#000000', '#FFFFFF')
        pass_text_rect = pass_text_box_rect.copy()
        pass_text_rect.inflate_ip(-10, -10)

        window.blit(background, background_rect)
        window.blit(user_text_box, user_text_box_rect)
        window.blit(user_text_surface, user_text_rect)
        window.blit(pass_text_box, pass_text_box_rect)
        window.blit(pass_text_surface, pass_text_rect)

        pygame.display.update()
        stopped = False
        while not stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    print(event)
                    if event.key == pygame.K_ESCAPE:
                        text_box = ''
                        pygame.QUIT
                        return
                    elif event.key == 8:
                        self.text = self.text[:-1]
                        user_text_surface = font.render(self.text, True, '#000000', '#FFFFFF')
                        pass_text_surface = font.render(self.text, True, '#000000', '#FFFFFF')
                        window.blit(user_text_box, user_text_box_rect)
                        window.blit(pass_text_box, pass_text_box_rect)
                        window.blit(user_text_surface, user_text_rect)
                        window.blit(pass_text_surface, pass_text_rect)
                        pygame.display.update()

    def draw_about(self):
        window.fill(BG_COLOR)
        window.blit(BG_LINES, (0, 0))
        pass




















if __name__ == '__main__':
    window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    game = MainRun(DISPLAY_WIDTH, DISPLAY_HEIGHT)


