

from download_utils import ( BUCKET_NAME, SERVER, ACCESS_KEY, SECRET_KEY )
from download_utils import DownloadHelper

def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    downlaod_helper = DownloadHelper( SERVER,
                                      access_key=ACCESS_KEY,
                                      secret_key=SECRET_KEY )
    
    # Get the train and validate file lists.
    try:
        downlaod_helper.download( BUCKET_NAME,
                                'MVS_Fisheye_Dataset/minio_list_train.txt', 
                                './minio_list_train.txt' )

        downlaod_helper.download( BUCKET_NAME, 
                                'MVS_Fisheye_Dataset/minio_list_validate.txt', 
                                './minio_list_validate.txt' )
    except Exception as exc:
        print(exc)
        return 1

    return 0

if __name__ == "__main__":
    import sys
    sys.exit( main() )
    