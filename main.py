

import menu
import pb
import os

clear = lambda : os.system('clear')


def show_menu():
    
    result = menu.print()
    clear()

    match result:
        case 1:
            pb.open_file()
        case 2:
            pb.save_file()
        case 3:
            pb.print_file()
        case 4:
            pb.create_contact()
        case 5: 
            pb.edit_contact()
        case 6:
            pb.find_contact()
        case 7:
            pb.del_contact()
        case 8:
            exit()

    show_menu()


clear()
show_menu()