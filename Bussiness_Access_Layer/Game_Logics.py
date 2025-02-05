import Bussiness_Entities.Game_Entites as Bent
import Data_Access_Layer.Data_DB as Dal
import random
obj_db=Dal.C_Data_DB()
class C_Game_Logics:
    def random_number_generation(self, obj_ent=Bent.C_Entites()):
        return random.randrange(obj_ent.get_lower_bound(), obj_ent.get_upper_bound())

    def game_logic(self, obj_ent=Bent.C_Entites()):
        guess_number = obj_ent.get_guess_number()
        random_number = obj_ent.get_random_number()
        if guess_number == random_number:
            return "equal"
        elif guess_number < random_number:
            return "low"
        elif guess_number > random_number:
            return "high"
        elif guess_number > obj_ent.get_lower_bound():
            return "Out of higher bound"
        elif guess_number < obj_ent.get_lower_bound():
            return "Out of lower bound"
        else:
            return "error"

    def insertion_DB(self, obj_ent=Bent.C_Entites()):
        obj_db.sql_server_connect()
        obj_db.insert(obj_ent)

    def history_DB(self):
        obj_db.sql_server_connect()
        return obj_db.history()
