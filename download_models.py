
import os
from tqdm import tqdm

from download_utils import ( BUCKET_NAME, SERVER, ACCESS_KEY, SECRET_KEY )
from download_utils import DownloadHelper

def main():
    remote_path_prefix = 'code_and_model'
    
    remote_paths = [
        f'{remote_path_prefix}/mvs_gi_code_release_validation_samples/CR_EV004/dsta_sweep_config103_WB_jy2dqg6r_v102.ckpt',
        f'{remote_path_prefix}/mvs_gi_code_release_validation_samples/CR_EV004/ev_sweep_dataset.yaml',
        f'{remote_path_prefix}/mvs_gi_code_release_validation_samples/config/ev_data_dirs.yaml',
        f'{remote_path_prefix}/mvs_gi_code_release_validation_samples/config/ev_main_dataset.yaml',
        f'{remote_path_prefix}/mvs_gi_code_release_validation_samples/config/ev_trainer_callbacks.yaml',
        f'{remote_path_prefix}/onnx_tensorrt/config103_WB_jy2dqg6r_v102_jp4.6.1.engine',
        f'{remote_path_prefix}/onnx_tensorrt/config103_WB_jy2dqg6r_v102_jp5.0.2.engine',
        f'{remote_path_prefix}/onnx_tensorrt/config103_WB_jy2dqg6r_v102_jp5.1.2.engine',
        f'{remote_path_prefix}/onnx_tensorrt/config103_WB_jy2dqg6r_v102_sanitized.onnx',
        f'{remote_path_prefix}/onnx_tensorrt/config29_WB_zslyi5q8_v130_jp4.6.1.engine',
        f'{remote_path_prefix}/onnx_tensorrt/config29_WB_zslyi5q8_v130_jp5.1.2.engine',
        f'{remote_path_prefix}/onnx_tensorrt/config29_WB_zslyi5q8_v130_sanitized.onnx',
        f'{remote_path_prefix}/pre_trained_models/E16/dsta_sweep_config19_WB_zdtldl4s_v96.ckpt',
        f'{remote_path_prefix}/pre_trained_models/E8/dsta_sweep_config24_WB_jbektzh2_v122.ckpt',
        f'{remote_path_prefix}/pre_trained_models/G16/dsta_sweep_config20_WB_f6tysxvk_v93.ckpt',
        f'{remote_path_prefix}/pre_trained_models/G16V/dsta_sweep_config21_WB_a7kccavm_v59.ckpt',
        f'{remote_path_prefix}/pre_trained_models/G16VV/dsta_sweep_config103_WB_jy2dqg6r_v102.ckpt',
        f'{remote_path_prefix}/pre_trained_models/G8/dsta_sweep_config25_WB_koju4sfh_v140.ckpt',
        f'{remote_path_prefix}/code_release_202310_data.zip',
        f'{remote_path_prefix}/mvs_gi_code_release_validation_samples.zip',
    ]
    
    n_char_remote_path_prefix = len(remote_path_prefix)
    
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    downlaod_helper = DownloadHelper( SERVER,
                                      access_key=ACCESS_KEY,
                                      secret_key=SECRET_KEY )
    # The return value of main().
    res = 0
    
    for remote_path in tqdm(remote_paths, desc=f'>> Downloading {len(remote_paths)} files'):
        
        local_path = os.path.join(
            'models_and_samples',
            remote_path[ n_char_remote_path_prefix + 1 : ]
        )
        
        os.makedirs( os.path.dirname(local_path), exist_ok=True )
        
        print(f'Downloading {remote_path} to \n {local_path}...')
    
        # Get the train and validate file lists.
        try:
            downlaod_helper.download( BUCKET_NAME,
                                      remote_path, 
                                      local_path )

        except Exception as exc:
            print(exc)
            res = 1
        
        print('')

    return res

if __name__ == "__main__":
    import sys
    sys.exit( main() )
    