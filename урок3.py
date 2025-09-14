# class Human:
#     height = 170
#     age = 70
#
# class Student(Human):
#     age= 20
# class Worker(Human):
#     age = 100
#
# nick = Student()
# ann = Worker()
# print(nick.height)
# print(ann.age)
from symtable import Class


# class Grandparent:
#     height = 170
#     age = 70
#     national = "ua"
#
# class parent(Grandparent):
#     age = 40
#
# class child(parent):
#     height = 60
#     def __init__(self):
#         print(self.height)
#         print(self.age)
#         print(self.national)
# nick = child()


# class cl1:
#     var = 20
#     def __init__(self):
#         self.var = 10
#
# class cl2(cl1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
# a = cl2()



# class Grandparent:
#     def about(self):
#         print("Grandparent")
#     def about2(self):
#         print("Grandparent")
#
#
# class parent(Grandparent):
#     def about(self):
#         print("parent")
#
# class child(parent):
#     def __init__(self):
#         super().about()
#         super().about2()
#
# nick = child()





# class pc:
#     def __init__(self):
#         super().__init__()
#         self.memory =128
#
# class display:
#     def __init__(self):
#         super().__init__()
#         self.resolution = "4k"
#
#
# class phone(display,pc):
#     def print_info(self):
#         print(self.resolution)
#         print(self.memory)
#
# iphone = phone()
# iphone.print_info()



class AudioPlayer:
    def play_audio(self):
        print("Playing audio...")



class VideoPlayer:
    def play_video(self):
        print("Playing video...")

class MultimediaPlayer(AudioPlayer, VideoPlayer):
    def play(self):
        print("Playing multimedia...")

chivapchichi_mp4 = MultimediaPlayer()
chivapchichi_mp4.play()