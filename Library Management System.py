import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pickle

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrower = None

    def __str__(self):
        status = f"Borrowed by {self.borrower}" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    def get_status(self):
        return "Available" if not self.is_borrowed else f"Borrowed by {self.borrower}"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            book.borrower = self.name
            self.borrowed_books.append(book.title)
        else:
            messagebox.showerror("Error", f"The book '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book.is_borrowed and book.borrower == self.name:
            book.is_borrowed = False
            book.borrower = None
            self.borrowed_books.remove(book.title)
        else:
            messagebox.showerror("Error", f"The book '{book.title}' was not borrowed by {self.name}.")

    def __str__(self):
        return f"Member: {self.name}, Borrowed books: {', '.join(self.borrowed_books) if self.borrowed_books else 'None'}"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.load_data()

    def initialize_library(self):
        # Predefined collection of 100 books
        books_data = [
            ("The Great Gatsby", "F. Scott Fitzgerald"),
            ("To Kill a Mockingbird", "Harper Lee"),
            ("1984", "George Orwell"),
            ("Brave New World", "Aldous Huxley"),
            ("The Catcher in the Rye", "J.D. Salinger"),
            ("Lord of the Flies", "William Golding"),
            ("Animal Farm", "George Orwell"),
            ("Pride and Prejudice", "Jane Austen"),
            ("Jane Eyre", "Charlotte Brontë"),
            ("Wuthering Heights", "Emily Brontë"),
            ("The Lord of the Rings", "J.R.R. Tolkien"),
            ("The Hobbit", "J.R.R. Tolkien"),
            ("Fahrenheit 451", "Ray Bradbury"),
            ("Moby Dick", "Herman Melville"),
            ("The Odyssey", "Homer"),
            ("Crime and Punishment", "Fyodor Dostoevsky"),
            ("The Brothers Karamazov", "Fyodor Dostoevsky"),
            ("War and Peace", "Leo Tolstoy"),
            ("Anna Karenina", "Leo Tolstoy"),
            ("Les Misérables", "Victor Hugo"),
            ("The Count of Monte Cristo", "Alexandre Dumas"),
            ("The Three Musketeers", "Alexandre Dumas"),
            ("Don Quixote", "Miguel de Cervantes"),
            ("The Picture of Dorian Gray", "Oscar Wilde"),
            ("Dracula", "Bram Stoker"),
            ("Frankenstein", "Mary Shelley"),
            ("One Hundred Years of Solitude", "Gabriel García Márquez"),
            ("The Divine Comedy", "Dante Alighieri"),
            ("The Iliad", "Homer"),
            ("The Bell Jar", "Sylvia Plath"),
            ("Catch-22", "Joseph Heller"),
            ("Slaughterhouse-Five", "Kurt Vonnegut"),
            ("The Shining", "Stephen King"),
            ("It", "Stephen King"),
            ("The Stand", "Stephen King"),
            ("Pet Sematary", "Stephen King"),
            ("The Girl with the Dragon Tattoo", "Stieg Larsson"),
            ("Gone Girl", "Gillian Flynn"),
            ("The Hunger Games", "Suzanne Collins"),
            ("Mockingjay", "Suzanne Collins"),
            ("The Maze Runner", "James Dashner"),
            ("Divergent", "Veronica Roth"),
            ("Ender's Game", "Orson Scott Card"),
            ("Neuromancer", "William Gibson"),
            ("The Road", "Cormac McCarthy"),
            ("Blood Meridian", "Cormac McCarthy"),
            ("A Game of Thrones", "George R.R. Martin"),
            ("A Clash of Kings", "George R.R. Martin"),
            ("A Storm of Swords", "George R.R. Martin"),
            ("A Feast for Crows", "George R.R. Martin"),
            ("A Dance with Dragons", "George R.R. Martin"),
            ("The Silmarillion", "J.R.R. Tolkien"),
            ("The Chronicles of Narnia", "C.S. Lewis"),
            ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
            ("Harry Potter and the Chamber of Secrets", "J.K. Rowling"),
            ("Harry Potter and the Prisoner of Azkaban", "J.K. Rowling"),
            ("Harry Potter and the Goblet of Fire", "J.K. Rowling"),
            ("Harry Potter and the Order of the Phoenix", "J.K. Rowling"),
            ("Harry Potter and the Half-Blood Prince", "J.K. Rowling"),
            ("Harry Potter and the Deathly Hallows", "J.K. Rowling"),
            ("The Alchemist", "Paulo Coelho"),
            ("The Da Vinci Code", "Dan Brown"),
            ("Angels and Demons", "Dan Brown"),
            ("Inferno", "Dan Brown"),
            ("The Lovely Bones", "Alice Sebold"),
            ("Little Women", "Louisa May Alcott"),
            ("Great Expectations", "Charles Dickens"),
            ("Oliver Twist", "Charles Dickens"),
            ("David Copperfield", "Charles Dickens"),
            ("A Tale of Two Cities", "Charles Dickens"),
            ("Sense and Sensibility", "Jane Austen"),
            ("Emma", "Jane Austen"),
            ("Northanger Abbey", "Jane Austen"),
            ("Persuasion", "Jane Austen"),
            ("The Secret Garden", "Frances Hodgson Burnett"),
            ("The Wind in the Willows", "Kenneth Grahame"),
            ("Charlotte's Web", "E.B. White"),
            ("Stuart Little", "E.B. White"),
            ("The Outsiders", "S.E. Hinton"),
            ("The Giver", "Lois Lowry"),
            ("Hatchet", "Gary Paulsen"),
            ("Tales of the Unexpected", "Roald Dahl"),
            ("James and the Giant Peach", "Roald Dahl"),
            ("Matilda", "Roald Dahl"),
            ("Charlie and the Chocolate Factory", "Roald Dahl"),
            ("Fantastic Mr. Fox", "Roald Dahl"),
            ("The BFG", "Roald Dahl")
        ]

        for title, author in books_data:
            self.add_book(title, author)

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        self.save_data()  # Save data whenever a book is added

    def add_books_bulk(self, books):
        for title, author in books:
            self.add_book(title, author)

    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        self.save_data()  # Save data whenever a member is added

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_member(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    def borrow_book(self, title, member_name):
        book = self.find_book(title)
        member = self.find_member(member_name)
        if book and member:
            member.borrow_book(book)
            self.save_data()  # Save data whenever a book is borrowed
        else:
            messagebox.showerror("Error", "Book or member not found.")

    def return_book(self, title, member_name):
        book = self.find_book(title)
        member = self.find_member(member_name)
        if book and member:
            member.return_book(book)
            self.save_data()  # Save data whenever a book is returned
        else:
            messagebox.showerror("Error", "Book or member not found.")

    def generate_report(self):
        report = "\nLibrary Report:\n"
        report += f"Total books: {len(self.books)}\n"
        report += f"Total members: {len(self.members)}\n\nBooks:\n"
        for book in self.books:
            report += str(book) + "\n"
        report += "\nMembers:\n"
        for member in self.members:
            report += str(member) + "\n"
        messagebox.showinfo("Library Report", report)

    def save_data(self):
        with open('library_data.pkl', 'wb') as file:
            data = {
                'books': self.books,
                'members': self.members
            }
            pickle.dump(data, file)

    def load_data(self):
        try:
            with open('library_data.pkl', 'rb') as file:
                data = pickle.load(file)
                self.books = data['books']
                self.members = data['members']
        except FileNotFoundError:
            self.initialize_library()
        except EOFError:
            self.initialize_library()

class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.create_menubar()
        self.create_widgets()

    def create_menubar(self):
        menubar = tk.Menu(self.root)

        # Library menu
        library_menu = tk.Menu(menubar, tearoff=0)
        library_menu.add_command(label="Add Book", command=self.add_book)
        library_menu.add_command(label="Add Books in Bulk", command=self.add_books_bulk)
        library_menu.add_command(label="Register Member", command=self.add_member)
        library_menu.add_command(label="Borrow Book", command=self.borrow_book)
        library_menu.add_command(label="Return Book", command=self.return_book)
        library_menu.add_command(label="Generate Report", command=self.generate_report)
        menubar.add_cascade(label="Library", menu=library_menu)

        # Support menu
        support_menu = tk.Menu(menubar, tearoff=0)
        support_menu.add_command(label="Contact Support", command=self.contact_support)
        menubar.add_cascade(label="Support", menu=support_menu)

        self.root.config(menu=menubar)

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg='#f0f8ff')
        self.frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        self.title_label = tk.Label(self.frame, text="Library Management System", bg='#f0f8ff', font=("Helvetica", 24, "bold"))
        self.title_label.pack(pady=10)

        # Search bar
        self.search_label = tk.Label(self.frame, text="Search for a Book:", bg='#f0f8ff', font=("Helvetica", 14, "bold"))
        self.search_label.pack(pady=5)

        self.search_entry = tk.Entry(self.frame, font=("Helvetica", 12))
        self.search_entry.pack(pady=5, fill=tk.X)
        self.search_entry.bind("<KeyRelease>", self.search_books)

        # Catalogue section
        self.catalogue_label = tk.Label(self.frame, text="Library Catalogue", bg='#f0f8ff', font=("Helvetica", 16, "bold"))
        self.catalogue_label.pack(pady=10)

        self.catalogue_frame = tk.Frame(self.frame, bg='#f0f8ff')
        self.catalogue_frame.pack(pady=10)

        self.catalogue_text = tk.Text(self.catalogue_frame, height=15, width=80, wrap=tk.WORD, bg='#f5f5f5', font=("Helvetica", 10))
        self.catalogue_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.catalogue_scroll = tk.Scrollbar(self.catalogue_frame, orient=tk.VERTICAL, command=self.catalogue_text.yview)
        self.catalogue_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.catalogue_text.config(yscrollcommand=self.catalogue_scroll.set)

        # Display existing books in the catalogue
        self.update_catalogue_text()

        # Buttons section
        self.buttons_frame = tk.Frame(self.frame, bg='#f0f8ff')
        self.buttons_frame.pack(pady=20)

        self.add_book_button = tk.Button(self.buttons_frame, text="Add Book", command=self.add_book, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.add_book_button.pack(side=tk.LEFT, padx=10)

        self.add_books_bulk_button = tk.Button(self.buttons_frame, text="Add Books in Bulk", command=self.add_books_bulk, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.add_books_bulk_button.pack(side=tk.LEFT, padx=10)

        self.add_member_button = tk.Button(self.buttons_frame, text="Register Member", command=self.add_member, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.add_member_button.pack(side=tk.LEFT, padx=10)

        self.borrow_book_button = tk.Button(self.buttons_frame, text="Borrow Book", command=self.borrow_book, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.borrow_book_button.pack(side=tk.LEFT, padx=10)

        self.return_book_button = tk.Button(self.buttons_frame, text="Return Book", command=self.return_book, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.return_book_button.pack(side=tk.LEFT, padx=10)

        self.generate_report_button = tk.Button(self.buttons_frame, text="Generate Report", command=self.generate_report, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.generate_report_button.pack(side=tk.LEFT, padx=10)

        # Support button
        self.contact_support_button = tk.Button(self.frame, text="Contact Support", command=self.contact_support, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.contact_support_button.pack(pady=10)

    def update_catalogue_text(self):
        self.catalogue_text.delete('1.0', tk.END)
        for book in self.library.books:
            self.catalogue_text.insert(tk.END, f"{book.title} by {book.author} - {book.get_status()}\n")

    def search_books(self, event):
        search_query = self.search_entry.get().lower()
        self.catalogue_text.delete('1.0', tk.END)
        for book in self.library.books:
            if search_query in book.title.lower() or search_query in book.author.lower():
                self.catalogue_text.insert(tk.END, f"{book.title} by {book.author} - {book.get_status()}\n")

    def add_book(self):
        self.book_window = tk.Toplevel(self.root)
        self.book_window.title("Add Book")
        self.book_window.geometry("400x250")

        self.title_label = tk.Label(self.book_window, text="Book Title:", font=("Helvetica", 12))
        self.title_label.pack(pady=10)

        self.title_entry = tk.Entry(self.book_window, font=("Helvetica", 12))
        self.title_entry.pack(pady=5, fill=tk.X)

        self.author_label = tk.Label(self.book_window, text="Book Author:", font=("Helvetica", 12))
        self.author_label.pack(pady=10)

        self.author_entry = tk.Entry(self.book_window, font=("Helvetica", 12))
        self.author_entry.pack(pady=5, fill=tk.X)

        self.add_button = tk.Button(self.book_window, text="Add Book", command=self.add_book_to_library, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.add_button.pack(pady=10)

    def add_book_to_library(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.library.add_book(title, author)
            self.update_catalogue_text()
            self.book_window.destroy()
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showerror("Error", "Please enter both title and author.")

    def add_books_bulk(self):
        self.bulk_window = tk.Toplevel(self.root)
        self.bulk_window.title("Add Books in Bulk")
        self.bulk_window.geometry("500x300")

        self.bulk_label = tk.Label(self.bulk_window, text="Enter books in the format 'Title, Author':", font=("Helvetica", 12))
        self.bulk_label.pack(pady=10)

        self.bulk_text = tk.Text(self.bulk_window, height=10, width=60, wrap=tk.WORD, bg='#f5f5f5', font=("Helvetica", 10))
        self.bulk_text.pack(pady=10)

        self.add_bulk_button = tk.Button(self.bulk_window, text="Add Books", command=self.add_books_to_library_bulk, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.add_bulk_button.pack(pady=10)

    def add_books_to_library_bulk(self):
        bulk_data = self.bulk_text.get('1.0', tk.END).strip().split('\n')
        books = []
        for line in bulk_data:
            if line.strip():
                parts = line.split(', ')
                if len(parts) == 2:
                    books.append((parts[0], parts[1]))
        if books:
            self.library.add_books_bulk(books)
            self.update_catalogue_text()
            self.bulk_window.destroy()
            messagebox.showinfo("Success", "Books added in bulk successfully!")
        else:
            messagebox.showerror("Error", "Invalid book data format.")

    def add_member(self):
        name = simpledialog.askstring("Input", "Enter member name:")
        if name:
            self.library.add_member(name)
            messagebox.showinfo("Success", f"Member '{name}' registered successfully!")

    def borrow_book(self):
        self.borrow_window = tk.Toplevel(self.root)
        self.borrow_window.title("Borrow Book")
        self.borrow_window.geometry("400x200")

        self.title_label = tk.Label(self.borrow_window, text="Book Title:", font=("Helvetica", 12))
        self.title_label.pack(pady=10)

        self.title_entry = tk.Entry(self.borrow_window, font=("Helvetica", 12))
        self.title_entry.pack(pady=5, fill=tk.X)

        self.member_label = tk.Label(self.borrow_window, text="Member Name:", font=("Helvetica", 12))
        self.member_label.pack(pady=10)

        self.member_entry = tk.Entry(self.borrow_window, font=("Helvetica", 12))
        self.member_entry.pack(pady=5, fill=tk.X)

        self.borrow_button = tk.Button(self.borrow_window, text="Borrow Book", command=self.borrow_book_from_library, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.borrow_button.pack(pady=10)

    def borrow_book_from_library(self):
        title = self.title_entry.get()
        member_name = self.member_entry.get()
        if title and member_name:
            self.library.borrow_book(title, member_name)
            self.update_catalogue_text()
            self.borrow_window.destroy()
            messagebox.showinfo("Success", f"Book '{title}' borrowed by '{member_name}'!")
        else:
            messagebox.showerror("Error", "Please enter both book title and member name.")

    def return_book(self):
        self.return_window = tk.Toplevel(self.root)
        self.return_window.title("Return Book")
        self.return_window.geometry("400x200")

        self.title_label = tk.Label(self.return_window, text="Book Title:", font=("Helvetica", 12))
        self.title_label.pack(pady=10)

        self.title_entry = tk.Entry(self.return_window, font=("Helvetica", 12))
        self.title_entry.pack(pady=5, fill=tk.X)

        self.member_label = tk.Label(self.return_window, text="Member Name:", font=("Helvetica", 12))
        self.member_label.pack(pady=10)

        self.member_entry = tk.Entry(self.return_window, font=("Helvetica", 12))
        self.member_entry.pack(pady=5, fill=tk.X)

        self.return_button = tk.Button(self.return_window, text="Return Book", command=self.return_book_to_library, bg='#4682b4', fg='white', font=("Helvetica", 12))
        self.return_button.pack(pady=10)

    def return_book_to_library(self):
        title = self.title_entry.get()
        member_name = self.member_entry.get()
        if title and member_name:
            self.library.return_book(title, member_name)
            self.update_catalogue_text()
            self.return_window.destroy()
            messagebox.showinfo("Success", f"Book '{title}' returned by '{member_name}'!")
        else:
            messagebox.showerror("Error", "Please enter both book title and member name.")

    def generate_report(self):
        self.library.generate_report()

    def contact_support(self):
        support_info = (
            "For support, please contact:\n"
            "Email: support@library.com\n"
            "Phone: +123-456-7890\n"
            "Address: 123 Library Lane, Booktown, BK 12345"
        )
        messagebox.showinfo("Contact Support", support_info)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("800x600")
    root.configure(bg='#f0f8ff')

    library = Library()
    app = LibraryGUI(root, library)
    root.mainloop()
