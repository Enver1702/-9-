import model
import text
import view


def start():
 while True :
   select = view.menu()
   match select:
      case 1:
          if model.open_file():
              view.print_massage(text.load_successful)
          else:
              view.print_massage(text.error_load)
      case 2:
          if model.save_file():
              view.print_massage(text.save_successful)
          else:
              view.print_massage(text.error_save)
      case 3:
          view.show_contacts(model.phone_book,text.empty_book)
      case 4:
          new = view.add_contact()
          model.add_contact(new)
          view.print_massage(text.add_successful(new.get('name')))
      case 5:
          word = view.search_word()
          result = model.search_word()
          view.show_contacts(result, text.empty_search(word))
      case 6:
          if model.edit_contacts():
              view.print_massage(text.edit_contacts)
          else:
              view.print_massage(text.error_edit)
      case 7:
          if model.delete_contacts():
              view.print_massage(text.delete_contacts)
          else:
              view.print_massage(text.error_delete)
      case 8:
          view.print_massage(0)
          break
