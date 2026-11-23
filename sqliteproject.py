# db assignment with sqlite3
import sqlite3
conn = sqlite3.connect('utube_vids.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    ) 

''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if not videos:
        print("No videos in the list.")
        return
    for row in videos:
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)", (name,time))
    conn.commit()

def update_video(vid,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id == ?", (new_name,new_time,vid))
    conn.commit()

def delete_video(vid):
    cursor.execute("DELETE FROM videos where id = ?", (vid,)) # , as tuple is accepted
    conn.commit()

def main():
    while True:
        print("\n UTUBE MANAGER WITH DB")
        print("1. list a fav video")
        print("2. add a utube video")
        print("3. update a utube video")
        print("4. delete a utube video")
        print("5. exit")
        choice = input("enter the choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter the video name: ") 
            time = input("enter the video time: ") 
            add_video(name,time) 
        elif choice == '3':
            vid = input("enter the video id to update: ")
            name = input("enter the video name: ") 
            time = input("enter the video time: ") 
            update_video(vid,name,time)
        elif choice == '4':
            vid = input("enter the video id to update: ")
            delete_video(vid)
        elif choice == '5':
            break
        else:
            print("invalid choice selected")                  
    conn.close() # for not to corrupt the db


if __name__ == "__main__":    #dunder
    main()     
