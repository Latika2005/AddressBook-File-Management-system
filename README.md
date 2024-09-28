# 🗂️ Address Book CLI Application

A **simple yet powerful** Command Line Interface (CLI) application that allows you to manage your contacts in a user-friendly manner. Built with Python, it uses external file storage to keep your contacts safe, even after the program closes! Whether it's adding, viewing, or searching for contacts, this tool has got you covered.

---

## 🌟 Features

✨ **Add Contact**  
Easily add new contacts by entering their name, phone number, and email address. The contact gets automatically saved into the `address_book.txt` file.

👀 **View Contacts**  
Display all the saved contacts in a neat and well-structured table format.

🔍 **Search Contact**  
Search for a contact by their name. The app will instantly display the contact details if found.

💾 **File Management**  
No worries about losing data! The app saves and loads contacts directly from an external file (`address_book.txt`).

---

## 🚀 How to Get Started

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/Latika2005/AdreesBook-File-Management-system.git
```

### 2. Install Python

Make sure you have Python 3 installed. You can download it [here](https://www.python.org/downloads/).

### 3. Run the Application

Run the Python script to start managing your contacts:

```bash
python main.py
```

---

## 🎮 Usage Instructions

When you run the program, you'll see this menu:

```bash
Address Book
1. Add Contact
2. View Contacts
3. Search Contact
4. Exit
```

### 💼 Option 1: Add a Contact

- Enter the name, phone number, and email when prompted.
- The contact will be added to the file and saved for future use.

### 📖 Option 2: View Contacts

- Lists all your contacts in a table format with details such as name, phone number, and email.

### 🔎 Option 3: Search Contact

- Enter a contact's name to search for them in the list.
- If the contact exists, their details will be displayed.

### 🛑 Option 4: Exit

- Simply exit the application.

---

## 📂 File Structure

Your contacts are saved in a simple, easy-to-read text file called `address_book.txt`. Each contact is stored as a comma-separated line like this:

```
Name,Phone Number,Email
John Doe,+1 1234567890,johndoe@example.com
```

### Example:

```bash
============================================================
-                      Contact List                       -
============================================================
-    Name         Phone            Email                  -
------------------------------------------------------------
1   John Doe      +91 9876543210   johndoe@example.com     
------------------------------------------------------------
2   Jane Smith    +44 1234567890   janesmith@example.co.uk 
------------------------------------------------------------
============================================================
```

---

## 🛠️ Technical Details

This application uses Python’s built-in file handling capabilities to:

- **Load Contacts**: Automatically loads contacts from the file when the application starts.
- **Save Contacts**: Saves new and updated contacts back to the file after every operation.
- **Handle Errors**: If the file is missing or empty, the app will handle the error gracefully.

---

## 🎨 Customizations

Want to make the app your own? Here are a few things you could tweak:

1. **Change the File Format**: Switch from `.txt` to `.csv` for easier handling in spreadsheets.
2. **Additional Fields**: Add more details to your contacts (like address, birthday, etc.).
3. **Sort Contacts**: Implement sorting options to view contacts alphabetically or by phone number.

---

## ⚡ Future Enhancements

Here’s what’s on the roadmap for this CLI app:

- **Export to CSV**: Easily export all contacts to a `.csv` file.
- **Import Contacts**: Import contacts from an external `.csv` file.
- **Delete/Update Contacts**: Add more flexibility to manage contacts.

---

