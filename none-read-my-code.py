from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    task = simpledialog.askstring('Tarefa', 'Você deseja criptografar ou descriptografar?')
    return task

def get_message():
    message = simpledialog.askstring('Mensagem', 'Digite a mensagem secreta: ')
    return message

root = Tk()
while True:
    task = get_task()
    if task == 'criptografar':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('O texto cifrado da mensagem secreta é:', encrypted)
        
    elif task == 'decifrar':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('O texto da mensagem secreta é:', decrypted)
    else:
        break
root.mainloop()
