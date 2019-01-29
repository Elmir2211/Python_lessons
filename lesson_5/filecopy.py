def file_copy():
    import shutil
    import sys
    first_file = sys.argv[0]
    copy_file = first_file + '.backup'
    shutil.copy(first_file, copy_file)
file_copy()