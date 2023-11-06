# list.txt 清單中是封面圖檔名，是以 book_id命名
with open('list.txt', 'r') as file:
    lines = file.readlines()

for i, line in enumerate(lines, 1):
    filename = line.strip()
    parts = filename.split('.')
    if len(parts) == 2:
        file_name, extension = parts
        print(f"INSERT INTO `file_attachment` (`File_attachment_ID`, `Book_ID`, `File_Path`, `File_Type`) VALUES ({i+1}, {file_name}, 'https://lib2.tereyo.com/{filename}', 0);")
    else:
        print(f"id {i}: format error - {filename}")
