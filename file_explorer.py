import sys
from pathlib import Path

EXTENSION_TYPES = {
  ".txt": "text/plain",
  ".jpeg": "image/jpeg",
  ".png": "image/png",
  ".pdf": "application/pdf",
  ".zip": "application/zip",
}

def list_directory(path):
  base = Path(path)
  for thing in base.iterdir():
    if thing.is_dir()
      type = "dir"
      size = "-"
      extension = "-"
    elif thing.is_file():
      type = "file"
      size = thing.stat().st_size
      extension = get_extension(thing)
    print(f"{str(full_path):<40} [{item_type:<4}] {size:>6}    {content_type}")
  
def get_extension(file_name):
  return EXTENSION_TYPES.get(path.suffix())


if __name__ == "__main__":
  list_directory(sys.argv[1])
