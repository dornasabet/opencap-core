from utilsAugmenter import augmentTRC
import numpy as np
import os
baseDir=r"D:\opencap\opencap-core"
augmenterDir = os.path.join(baseDir, "MarkerAugmenter")
# logging.info('Augmenting marker set')
offset=0.1
vertical_offset = augmentTRC(
    'D:\opencap\opencap-core\data\mediapipe_body_3d_xyz_output_data.trc', 65.5,
    1.62, "pathAugmentedOutputFiles[trialName]",
    augmenterDir, offset=offset)
if len(e.args) == 2:  # specific exception
    raise Exception(e.args[0], e.args[1])
elif len(e.args) == 1:  # generic exception
    exception = "Marker augmentation failed. Verify your setup and try again. Visit https://www.opencap.ai/best-pratices to learn more about data collection and https://www.opencap.ai/troubleshooting for potential causes for a failed trial."
    raise Exception(exception, traceback.format_exc())
if offset:
    # If offset, no need to offset again for the webapp visualization.
    # (0.01 so that there is no overall offset, see utilsOpenSim).
    vertical_offset_settings = float(np.copy(vertical_offset) - 0.01)
    vertical_offset = 0.01
