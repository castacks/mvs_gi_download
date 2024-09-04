
import argparse
import os
from tqdm import tqdm

from download_utils import ( BUCKET_NAME, SERVER, ACCESS_KEY, SECRET_KEY )
from download_utils import DownloadHelper

def check_create_dir(d: str):
    if not os.path.isdir(d):
        os.makedirs(d)

def read_list(fn: str):
    with open(fn, 'r') as fp:
        lines = fp.readlines()
        return [ line.strip() for line in lines ]

def handle_args():
    parser = argparse.ArgumentParser(description='Download dataset by referencing a list file. ')
    
    parser.add_argument( '--input_list', type=str, 
                         help='The list file in txt format. ' )
    
    parser.add_argument( '--output_dir', type=str,
                         help='The output directory. ')
    
    parser.add_argument( '--dataset_type', type=str, choices=['train', 'validate'],
                         help='The type of dataset. Choose from "train" and "validate". ')
    
    return parser.parse_args()

def main():
    args = handle_args()
    
    # Check the output directory.
    check_create_dir( args.output_dir )
    
    # Read the input list.
    files = read_list( args.input_list )
    print('Downloading the following files: ')
    for f in files:
        print(f)
        
    print('')
    
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    downlaod_helper = DownloadHelper( SERVER,
                                      access_key=ACCESS_KEY,
                                      secret_key=SECRET_KEY )
    
    # Download the file.
    res = 0
    for f in tqdm(files, desc=f'>> Downloading {len(files)} files'):
        print(f'>>> Downloading {f}...')
        
        object_path = os.path.join( 'MVS_Fisheye_Dataset/compressed_dataset', args.dataset_type, f )
        out_fn = os.path.join( args.output_dir, f )
        
        # Make the directory if it does not exist.
        os.makedirs( os.path.dirname( out_fn ), exist_ok=True )
        
        try:
            downlaod_helper.download( BUCKET_NAME,
                                      object_path, 
                                      out_fn )
        except Exception as exc:
            print(exc)
            res = 1
            
        print('')

    return res

if __name__ == "__main__":
    import sys
    sys.exit( main() )