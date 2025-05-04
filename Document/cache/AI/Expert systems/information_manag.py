class Document:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class InformationManagementSystem:
    def __init__(self):
        self.documents = []  # List of documents in the system

    # Function to add a document to the system
    def add_document(self):
        title = input("Enter the title of the document: ")
        description = input("Enter the description of the document: ")
        new_doc = Document(title, description)
        self.documents.append(new_doc)
        print("Document added successfully!")

    # Function to display all documents
    def display_documents(self):
        if not self.documents:
            print("No documents in the system.")
            return

        print("Listing all documents:")
        for doc in self.documents:
            print(f"Title: {doc.title}, Description: {doc.description}")

    # Function to search for a document by title
    def search_document(self):
        query = input("Enter the title of the document you want to search: ")
        found = False
        for doc in self.documents:
            if doc.title == query:
                print("Found document:")
                print(f"Title: {doc.title}, Description: {doc.description}")
                found = True
                break

        if not found:
            print(f"Document with the title \"{query}\" not found.")

    # Function to delete a document by title
    def delete_document(self):
        query = input("Enter the title of the document you want to delete: ")
        doc_to_delete = next((doc for doc in self.documents if doc.title == query), None)

        if doc_to_delete:
            self.documents.remove(doc_to_delete)
            print("Document deleted successfully!")
        else:
            print(f"Document with the title \"{query}\" not found.")

    # Function to update the description of an existing document
    def update_document(self):
        query = input("Enter the title of the document you want to update: ")
        doc_to_update = next((doc for doc in self.documents if doc.title == query), None)

        if doc_to_update:
            new_description = input("Enter the new description for the document: ")
            doc_to_update.description = new_description
            print("Document updated successfully!")
        else:
            print(f"Document with the title \"{query}\" not found.")

    # Main menu to interact with the system
    def display_menu(self):
        while True:
            print("\nInformation Management System Menu:")
            print("1. Add a document")
            print("2. Display all documents")
            print("3. Search for a document by title")
            print("4. Delete a document")
            print("5. Update a document's description")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_document()
            elif choice == "2":
                self.display_documents()
            elif choice == "3":
                self.search_document()
            elif choice == "4":
                self.delete_document()
            elif choice == "5":
                self.update_document()
            elif choice == "6":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of the Information Management System and run it
if __name__ == "__main__":
    ims = InformationManagementSystem()
    ims.display_menu()
