import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
           return json.load(file)
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    if len(videos) == 0:
        print("No videos to display")
    else:
        for i, video in enumerate(videos):
            print(f"{i+1}. {video['name']}, {video['time']} mins")


def save_data_helper(videos):
    try:
        with open("youtube.txt", "w") as file:
            return json.dump(videos,file)
    except:
        print("failed to save")


def add_video(videos):
    video_description = input("Enter video name").strip()
    time_dur = input("Enter time duration")

    if video_description:
        videos.append({"name":video_description, "time":time_dur})
        save_data_helper(videos)
        print("Video description saved")
    else:
        print("video description cannot be empty")


def update_video(videos):
    list_all_videos(videos)
    update_num = int(input("Enter video number you want to change"))

    if 1 <= update_num <= len(videos):
        name = input("Enter the name: ")
        time = input("Enter the time duration: ")
        videos[update_num - 1 ] = {"name": name, "time": time}
        save_data_helper(videos)

def del_videos(videos):
    list_all_videos(videos)
    num = int(input("Enter the number you want to delete"))

    if 1 <= num <= len(videos):
        del videos[num - 1]
        save_data_helper(videos)
    else:
        print("number is invalid")


def main():
    videos = []
    while True:
        print("Youtube Manager\n")
        print("1. list all the youtube videos")
        print("2. Add a Youtube videos")
        print("3. Update a youtube videos")
        print("4. Delete a youtube videos")
        print("5. Exit the program")
        choice = input("Enter your choice")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                del_videos(videos)
            case '5':
                print("Exit the program")
                break
            case _:
                print("Invalid")

if __name__ == "__main__":
    main()








