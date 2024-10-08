from services.post_service import insert_post, get_all_posts, update_post, delete_post

def main():
    # הכנס פוסט חדש
    post_id = insert_post(
        source='Twitter',
        content='Important update from Twitter',
        metadata={'date': '2024-10-07', 'relevance': 'high'}
    )
    print(f'Document inserted: {post_id}')

    # קבל את כל הפוסטים
    posts = get_all_posts()
    print(f'All posts: {posts}')

    # עדכן פוסט אם קיים
    if posts:
        updated_count = update_post(posts[0]['_id'], {'content': 'Updated content'})
        print(f'Number of posts updated: {updated_count}')

    # מחק פוסט אם קיים
    if posts:
        deleted_count = delete_post(posts[0]['_id'])
        print(f'Number of posts deleted: {deleted_count}')

if __name__ == '__main__':
    main()
