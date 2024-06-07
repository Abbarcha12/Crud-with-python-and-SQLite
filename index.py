import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# Create the videos table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

# Function to list all videos
def list_videos():
    cur.execute("SELECT * FROM videos")
    rows = cur.fetchall()
    
    if not rows:
        print("No Videos to list ? Add a video")
    else:
        for row in rows:
            print(row)

# Function to add a new video
def add_video(name, time):
    cur.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    conn.commit()

# Function to update an existing video
def update_video(videoId, new_name, new_time):
    cur.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (new_name, new_time, videoId))
    conn.commit()

# Function to delete a video
def delete_video(videoId):
    cur.execute('DELETE FROM videos WHERE id = ?', (videoId,))
    conn.commit()

# Main function to run the program
def main():
    print("\nYouTube Manager with SQLite3")
    
    while True:
        print("\n1. List All videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video Name: ")
            time = input("Enter the video Time: ")
            add_video(name, time)
        elif choice == "3":
            videoId = input("Enter the video Id to update: ")
            name = input("Enter the new video Name: ")
            time = input("Enter the new video Time: ")
            update_video(videoId, name, time)
        elif choice == "4":
            videoId = input("Enter the video Id to delete: ")
            delete_video(videoId)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid Choice, please try again.")

    conn.close()

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
