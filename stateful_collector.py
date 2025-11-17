import numpy as np
import torch

def make_blank_image():
    # 1x1 black RGB image (ComfyUI tensor format)
    arr = np.zeros((1, 1, 3), dtype=np.float32)
    return torch.from_numpy(arr)[None, ...]

class StatefulImageCollector:
    """
    Stores 6 processed images in internal memory.
    Updates only the slot matching the provided index.
    Resets automatically when index == 0.
    Always outputs 6 images for preview.
    """

    # persistent class-level buffer
    buffer = [None, None, None, None, None, None]

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "processed_image": ("IMAGE",),
                "index": ("INT",),
            }
        }

    RETURN_TYPES = ("IMAGE", "IMAGE", "IMAGE", "IMAGE", "IMAGE", "IMAGE")
    RETURN_NAMES = ("slot1", "slot2", "slot3", "slot4", "slot5", "slot6")
    FUNCTION = "collect"
    CATEGORY = "image/sequence"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # force node to execute every queue job
        return float(torch.rand(1))

    def collect(self, processed_image, index):
        # safety clamp
        idx = max(0, min(5, index))

        # reset when index == 0
        if idx == 0:
            StatefulImageCollector.buffer = [None, None, None, None, None, None]

        # store image
        StatefulImageCollector.buffer[idx] = processed_image

        # build outputs with blanks for missing images
        outputs = []
        for img in StatefulImageCollector.buffer:
            if img is None:
                outputs.append(make_blank_image())
            else:
                outputs.append(img)

        return tuple(outputs)

NODE_CLASS_MAPPINGS = {
    "StatefulImageCollector": StatefulImageCollector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StatefulImageCollector": "Six Slot Image Buffer (Stateful)"
}
