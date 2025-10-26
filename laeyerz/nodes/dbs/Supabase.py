# Copyright 2025 Pixagan Technologies
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Supabase module for Supabase database integration
in the Laeyerz framework.
"""

from laeyerz.flow.Node import Node
import os
from supabase import create_client, Client

class Supabase(Node):
    def __init__(self, config={}):
        self.client = create_client(os.getenv('SUPABASE_URL'), os.getenv('SUPABASE_KEY'))


    def fetch_data(self, table_name):
        return self.client.table(table_name).select("*").execute()

    def insert_data(self, table_name, data):
        return self.client.table(table_name).insert(data).execute()

    def update_data(self, table_name, data):
        return self.client.table(table_name).update(data).eq('id', data['id']).execute()
        
    def upsert_data(self, table_name, data):
        return self.client.table(table_name).upsert(data).execute()
        
    def delete_data(self, table_name, data):
        return self.client.table(table_name).delete().eq('id', data['id']).execute()
        
    def all_postgres(self, fun_in):
        return self.client.rpc(fun_in).execute()
        