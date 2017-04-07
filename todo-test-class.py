import sys


class Database():
    """Open database for further working process"""
    def __init__(self, line_list = []):
        # super(Database, self).__init__()
        self.line_list = line_list


    def open_db(self, openfile = '', open_arg = ''):
        self.openfile = openfile
        self.open_arg = open_arg
        number = 1

        file = open(self.openfile, self.open_arg)
        for line in file:
            x = line.rstrip().split(";")
            x.insert(0, number)
            # print(x)
            line_list = self.line_list.append(x)
            number += 1   

        return self.line_list

    

opendb_var = Database()
print(opendb_var.open_db('todo-db.txt','r'))













class Controller():
    """Controller for listening command line arguments and sending parameters for Opendb class"""
    def __init__(self, arg):
        # super(Controller, self).__init__()
        self.arg = arg

    def help_txt(self):

        file = open('help.txt','r')
        helptxt = file.read()
        print(helptxt)
        


    def arg_reader(self):

        if len(sys.argv) == 1:
            self.help_txt()
        else:
            # # return sys.argv[1:]
            # if ( sys.argv[1] == '-l' ):
            #     self.view()
            #     # todo_list()
            # elif ( sys.argv[1] == '-a' ):
            #     self.add_line()
            pass








# def view():

#     file = open('todo-db.txt','r')
#     number = 1
#     for line in file:
#         line_list = line.rstrip().split(";")
#         if line_list[0] == '1':
#             print(number,'[X] ',line_list[1])
#         else:
#             print(number,'[ ] ',line_list[1])
#         number += 1
#     file.close()