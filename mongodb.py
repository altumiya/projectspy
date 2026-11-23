# mongodb with python 
#pymongo for installation
#import pymongo
from pymongo import MongoClient #so that pymongo repeated use must be stop example below
from bson import ObjectId

#client = pymongo.MongoClient(mongodb+srv://CHAI:CHAI@cluster0.lxl3fsq.mongodb.net/", tlsAllowInvalidCertificates=True)

client = MongoClient("mongodb+srv://app_admin:SecurePass123!@cluster0.lxl3fsq.mongodb.net/?retryWrites=true&w=majority", tlsAllowInvalidCertificates=True)

db = client["utmanager"] #std approach

video_collection = db["videos"]

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

    def list_videos():
        videos = list(video_collection.find())
        if not videos:
            print("\nNo videos found.")
            return
    
        print("\n--- All Videos ---")
        for video in videos:
            print(f"ID: {video['_id']} | Name: {video['name']} | Time: {video['time']}")
    
    
    def update_video(video_id, new_name, new_time):
        try:
            result = video_collection.update_one(
                {"_id": ObjectId(video_id)},
                {"$set": {"name": new_name, "time": new_time}},
            )
            if result.matched_count:
                print("Video updated successfully!")
            else:
                print("No video found with that ID.")
        except Exception as e:
            print(f"Error: Invalid ID format ({e})")
    
    
    def delete_video(video_id):
        try:
            result = video_collection.delete_one({"_id": ObjectId(video_id)})
            if result.deleted_count:
                print("Video deleted successfully!")
            else:
                print("No video found with that ID.")
        except Exception as e:
            print(f"Error: Invalid ID format ({e})")
    
    
    def main():
        while True:
            print("\n=== YouTube Manager App ===")
            print("1. List all videos")
            print("2. Add a new video")
            print("3. Update a video")
            print("4. Delete a video")
            print("5. Exit the app")
            choice = input("Enter your choice (1-5): ").strip()
    
            if choice == "1":
                list_videos()
            elif choice == "2":
                name = input("Enter the video name: ").strip()
                time = input("Enter the video duration/time: ").strip()
                add_video(name, time)
            elif choice == "3":
                video_id = input("Enter the video ID to update: ").strip()
                name = input("Enter the updated video name: ").strip()
                time = input("Enter the updated video duration/time: ").strip()
                update_video(video_id, name, time)
            elif choice == "4":
                video_id = input("Enter the video ID to delete: ").strip()
                delete_video(video_id)
            elif choice == "5":
                print("Exiting application...")
                break
            else:
                print("Invalid choice, please select between 1 and 5.")
    
    
    if __name__ == "__main__":
        main()       
