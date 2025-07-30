from werkzeug.security import generate_password_hash, check_password_hash

def hasher_mot_de_passe(mot_de_passe):
    return generate_password_hash(mot_de_passe)

def verifier_mot_de_passe(mot_de_passe, hash_stocke):
    return check_password_hash(hash_stocke, mot_de_passe)
