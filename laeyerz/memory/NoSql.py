# Created: Anil Variyar
# NoSQL

from laeyerz.memory.nosqldb.MongoAdapter import MongoAdapter

class NoSql:
    def __init__(self, dbtype='Mongo'):
        if(dbtype == 'Mongo'):
            self.db = MongoAdapter()
        else:
            raise ValueError("Invalid database type")




    def create_session(self, session_id, title):
        print("Creating session")

        newSession = {
            'id': session_id,
            'title': title,
        }

        #check for duplicate in title
        #if same title exists, return the existing session id
        existingSession = self.db.read_one('session', {'title': title})

        if existingSession:
            print("Session already exists! Session titles should be unique")
            return False

        else:
            self.db.create('session',newSession)
            return True


    def load_session_list(self):
        print("Loading session list")

        session_list = self.db.read('session', {})

        return session_list



    def load_session(self, title):
        print("Reading session")

        curr_session = self.db.read_one('session', {'title': title})

        return curr_session


    def add_session_item(self, session_id, item):
        print("Adding session item")

        self.db.create('chats', item)




    def create_document(self, document_id, title, document_type):
        print("Creating document")

        doc = {
            'id': document_id,
            'title': title,
            'document_type': document_type,
        }

        docItem = self.db.create('document', doc)

        return docItem
  


    def add_items(self, items):

        items = self.db.create_many('items', items)

        return items




    def read_document(self, document_id):
        print("Reading document")

        self.db.read(document_id)











