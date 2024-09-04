
from tqdm import tqdm

from minio import Minio
from minio.error import S3Error
from minio.helpers import ProgressType

class BarTqdm(ProgressType):
    def __init__(self) -> None:
        super().__init__()
        
        self.pbar = None
        
    def set_meta(self, object_name: str, total_length: int):
        self.pbar = tqdm( total=total_length, 
                          unit='B',
                          unit_scale=True,
                          desc=object_name )
        
    def update(self, length: int):
        self.pbar.update(length)

class DownloadHelper(object):
    def __init__(self, server: str, access_key: str, secret_key: str) -> None:
        super().__init__()
        
        self.client = Minio(server,
                            access_key=access_key,
                            secret_key=secret_key,
                            secure=True )
        
    def download(self, bucket_name, remote_path, local_path) -> None:
        object_stat = self.client.stat_object(bucket_name, remote_path)
        object_size = object_stat.size

        # Attempt to get the object, which will raise an error if it doesn't exist
        self.client.fget_object( bucket_name, 
                                 remote_path, 
                                 local_path,
                                 progress=BarTqdm() )
