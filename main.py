import sys
# Импортируем написанные командой модули
from modules.text_processor import clean_text, get_word_frequency, count_sentences
from modules.menu_ui import print_header, get_user_input, format_results

def main():
    print_header()
    user_text = get_user_input()
    
    if not user_text:
        print("\n Ошибка: введён пустой текст. Завершение работы.")
        sys.exit(1)
        
    freq = get_word_frequency(user_text)
    sentences = count_sentences(user_text)
    format_results(freq, sentences)
    print("\n Анализ завершён успешно.")

if __name__ == "__main__":
    main()
