import os
from pathlib import Path

def main():
    dir_path = "."  # 当前目录
    merge_split_pdfs_in_directory(dir_path)

def merge_split_pdfs_in_directory(dir_path):
    split_files = {}
    
    # 扫描目录中的文件
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        
        # 跳过目录
        if os.path.isdir(file_path):
            continue
        
        # 查找分割的PDF文件
        if ".pdf." in file_name:
            base_name = file_name.split(".pdf.")[0] + ".pdf"
            if base_name not in split_files:
                split_files[base_name] = []
            split_files[base_name].append(file_name)
    
    # 合并每组分割文件
    for base_name, parts in split_files.items():
        parts.sort()  # 确保文件顺序正确
        merge_files(base_name, parts)

def merge_files(base_name, parts):
    with open(base_name, 'wb') as merged_file:
        for part in parts:
            with open(part, 'rb') as part_file:
                merged_file.write(part_file.read())
            os.remove(part)  # 合并后删除分割文件

if __name__ == "__main__":
    main()