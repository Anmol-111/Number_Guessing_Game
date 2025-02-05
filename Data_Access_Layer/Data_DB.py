import Bussiness_Entities.Game_Entites as Bent
import pymssql
class C_Data_DB:
    def sql_server_connect(self):
        global cursor
        global constr
        constr = pymssql.connect(server="LAPTOP-8T8MA06J\\SQLEXPRESS",
                                 user="root",
                                 password="Admin@1234",
                                 database="Guessing_Game")
        cursor = constr.cursor()

    def insert(self, obj_ent=Bent.C_Entites()):
        cursor.callproc('sp_insert_data', (obj_ent.get_name(), obj_ent.get_age(), obj_ent.get_random_number(), obj_ent.get_result()))
        constr.commit()

    def history(self):
        cursor.callproc('sp_history')
        data=cursor.fetchall()
        return data