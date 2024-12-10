import os
from bs4 import BeautifulSoup

def extract_comments(file_path):
    if not os.path.exists(file_path):
        print(f"فایل یافت نشد: {file_path}")
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    
    # یافتن تمام مقالات مربوط به کامنت‌ها
    comment_articles = soup.find_all('article', class_='comments-comment-entity')
    
    comments_data = []
    
    for article in comment_articles:
        # استخراج نام کاربر
        user_tag = article.find('span', class_='comments-comment-meta__description-title')
        user_name = user_tag.get_text(strip=True) if user_tag else 'نامشخص'
        
        # استخراج متن کامنت
        comment_span = article.find('span', class_='comments-comment-item__main-content')
        comment_text = comment_span.get_text(strip=True) if comment_span else 'بدون متن'
        
        comments_data.append({
            'user': user_name,
            'comment': comment_text
        })
    
    return comments_data

def main():
    # مسیر فایل linkedin.txt
    file_path = r'linkedin.txt'
    
    comments = extract_comments(file_path)
    with open('result.txt', 'w', encoding='utf-8') as file:
        for comment in comments:
           if comment['user'] != 'Massoud Beygi':
            file.write(f"{comment['user']}   | {comment['comment']}\n")

if __name__ == "__main__":
    main()