from database import get_db
from models.social_post import SocialPost

def insert_post(source, content, metadata):
    db = get_db()
    post = SocialPost(source, content, metadata)
    result = db.insert_one(post.to_dict())
    return result.inserted_id

def get_all_posts():
    db = get_db()
    return list(db.find())

def update_post(post_id, update_data):
    db = get_db()
    result = db.update_one({'_id': post_id}, {'$set': update_data})
    return result.modified_count

def delete_post(post_id):
    db = get_db()
    result = db.delete_one({'_id': post_id})
    return result.deleted_count
