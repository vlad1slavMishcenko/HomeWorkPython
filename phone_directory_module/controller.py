import text
import  view
import model

def start():
    pb = model.PhoneBook()
    while True:
        select = view.menu()
        match select:
            case 1:
                if pb.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if pb.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contact(pb.get(), text.empty_book)
            case 4:
                new = view.add_contact()
                if new:
                    pb.add_contact(new)
                    view.print_message(text.add_successful(new.get('name')))

            case 5:
                word = view.search_word()
                result = pb.search(word)
                view.show_contact(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = pb.search(word)
                view.show_contact(result, text.empty_search(word))
                if result:
                    id_contact = view.del_contact()
                    result = pb.update(id_contact)
                    view.update_contact(result)

            case 7:
                word = view.search_word()
                result = pb.search(word)

                view.show_contact(result, text.empty_search(word))
                if result:
                    id_contact = view.del_contact()
                    res = pb.remuve(id_contact)
                    if res:
                        view.print_message(text.remuve_contact(res.get('name')))
                    else:
                        view.print_message(text.error_id)
            case 8:
                if pb.chek_on_exit():
                    answer = view.view_input(text.change_confirm)
                    if answer != 'n':
                        pb.save_file()
                view.print_message(text.good_bye)
                break